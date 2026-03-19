#!/usr/bin/env python3
"""
AI Skill Bench - 批量测试执行器

用法:
    python scripts/run_benchmark.py --all
    python scripts/run_benchmark.py --category code
"""

import argparse
import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List
import requests
from tqdm import tqdm

# 模型配置
MODELS = {
    "qwen3.5-plus": {
        "provider": "bailian",
        "api_key": os.getenv("BAILIAN_API_KEY", "sk-sp-b5c69caecd864f5f9b37a1370f4d0299"),
        "base_url": "https://coding.dashscope.aliyuncs.com/v1",
        "model_id": "qwen3.5-plus"
    },
    "kimi-k2.5": {
        "provider": "moonshot",
        "api_key": os.getenv("MOONSHOT_API_KEY", ""),  # 需要配置
        "base_url": "https://api.moonshot.cn/v1",
        "model_id": "kimi-k2.5"
    }
}

def load_questions(category: str = None) -> List[dict]:
    """加载测试题目"""
    questions = []
    dataset_dir = Path(__file__).parent.parent / "dataset"
    
    if category:
        categories = [dataset_dir / category]
    else:
        categories = [d for d in dataset_dir.iterdir() if d.is_dir()]
    
    for cat_dir in categories:
        if not cat_dir.exists():
            continue
        for file in sorted(cat_dir.glob("*.json")):
            with open(file, 'r', encoding='utf-8') as f:
                question = json.load(f)
                question["category"] = cat_dir.name
                questions.append(question)
    
    return questions

def call_model(model_id: str, prompt: str) -> dict:
    """调用模型 API"""
    config = MODELS.get(model_id)
    if not config:
        raise ValueError(f"模型未配置：{model_id}")
    
    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": config["model_id"],
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 4000,
        "temperature": 0.3
    }
    
    start_time = time.time()
    try:
        response = requests.post(
            f"{config['base_url']}/chat/completions",
            headers=headers,
            json=payload,
            timeout=300
        )
        response.raise_for_status()
        result = response.json()
        
        usage = result.get("usage", {})
        end_time = time.time()
        
        return {
            "content": result["choices"][0]["message"]["content"],
            "input_tokens": usage.get("prompt_tokens", 0),
            "output_tokens": usage.get("completion_tokens", 0),
            "response_time": end_time - start_time,
            "status": "success"
        }
    except Exception as e:
        return {
            "content": "",
            "input_tokens": 0,
            "output_tokens": 0,
            "response_time": time.time() - start_time,
            "status": "failed",
            "error": str(e)
        }

def run_benchmark(questions: List[dict], models: List[str], output_dir: str):
    """运行基准测试"""
    os.makedirs(output_dir, exist_ok=True)
    
    all_results = []
    
    for model_id in tqdm(models, desc="模型"):
        print(f"\n🚀 测试模型：{model_id}")
        
        for question in tqdm(questions, desc="题目", leave=False):
            result = call_model(model_id, question["prompt"])
            
            result_record = {
                "question_id": question["id"],
                "category": question["category"],
                "model": model_id,
                "prompt": question["prompt"],
                "response": result["content"],
                "input_tokens": result["input_tokens"],
                "output_tokens": result["output_tokens"],
                "response_time": result["response_time"],
                "status": result["status"],
                "error": result.get("error", ""),
                "timestamp": datetime.now().isoformat()
            }
            
            all_results.append(result_record)
            
            # 延迟避免限流
            time.sleep(1)
    
    # 保存结果
    output_file = os.path.join(output_dir, f"benchmark_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            "metadata": {
                "total_questions": len(questions),
                "models": models,
                "timestamp": datetime.now().isoformat()
            },
            "results": all_results
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 结果已保存：{output_file}")
    return all_results

def generate_report(results: List[dict], output_dir: str):
    """生成对比报告"""
    # 按模型分组统计
    model_stats = {}
    for result in results:
        model = result["model"]
        if model not in model_stats:
            model_stats[model] = {
                "total": 0,
                "success": 0,
                "failed": 0,
                "total_tokens": 0,
                "total_time": 0
            }
        
        model_stats[model]["total"] += 1
        if result["status"] == "success":
            model_stats[model]["success"] += 1
        else:
            model_stats[model]["failed"] += 1
        model_stats[model]["total_tokens"] += result["input_tokens"] + result["output_tokens"]
        model_stats[model]["total_time"] += result["response_time"]
    
    # 生成 Markdown 报告
    report_lines = [
        "# AI 模型对比测试报告",
        "",
        f"**测试时间:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**题目数量:** {len(results) // len(model_stats)}",
        f"**测试模型:** {', '.join(model_stats.keys())}",
        "",
        "## 总体对比",
        "",
        "| 模型 | 总题数 | 成功 | 失败 | 成功率 | 总 Token | 平均响应时间 |",
        "|------|--------|------|------|--------|----------|--------------|"
    ]
    
    for model, stats in model_stats.items():
        success_rate = (stats["success"] / stats["total"] * 100) if stats["total"] > 0 else 0
        avg_time = stats["total_time"] / stats["total"] if stats["total"] > 0 else 0
        report_lines.append(
            f"| {model} | {stats['total']} | {stats['success']} | {stats['failed']} | "
            f"{success_rate:.1f}% | {stats['total_tokens']:,} | {avg_time:.2f}s |"
        )
    
    report_lines.extend([
        "",
        "## 详细结果",
        "",
        "见 JSON 文件：benchmark_*.json"
    ])
    
    # 保存报告
    report_file = os.path.join(output_dir, f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    print(f"\n📊 报告已保存：{report_file}")

def main():
    parser = argparse.ArgumentParser(description="AI Skill Bench - 批量测试执行器")
    parser.add_argument("--all", action="store_true", help="运行全部测试")
    parser.add_argument("--category", type=str, help="测试类别")
    parser.add_argument("--models", type=str, nargs='+', default=["qwen3.5-plus", "kimi-k2.5"], help="测试模型")
    parser.add_argument("--output", type=str, default="results", help="输出目录")
    
    args = parser.parse_args()
    
    # 加载题目
    questions = load_questions(args.category)
    if not questions:
        print("❌ 未找到测试题目")
        return
    
    print(f"📋 测试计划:")
    print(f"   模型：{', '.join(args.models)}")
    print(f"   题目：{len(questions)} 道")
    print(f"   预计时间：{len(questions) * len(args.models) * 2} 分钟")
    
    # 运行测试
    results = run_benchmark(questions, args.models, args.output)
    
    # 生成报告
    generate_report(results, args.output)

if __name__ == "__main__":
    main()
