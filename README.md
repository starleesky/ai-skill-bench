# AI Skill Bench - AI 技能测试基准

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AI 技能测试基准 - 客观评估大模型在真实场景下的能力表现**

---

## 📋 项目简介

AI Skill Bench 是一个标准化的 AI 模型测试框架，提供：

- ✅ **80 道精选题目** - 覆盖代码生成、逻辑推理、长文本理解等 6 大维度
- ✅ **自动化测试** - 一键执行测试，自动生成报告
- ✅ **多维度评分** - 功能正确性、代码规范、边界处理等
- ✅ **成本分析** - Token 消耗、API 成本统计
- ✅ **对比报告** - 多模型横向对比，可视化图表

---

## 🚀 快速开始

### 安装

```bash
git clone https://github.com/starleesky/ai-skill-bench.git
cd ai-skill-bench
pip install -r requirements.txt
```

### 配置 API

```bash
cp config.example.json config.json
# 编辑 config.json，填入你的 API Key
```

### 运行测试

```bash
# 运行全部测试
python run_tests.py --all

# 运行特定维度
python run_tests.py --category code
```

---

## 📊 测试维度

| 维度 | 题数 | 权重 | 说明 |
|------|------|------|------|
| 代码生成 | 25 | 25% | Python/JS/Java/SQL/Shell |
| 逻辑推理 | 20 | 20% | 数学、逻辑题、推理 |
| 长文本理解 | 10 | 20% | 文档摘要、信息提取 |
| 工具调用 | 15 | 15% | API 选择、参数构造 |
| 中文理解 | 10 | 10% | 语义、上下文、文化 |
| 响应速度 | 10 | 10% | 延迟、生成速度 |

---

## 🔒 安全说明

**本项目严格遵守安全最佳实践：**

- ✅ 不提交任何 API Key/密码到 Git
- ✅ 使用 `.gitignore` 保护敏感文件
- ✅ 示例配置使用占位符
- ✅ CI/CD 使用 GitHub Secrets（可选）

**严禁行为：**
- ❌ 提交 config.json（含真实 API Key）
- ❌ 在 Issue/PR 中暴露敏感信息
- ❌ 分享个人配置文件

---

## 📄 许可证

MIT License
