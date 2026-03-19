#!/usr/bin/env python3
"""简化的测试执行器"""

import json, os, time, requests
from datetime import datetime

API_KEY = "sk-sp-b5c69caecd864f5f9b37a1370f4d0299"
BASE_URL = "https://coding.dashscope.aliyuncs.com/v1"

def test_model(prompt):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {"model": "qwen3.5-plus", "messages": [{"role": "user", "content": prompt}], "max_tokens": 4000}
    
    start = time.time()
    resp = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=payload, timeout=300)
    result = resp.json()
    
    return {
        "content": result["choices"][0]["message"]["content"],
        "tokens": result.get("usage", {}),
        "time": time.time() - start
    }

# 测试第 1 题
with open("dataset/code/001_lru_cache.json") as f:
    q = json.load(f)

print(f"🧪 测试题目：{q['id']} - {q['category']}")
print(f"Prompt: {q['prompt'][:100]}...")

result = test_model(q["prompt"])
print(f"\n✅ 响应时间：{result['time']:.2f}s")
print(f"Tokens: {result['tokens']}")
print(f"\n📝 回答预览:\n{result['content'][:500]}...")

# 保存结果
os.makedirs("results/raw", exist_ok=True)
with open(f"results/raw/qwen_q{q['id']}.json", "w") as f:
    json.dump({"question": q, "response": result}, f, ensure_ascii=False, indent=2)

print(f"\n💾 结果已保存：results/raw/qwen_q{q['id']}.json")
