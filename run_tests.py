#!/usr/bin/env python3
"""
AI Skill Bench - 测试执行器

用法:
    python run_tests.py --all                     # 运行全部测试
    python run_tests.py --category code           # 运行代码生成测试
    python run_tests.py --model qwen3.5-plus      # 测试特定模型
"""

import argparse
import json
import os
import time
from datetime import datetime
from typing import Dict, List, Optional

import requests
from tqdm import tqdm


class ModelTester:
    """模型测试器"""
    
    def __init__(self, config_path: str = "config.json"):
        self.config = self._load_config(config_path)
        self.results = []
        self.stats = {
            "total_questions": 0,
            "completed": 0,
            "failed": 0,
            "total_tokens": 0,
            "total_cost": 0.0,
        }
    
    def _load_config(self, config_path: str) -> dict:
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"配置文件不存在：{config_path}")
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _call_model(self, model_id: str, prompt: str) -> dict:
        model_config = self.config["models"].get(model_id)
        if not model_config:
            raise ValueError(f"模型未配置：{model_id}")
        
        headers = {
            "Authorization": f"Bearer {model_config['api_key']}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model_config["model_id"],
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 4000,
            "temperature": 0.3
        }
        
        start_time = time.time()
        response = requests.post(
            f"{model_config['base_url']}/chat/completions",
            headers=headers,
            json=payload,
            timeout=self.config["test"]["timeout"]
        )
        end_time = time.time()
        
        response.raise_for_status()
        result = response.json()
        
        usage = result.get("usage", {})
        input_tokens = usage.get("prompt_tokens", 0)
        output_tokens = usage.get("completion_tokens", 0)
        
        pricing = model_config.get("pricing", {})
        cost = (input_tokens * pricing.get("input", 0) + 
                output_tokens * pricing.get("output", 0)) / 1_000_000
        
        return {
            "content": result["choices"][0]["message"]["content"],
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost": cost,
            "response_time": end_time - start_time,
        }
    
    def run_question(self, question: dict, model_id: str) -> dict:
        try:
            result = self._call_model(model_id, question["prompt"])
            return {
                "question_id": question["id"],
                "model": model_id,
                "status": "success",
                "response": result["content"],
                "input_tokens": result["input_tokens"],
                "output_tokens": result["output_tokens"],
                "cost": result["cost"],
                "response_time": result["response_time"],
            }
        except Exception as e:
            return {
                "question_id": question["id"],
                "model": model_id,
                "status": "failed",
                "error": str(e),
            }
    
    def save_results(self, results: List[dict], output_path: str):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({"results": results, "stats": self.stats}, f, ensure_ascii=False, indent=2)
        print(f"\n✅ 结果已保存：{output_path}")


def main():
    parser = argparse.ArgumentParser(description="AI Skill Bench - 测试执行器")
    parser.add_argument("--all", action="store_true", help="运行全部测试")
    parser.add_argument("--category", type=str, help="测试类别")
    parser.add_argument("--model", type=str, help="测试模型")
    parser.add_argument("--config", type=str, default="config.json", help="配置文件路径")
    args = parser.parse_args()
    
    try:
        tester = ModelTester(args.config)
    except FileNotFoundError as e:
        print(f"❌ {e}")
        print("提示：复制 config.example.json 为 config.json 并配置 API Key")
        return
    
    print(f"📋 测试计划：{args.model or 'all models'}")
    print("⚠️  请确保已配置 API Key")


if __name__ == "__main__":
    main()
