# 求职流 JobFlow for Codex

简体中文 | [English](README.en.md)

求职流 JobFlow for Codex 是一套给 Codex 使用的本地求职工作流。它把“找岗位、按规则筛选、打招呼、看消息、发简历、记录进度、生成日报”整理成可复用的流程、模板和脚本。

它适合正在主动找工作的用户，尤其适合希望用 Codex 辅助处理 BOSS 直聘、猎聘这类招聘网站的人。它不是自动投递外挂，也不会绕过验证码、登录、平台风控或安全限制。

## 你可以用它做什么

- 初始化一套本地求职工作区。
- 维护一份 `applications.jsonl` 求职台账。
- 用 `screening_rules.md` 记录你的岗位筛选规则。
- 让 Codex 按规则辅助筛选岗位。
- 让 Codex 检查招聘方消息并分类处理。
- 生成每日求职日报。
- 生成可审核的定时自动化 prompt。

## 适用场景

- 你正在找产品经理、增长、AI、Web3、运营、技术等岗位。
- 你希望每天固定节奏投递和跟进。
- 你希望有一份本地记录，知道哪些岗位已打招呼、已发简历、被拒、待回复。
- 你希望 Codex 帮你做重复流程，但关键判断仍由你确认。

## 前置条件

- 已安装 Codex，并能在本地运行 Python 脚本。
- Python 3.10 或更高版本。
- 如果要让 Codex 操作招聘网站，需要浏览器里已经登录对应平台。
- 如果要自动发送简历，需要先在本地配置简历文件路径。
- 如果要使用定时任务，需要你自己在 Codex 里创建或审核自动化 prompt。

## 兼容性说明

当前项目只在 Windows + 本地 Codex 工作流下自测通过。其他操作系统、浏览器控制方式或自动化模式可能也能使用，但需要使用者自行验证和适配。

## 快速开始

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

然后编辑：

- `user_profile.yaml`：你的目标岗位、城市、平台、简历路径。
- `screening_rules.md`：你的岗位偏好、必投信号、排除项。

## 常用命令

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

## 哪些地方需要你介入

求职流不会假装自己能完全无人值守。下面这些情况需要用户介入：

- 第一次使用前，你需要登录招聘平台。
- 遇到验证码、风控、安全确认时，需要你处理。
- 招聘方问微信、电话、薪资、到岗时间、面试时间时，需要你决定怎么回复。
- 招聘方的问题需要结合个人情况判断时，需要你回复。
- 启用定时自动化前，需要你审核生成的 prompt。
- 平台页面结构变化导致 Codex 无法确认成功状态时，需要你复核。

## 消息处理规则

Codex 可以辅助判断消息，但不会替你乱回复：

- 明确说不合适：更新为 `not_suitable`。
- 明确要简历：如果你配置了简历路径，可以发送简历并更新为 `resume_sent`。
- 需要判断的问题：标记为 `needs_user_action`，并提醒你处理。
- 无法确认的页面或消息：标记为 `needs_review`。

## 标准状态值

台账使用这些状态：

- `contacted`
- `resume_sent`
- `interviewed`
- `not_suitable`
- `needs_user_action`
- `needs_review`

你可以在日报里显示中文标签，但脚本会使用这些英文状态值。

## 数据保存在哪里

你的真实数据保存在你自己的 workspace，例如：

```text
/path/to/your/workspace/data/job_search/
```

这个仓库只提供插件、模板和脚本，不应该保存你的真实简历、账号信息、cookie、session 或真实求职台账。

## 项目结构

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

## 当前支持平台

- BOSS 直聘
- 猎聘

其他平台可以后续通过新增 reference 和流程规则支持。

## 当前限制

- 不能绕过验证码或平台风控。
- 不能保证平台一定允许自动化操作。
- 不能保证投递结果。
- 招聘网站页面变化后，可能需要更新平台操作规则。
- 复杂消息仍需要用户自己判断。
