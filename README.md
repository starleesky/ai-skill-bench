# AI Skill Bench - AI 模型测试基准

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/starleesky/ai-skill-bench/actions/workflows/test.yml/badge.svg)](https://github.com/starleesky/ai-skill-bench/actions)

**AI 技能测试基准 - 客观评估大模型在真实场景下的能力表现**

---

## 📋 项目简介

AI Skill Bench 是一个标准化的 AI 模型测试框架，提供：

- ✅ **80 道精选题目** - 覆盖代码生成、逻辑推理、长文本理解等 6 大维度
- ✅ **自动化测试** - 一键执行测试，自动生成报告
- ✅ **多维度评分** - 功能正确性、代码规范、边界处理等
- ✅ **成本分析** - Token 消耗、API 成本统计
- ✅ **对比报告** - 多模型横向对比，可视化图表

**测试维度：**

| 维度 | 题数 | 权重 | 说明 |
|------|------|------|------|
| **代码生成** | 25 | 25% | Python/JS/Java/SQL/Shell |
| **逻辑推理** | 20 | 20% | 数学、逻辑题、演绎归纳 |
| **长文本理解** | 10 | 20% | 文档摘要、信息提取 |
| **工具调用** | 15 | 15% | API 选择、参数构造 |
| **中文理解** | 10 | 10% | 语义、上下文、文化 |
| **响应速度** | 10 | 10% | 延迟、生成速度 |

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
# 或使用环境变量：
# export BAILIAN_API_KEY=sk-sp-xxx
# export MOONSHOT_API_KEY=sk-kimi-xxx
```

### 运行测试

```bash
# 运行全部测试
python scripts/run_benchmark.py --all

# 运行特定维度
python scripts/run_benchmark.py --category code

# 测试特定模型
python scripts/run_benchmark.py --models qwen3.5-plus
```

### 查看报告

```bash
# 查看最新报告
cat results/report_*.md

# 查看原始数据
cat results/benchmark_*.json
```

---

## 📊 当前进度

### 题目完成度

| 维度 | 已完成 | 总计 | 进度 |
|------|--------|------|------|
| 代码生成 | 5 | 25 | 20% |
| 逻辑推理 | 2 | 20 | 10% |
| 长文本理解 | 1 | 10 | 10% |
| 工具调用 | 1 | 15 | 7% |
| 中文理解 | 1 | 10 | 10% |
| 响应速度 | 1 | 10 | 10% |
| **总计** | **11** | **80** | **14%** |

### 模型对比

| 模型 | 提供商 | 状态 |
|------|--------|------|
| **Qwen3.5-Plus** | 阿里云百炼 | ✅ 已配置 |
| **Kimi-K2.5** | Moonshot | ⏳ 待配置 API Key |

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

## 📁 项目结构

```
ai-skill-bench/
├── README.md                 # 本文件
├── LICENSE                   # MIT 许可证
├── requirements.txt          # Python 依赖
├── config.example.json       # 配置模板
├── scripts/
│   ├── run_benchmark.py      # 批量测试执行器
│   └── generate_report.py    # 报告生成脚本
├── dataset/                  # 测试数据集
│   ├── code/                 # 代码生成 (25 题)
│   ├── logic/                # 逻辑推理 (20 题)
│   ├── longtext/             # 长文本理解 (10 题)
│   ├── tool/                 # 工具调用 (15 题)
│   ├── chinese/              # 中文理解 (10 题)
│   └── speed/                # 响应速度 (10 题)
├── results/                  # 测试结果
│   ├── raw/                  # 原始响应
│   ├── scored/               # 评分结果
│   └── reports/              # 对比报告
└── docs/                     # 文档
    ├── SCORING.md            # 评分标准
    └── ROADMAP.md            # 开发路线图
```

---

## 📈 评分标准

### 代码生成题

| 评分项 | 权重 | 说明 |
|--------|------|------|
| 功能正确 | 40% | 单元测试通过率 |
| 代码规范 | 20% | PEP8、命名、结构 |
| 边界处理 | 20% | 异常、边界条件 |
| 注释文档 | 10% | 文档字符串、注释 |
| 性能考虑 | 10% | 时间复杂度、优化 |

### 逻辑推理题

| 评分项 | 权重 | 说明 |
|--------|------|------|
| 答案正确 | 60% | 最终答案匹配 |
| 推理过程 | 30% | 步骤完整、逻辑清晰 |
| 步骤清晰 | 10% | 格式规范、易读 |

### 长文本理解

| 评分项 | 权重 | 说明 |
|--------|------|------|
| 信息完整 | 40% | 无遗漏关键点 |
| 准确无误 | 30% | 无错误信息 |
| 结构清晰 | 20% | 逻辑清晰、分层 |
| 简洁精炼 | 10% | 无冗余 |

---

## 🎯 开发路线图

### M1: 基础框架 (2026-03-19 ~ 2026-03-26)

- [x] ✅ 项目初始化
- [x] ✅ 测试执行器
- [x] ✅ 11 道测试题目
- [ ] ⏳ 80 道题目完成
- [ ] ⏳ 报告生成脚本

### M2: 完整数据集 (2026-03-27 ~ 2026-04-10)

- [ ] 代码生成 (25 题)
- [ ] 逻辑推理 (20 题)
- [ ] 长文本理解 (10 题)
- [ ] 工具调用 (15 题)
- [ ] 中文理解 (10 题)
- [ ] 响应速度 (10 题)

### M3: 可视化报告 (2026-04-11 ~ 2026-04-20)

- [ ] Markdown 报告模板
- [ ] HTML 交互式报告
- [ ] 雷达图 (6 维度对比)
- [ ] 成本趋势图
- [ ] JSON 数据导出

---

## 🔗 相关链接

- **GitHub:** https://github.com/starleesky/ai-skill-bench
- **Issues:** https://github.com/starleesky/ai-skill-bench/issues
- **Actions:** https://github.com/starleesky/ai-skill-bench/actions

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

**⭐ 如果对你有帮助，请给个 Star！**
