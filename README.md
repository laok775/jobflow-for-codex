# 求职流 JobFlow for Codex

[简体中文](#简体中文) | [English](#english)

## 简体中文

求职流 JobFlow for Codex 是一个面向 Codex 的本地求职工作流插件。它帮助用户初始化私有求职数据、维护 JSONL 求职台账、按规则筛选岗位、生成日报，并生成可人工审核的自动化 prompt。

它是一个求职辅助工作流，不是无人值守的批量投递外挂。它不会绕过验证码、反自动化机制、付费墙或平台安全检查。

### 包含什么

- Codex skill：`jobflow`
- BOSS 直聘和猎聘的平台操作参考
- 招聘方消息处理规则
- 岗位筛选规则指南
- 私有用户配置模板
- 本地台账校验、日报、目标检查和自动化 prompt 生成脚本

### 不包含什么

- 个人简历
- 平台账号、cookie、session 或凭据
- 真实求职台账
- 对平台接口可用性的保证
- 任何验证码或反自动化绕过能力

### 仓库结构

```text
.codex-plugin/
  plugin.json
skills/
  jobflow/
    SKILL.md
    references/
    scripts/
    templates/
```

### 快速开始

克隆仓库后，在你的私有工作区初始化 JobFlow：

```bash
python skills/jobflow/scripts/init_jobflow.py --workspace /path/to/your/workspace
```

这会创建：

```text
/path/to/your/workspace/data/job_search/
  user_profile.yaml
  screening_rules.md
  applications.jsonl
  automation_prompt.md
  reports/
```

然后编辑 `user_profile.yaml` 和 `screening_rules.md`，填入你自己的求职偏好和简历路径。

### 校验台账

```bash
python skills/jobflow/scripts/validate_ledger.py --workspace /path/to/your/workspace
```

### 生成日报

```bash
python skills/jobflow/scripts/summarize_day.py --workspace /path/to/your/workspace --date 2026-01-01
```

### 检查每日目标

```bash
python skills/jobflow/scripts/check_targets.py --workspace /path/to/your/workspace --date 2026-01-01 --boss 5 --liepin 5
```

### 生成自动化 Prompt

```bash
python skills/jobflow/scripts/build_automation_prompt.py --workspace /path/to/your/workspace --output /path/to/your/workspace/data/job_search/automation_prompt.generated.md
```

启用任何定时自动化前，请先人工审核生成的 prompt。

### 标准状态值

脚本使用可移植的 canonical status：

- `contacted`
- `resume_sent`
- `interviewed`
- `not_suitable`
- `needs_user_action`
- `needs_review`

下游用户可以在日报或界面中显示中文标签，但共享脚本建议始终依赖这些标准状态值。

### 隐私规则

发布到 GitHub 前请确认：

- 不提交真实简历。
- 不提交账号凭据、cookie、browser session 或 token。
- 不提交真实 `applications.jsonl`。
- 不提交真实 `user_profile.yaml`。
- 私有运行数据应该放在你自己的 workspace，不要放进插件仓库。

仓库里的 `.gitignore` 已经屏蔽了常见私有文件，但发布前仍然建议检查 `git status` 并运行敏感信息扫描。

### MVP 支持平台

- BOSS 直聘
- 猎聘

后续可以通过新增平台 reference 文件和更新工作流说明来支持更多平台。

### License

公开分发前建议补充许可证。

## English

JobFlow for Codex is a local, browser-assisted job-search workflow plugin for Codex. It helps a user initialize private job-search files, maintain a JSONL application ledger, apply screening rules, generate daily reports, and build reviewed automation prompts.

It is an assistant workflow, not an unattended mass-application bot. It does not bypass CAPTCHA, anti-bot controls, paywalls, or platform safety checks.

### What It Includes

- A Codex skill: `jobflow`
- Platform notes for BOSS Direct and Liepin
- Recruiter message handling rules
- Screening rule guidance
- Templates for private user setup
- Python scripts for local ledger validation, reports, target checks, and automation prompt generation

### What It Does Not Include

- Personal resumes
- Platform accounts, cookies, sessions, or credentials
- Real application ledgers
- Any guaranteed platform integration
- Any CAPTCHA or anti-bot bypass

### Repository Layout

```text
.codex-plugin/
  plugin.json
skills/
  jobflow/
    SKILL.md
    references/
    scripts/
    templates/
```

### Quick Start

Clone the repository and initialize a private workspace:

```bash
python skills/jobflow/scripts/init_jobflow.py --workspace /path/to/your/workspace
```

This creates:

```text
/path/to/your/workspace/data/job_search/
  user_profile.yaml
  screening_rules.md
  applications.jsonl
  automation_prompt.md
  reports/
```

Edit `user_profile.yaml` and `screening_rules.md` with your own job-search preferences and resume paths.

### Validate the Ledger

```bash
python skills/jobflow/scripts/validate_ledger.py --workspace /path/to/your/workspace
```

### Generate a Daily Report

```bash
python skills/jobflow/scripts/summarize_day.py --workspace /path/to/your/workspace --date 2026-01-01
```

### Check Daily Targets

```bash
python skills/jobflow/scripts/check_targets.py --workspace /path/to/your/workspace --date 2026-01-01 --boss 5 --liepin 5
```

### Build an Automation Prompt

```bash
python skills/jobflow/scripts/build_automation_prompt.py --workspace /path/to/your/workspace --output /path/to/your/workspace/data/job_search/automation_prompt.generated.md
```

Review the generated prompt before enabling any recurring automation.

### Canonical Status Values

Scripts use portable canonical values:

- `contacted`
- `resume_sent`
- `interviewed`
- `not_suitable`
- `needs_user_action`
- `needs_review`

Localized display labels can be added by downstream users, but shared tooling should rely on the canonical values.

### Privacy Rules

Before pushing this repository to GitHub:

- Do not commit real resumes.
- Do not commit account credentials, cookies, browser sessions, or tokens.
- Do not commit a real `applications.jsonl`.
- Do not commit a real `user_profile.yaml`.
- Keep private runtime data in your own workspace, not in the plugin repository.

The included `.gitignore` blocks the most common private files, but you should still inspect `git status` and run a secret scan before publishing.

### Supported Platforms in MVP

- BOSS Direct
- Liepin

Other platforms can be added later through new platform reference files and updated workflow instructions.

### License

Add a license before public distribution.
