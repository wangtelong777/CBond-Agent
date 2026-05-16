CBond-Agent

AI Multi-Agent Convertible Bond Quant Trading System

CBond-Agent 是一个基于 AI Multi-Agent 架构构建的可转债量化交易自动化系统。

项目目标并不仅仅是传统量化交易，而是希望通过 AI Agent 协同机制，实现：

AI 自主市场分析
AI 风险识别
AI 策略优化
AI 自动决策
自动交易执行
自动收益分析

最终形成一个可长期运行、自我优化的智能量化交易平台。

项目背景

传统量化系统大多数仍然依赖：

固定策略
人工调参
人工监控
单一逻辑执行

而 CBond-Agent 引入了 AI Multi-Agent 协同架构，使系统能够像“交易团队”一样工作。

不同 AI Agent 负责不同任务，并通过协同机制共同完成交易决策。

项目核心理念：

“让 AI 不只是分析工具，而是真正参与交易决策与风险控制。”

多 Agent 协同架构

系统当前设计了多个 AI Agent：

Agent	职责
Market Agent	市场情绪分析
Research Agent	新闻与公告研究
Strategy Agent	策略生成与参数优化
Risk Agent	风险控制与仓位调整
Trade Agent	自动执行交易
Summary Agent	每日收益分析与总结
Multi-Agent 工作流程
市场数据
   ↓
Research Agent 分析新闻与公告
   ↓
Market Agent 评估市场情绪
   ↓
Strategy Agent 生成交易信号
   ↓
Risk Agent 评估风险等级
   ↓
Trade Agent 自动执行交易
   ↓
Summary Agent 自动生成交易总结

整个系统并非单一模型调用，而是多个 AI Agent 之间协同工作。

这种架构更接近真实 AI Autonomous System（AI 自主系统）。

系统核心能力
1. AI 市场情绪分析

系统通过 LLM 对：

新闻
公告
热点板块
社交媒体情绪
市场波动

进行语义分析。

输出：

市场情绪评分
风险等级
仓位建议
2. AI 风险控制

Risk Agent 自动监控：

最大回撤
波动率异常
持仓风险
市场极端行情
黑天鹅事件

当风险超过阈值时：

自动减仓
自动暂停交易
自动发出风险通知
3. AI 策略优化

Strategy Agent 会根据历史数据动态优化：

买卖阈值
网格间距
仓位比例
止盈止损
因子权重

未来计划接入：

PPO
强化学习
AutoML
多因子 AI 模型
4. 自动化交易执行

Trade Agent 能够自动：

生成买卖信号
执行交易
记录日志
推送通知

未来将支持：

QMT
掘金
同花顺
券商 API

实现真实自动交易。

项目技术栈
模块	技术
后端	Python
Web API	FastAPI
AI 模型	OpenAI / DeepSeek
数据分析	Pandas / NumPy
数据源	AkShare
数据库	PostgreSQL
缓存	Redis
部署	Docker
通知	Telegram Bot
项目定位

CBond-Agent 并不是简单的量化脚本。

项目定位是：

“AI Agent 驱动的智能金融自动化系统。”

重点在于：

AI 决策能力
多 Agent 协同
自主分析能力
自动化执行能力
长期自我优化能力
