# AI Skill Bench 开发路线图

**版本：** v1.0  
**创建日期：** 2026-03-19  
**项目：** [ai-skill-bench](https://github.com/starleesky/ai-skill-bench)

---

## 🎯 项目愿景

打造业界标准的 AI 模型测试基准，客观评估大模型在真实场景下的能力表现。

**定期测评：** 每月更新测试题目，每季度发布新模型对比报告。

---

## 📋 里程碑

### M1: 基础框架 (2026-03-19 ~ 2026-03-26)

**目标：** 完成项目框架和首批测试题目

- [x] ✅ 项目初始化 (README, LICENSE, 目录结构)
- [x] ✅ 测试执行器 (run_benchmark.py)
- [x] ✅ 配置文件模板 (config.example.json)
- [x] ✅ 11 道测试题目
- [ ] ⏳ 80 道题目全部完成
- [ ] ⏳ 报告生成脚本 (generate_report.py)

**验收标准：**
- 能运行批量测试
- 能生成基础报告
- 题目覆盖 6 大维度

---

### M2: 完整数据集 (2026-03-27 ~ 2026-04-10)

**目标：** 完成全部 80 道测试题目

- [ ] 代码生成 (25 题) - Python/JS/Java/SQL/Shell
- [ ] 逻辑推理 (20 题) - 数学/逻辑谜题/演绎归纳
- [ ] 长文本理解 (10 题) - 文档摘要/合同提取
- [ ] 工具调用 (15 题) - API 选择/参数构造
- [ ] 中文理解 (10 题) - 语义/上下文/文化
- [ ] 响应速度 (10 题) - 延迟/生成速度测试

**验收标准：**
- 80 题全部完成
- 每道题包含 prompt 和评分标准
- 至少 2 个模型的测试结果

---

### M3: 可视化报告 (2026-04-11 ~ 2026-04-20)

**目标：** 实现专业的可视化报告

- [ ] Markdown 报告模板
- [ ] HTML 交互式报告
- [ ] 雷达图 (6 维度对比)
- [ ] 成本趋势图
- [ ] JSON 数据导出
- [ ] PDF 导出

**验收标准：**
- 一键生成完整报告
- 图表清晰美观
- 支持多模型对比

---

### M4: 定期测评 (2026-04-21 起)

**目标：** 建立定期测评机制

- [ ] 每月更新测试题目 (10-20 道)
- [ ] 每季度发布新模型对比
- [ ] 建立社区贡献机制
- [ ] GitHub Actions 自动化

**验收标准：**
- GitHub Star > 100
- 至少 10 个外部贡献者
- 被 3 个以上项目引用

---

## 📊 题目创作指南

### 题目格式

```json
{
  "id": 1,
  "category": "code",
  "subcategory": "python",
  "difficulty": "medium",
  "prompt": "请用 Python 实现...",
  "expected_output": "完整的 XX 类实现",
  "scoring": {
    "functionality": 40,
    "code_style": 20,
    "boundary_handling": 20,
    "comments": 10,
    "performance": 10
  },
  "test_cases": [...]
}
```

### 题目质量要求

1. **明确性** - prompt 清晰无歧义
2. **可评分** - 有明确的评分标准
3. **真实性** - 贴近真实场景
4. **难度分级** - easy/medium/hard
5. **覆盖全面** - 覆盖各难度和场景

---

## 🤝 贡献指南

### 如何参与

1. **Fork 项目** - https://github.com/starleesky/ai-skill-bench/fork
2. **创建分支** - `git checkout -b feature/add-questions`
3. **添加题目** - 在 dataset/ 目录下创建 JSON 文件
4. **提交更改** - `git commit -m 'feat: 添加 5 道代码题'`
5. **创建 PR** - https://github.com/starleesky/ai-skill-bench/pulls

### 题目提交要求

- [ ] 题目格式符合规范
- [ ] 包含评分标准
- [ ] 至少 3 个测试用例
- [ ] 无敏感信息

---

## 📈 项目指标

### 代码质量

| 指标 | 目标 | 当前 |
|------|------|------|
| 测试覆盖率 | >80% | - |
| 代码规范 | PEP8 | ✅ |
| 文档完整度 | >90% | 60% |

### 社区指标

| 指标 | 目标 | 当前 |
|------|------|------|
| GitHub Stars | 100+ | 0 |
| Forks | 20+ | 0 |
| 贡献者 | 10+ | 1 |
| Issues | 20+ | 0 |

---

## 🔗 相关链接

- **GitHub:** https://github.com/starleesky/ai-skill-bench
- **Issues:** https://github.com/starleesky/ai-skill-bench/issues
- **参考项目:**
  - [OpenAI Harness Engineering](https://openai.com/zh-Hans-CN/index/harness-engineering/)
  - [agency-agents](https://github.com/msitarzewski/agency-agents)

---

**最后更新：** 2026-03-19  
**维护者：** @starleesky
