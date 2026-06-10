# 求职流 JobFlow for Codex

[简体中文](#简体中文) | [English](#english)

## 简体中文

求职流 JobFlow for Codex 是一套给 Codex 使用的本地求职工作流。它把“找岗位、按规则筛选、打招呼、看消息、发简历、记录进度、生成日报”整理成可复用的流程、模板和脚本。

它适合正在主动找工作的用户，尤其适合希望用 Codex 辅助处理 BOSS 直聘、猎聘这类招聘网站的人。它不是自动投递外挂，也不会绕过验证码、登录、平台风控或安全限制。

### 你可以用它做什么

- 初始化一套本地求职工作区。
- 维护一份 `applications.jsonl` 求职台账。
- 用 `screening_rules.md` 记录你的岗位筛选规则。
- 让 Codex 按规则辅助筛选岗位。
- 让 Codex 检查招聘方消息并分类处理。
- 生成每日求职日报。
- 生成可审核的定时自动化 prompt。

### 适用场景

- 你正在找产品经理、增长、AI、Web3、运营、技术等岗位。
- 你希望每天固定节奏投递和跟进。
- 你希望有一份本地记录，知道哪些岗位已打招呼、已发简历、被拒、待回复。
- 你希望 Codex 帮你做重复流程，但关键判断仍由你确认。

### 前置条件

- 已安装 Codex，并能在本地运行 Python 脚本。
- Python 3.10 或更高版本。
- 如果要让 Codex 操作招聘网站，需要浏览器里已经登录对应平台。
- 如果要自动发送简历，需要先在本地配置简历文件路径。
- 如果要使用定时任务，需要你自己在 Codex 里创建或审核自动化 prompt。

### 这个项目包含什么

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

核心内容：

- `SKILL.md`：告诉 Codex 如何执行求职流。
- `references/`：BOSS 直聘、猎聘、消息处理、筛选规则说明。
- `templates/`：用户配置、筛选规则、台账、日报、自动化 prompt 模板。
- `scripts/`：初始化、校验台账、生成日报、检查目标、生成自动化 prompt。

### 快速开始

克隆仓库后，进入项目目录：

```bash
git clone https://github.com/laok775/jobflow-for-codex.git
cd jobflow-for-codex
```

初始化你的私有求职工作区：

```bash
python skills/jobflow/scripts/init_jobflow.py --workspace /path/to/your/workspace
```

它会创建：

```text
/path/to/your/workspace/data/job_search/
  user_profile.yaml
  screening_rules.md
  applications.jsonl
  automation_prompt.md
  reports/
```

然后你需要编辑：

- `user_profile.yaml`：你的目标岗位、城市、平台、简历路径。
- `screening_rules.md`：你的岗位偏好、必投信号、排除项。

### 常用命令

校验求职台账：

```bash
python skills/jobflow/scripts/validate_ledger.py --workspace /path/to/your/workspace
```

生成某天日报：

```bash
python skills/jobflow/scripts/summarize_day.py --workspace /path/to/your/workspace --date 2026-01-01
```

检查当天投递目标是否达成：

```bash
python skills/jobflow/scripts/check_targets.py --workspace /path/to/your/workspace --date 2026-01-01 --boss 5 --liepin 5
```

生成定时自动化 prompt：

```bash
python skills/jobflow/scripts/build_automation_prompt.py --workspace /path/to/your/workspace --output /path/to/your/workspace/data/job_search/automation_prompt.generated.md
```

### 哪些地方需要你介入

求职流不会假装自己能完全无人值守。下面这些情况需要用户介入：

- 第一次使用前，你需要登录招聘平台。
- 遇到验证码、风控、安全确认时，需要你处理。
- 招聘方问微信、电话、薪资、到岗时间、面试时间时，需要你决定怎么回复。
- 招聘方的问题需要结合个人情况判断时，需要你回复。
- 启用定时自动化前，需要你审核生成的 prompt。
- 平台页面结构变化导致 Codex 无法确认成功状态时，需要你复核。

### 消息处理规则

Codex 可以辅助判断消息，但不会替你乱回复：

- 明确说不合适：更新为 `not_suitable`。
- 明确要简历：如果你配置了简历路径，可以发送简历并更新为 `resume_sent`。
- 需要判断的问题：标记为 `needs_user_action`，并提醒你处理。
- 无法确认的页面或消息：标记为 `needs_review`。

### 标准状态值

台账使用这些状态：

- `contacted`
- `resume_sent`
- `interviewed`
- `not_suitable`
- `needs_user_action`
- `needs_review`

你可以在日报里显示中文标签，但脚本会使用这些英文状态值。

### 数据保存在哪里

你的真实数据保存在你自己的 workspace，例如：

```text
/path/to/your/workspace/data/job_search/
```

这个仓库只提供插件、模板和脚本，不应该保存你的真实简历、账号信息、cookie、session 或真实求职台账。

### 当前支持平台

- BOSS 直聘
- 猎聘

其他平台可以后续通过新增 reference 和流程规则支持。

### 当前限制

- 不能绕过验证码或平台风控。
- 不能保证平台一定允许自动化操作。
- 不能保证投递结果。
- 招聘网站页面变化后，可能需要更新平台操作规则。
- 复杂消息仍需要用户自己判断。

## English

JobFlow for Codex is a local job-search workflow for Codex. It organizes job discovery, screening, recruiter contact, message review, resume sending, progress tracking, and daily reports into reusable templates, scripts, and Codex skill instructions.

It is designed for users who want Codex to assist with repetitive job-search workflows on platforms such as BOSS Direct and Liepin. It is not a mass-application bot and does not bypass CAPTCHA, login, platform risk controls, or safety checks.

### What You Can Do With It

- Initialize a private local job-search workspace.
- Maintain an `applications.jsonl` application ledger.
- Store screening rules in `screening_rules.md`.
- Ask Codex to screen roles against your rules.
- Ask Codex to review recruiter messages and classify them.
- Generate daily job-search reports.
- Generate reviewable automation prompts for scheduled runs.

### When To Use It

- You are actively searching for jobs.
- You want a regular daily application and follow-up rhythm.
- You want a local record of contacted, resume-sent, rejected, and pending roles.
- You want Codex to handle repetitive workflow steps while keeping human judgment in the loop.

### Prerequisites

- Codex installed locally.
- Python 3.10 or newer.
- Logged-in browser sessions for supported job platforms if you want Codex to operate websites.
- Local resume file paths configured if you want resume sending support.
- Reviewed automation prompts if you want scheduled runs.

### Project Contents

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

Main parts:

- `SKILL.md`: workflow instructions for Codex.
- `references/`: platform notes, message rules, and screening guidance.
- `templates/`: user profile, screening rules, ledger, report, and automation prompt templates.
- `scripts/`: initialization, ledger validation, report generation, target checks, and prompt generation.

### Quick Start

Clone the repository:

```bash
git clone https://github.com/laok775/jobflow-for-codex.git
cd jobflow-for-codex
```

Initialize your private workspace:

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

Then edit:

- `user_profile.yaml`: target roles, cities, platforms, and resume paths.
- `screening_rules.md`: priorities, must-apply signals, and exclusions.

### Common Commands

Validate the ledger:

```bash
python skills/jobflow/scripts/validate_ledger.py --workspace /path/to/your/workspace
```

Generate a daily report:

```bash
python skills/jobflow/scripts/summarize_day.py --workspace /path/to/your/workspace --date 2026-01-01
```

Check daily targets:

```bash
python skills/jobflow/scripts/check_targets.py --workspace /path/to/your/workspace --date 2026-01-01 --boss 5 --liepin 5
```

Build an automation prompt:

```bash
python skills/jobflow/scripts/build_automation_prompt.py --workspace /path/to/your/workspace --output /path/to/your/workspace/data/job_search/automation_prompt.generated.md
```

### Where User Input Is Required

JobFlow is not fully unattended. User intervention is required when:

- You need to log in to job platforms.
- A CAPTCHA, risk control, or safety confirmation appears.
- A recruiter asks for WeChat, phone, salary details, availability, or interview time.
- A recruiter asks a question that requires personal judgment.
- You enable scheduled automation and need to review the generated prompt.
- A platform UI changes and Codex cannot confirm success state.

### Message Handling

Codex can help classify messages, but should not make judgment-heavy replies for you:

- Clearly unsuitable: set status to `not_suitable`.
- Resume requested: send the configured resume when possible and set status to `resume_sent`.
- Judgment required: set status to `needs_user_action`.
- Unclear or unconfirmed: set status to `needs_review`.

### Status Values

The ledger uses:

- `contacted`
- `resume_sent`
- `interviewed`
- `not_suitable`
- `needs_user_action`
- `needs_review`

### Where Data Is Stored

Your real data stays in your own workspace, for example:

```text
/path/to/your/workspace/data/job_search/
```

This repository contains only the plugin, templates, and scripts. It should not contain real resumes, account data, cookies, sessions, or real application records.

### Supported Platforms

- BOSS Direct
- Liepin

More platforms can be added later through new references and workflow rules.

### Limitations

- Does not bypass CAPTCHA or platform risk controls.
- Does not guarantee that a platform allows automation.
- Does not guarantee job-search outcomes.
- Platform UI changes may require workflow updates.
- Complex recruiter messages still require user judgment.
