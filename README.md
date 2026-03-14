# 🌟 女装图片保存助手

> **项目来源**：基于 [astrbot_plugin_stealer](https://github.com/nagatoquin33/astrbot_plugin_stealer) 重构
> 
> AstrBot 插件 - 自动识别并保存群友的女装图片，支持 SMTP 邮件推送每日统计日报

[![AstrBot](https://img.shields.io/badge/AstrBot-Plugin-blue)](https://github.com/Soulter/AstrBot)
[![Python](https://img.shields.io/badge/Python-3.10+-green.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-1.1.0-orange.svg)](https://github.com/WUHINS/astrbot_plugin_cosplay_saver)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

自动识别并保存群友的女装图片到对应目录。使用视觉模型（VLM）进行 AI 识别，支持宽松判断策略，确保不漏掉任何女装图片。图片按"群号/群员 QQ 号_QQ 名"的目录结构自动组织，支持 SMTP 邮件推送每日统计日报。

**注意**：本插件移除了原项目的表情包偷取和自动发送功能，专注于女装图片识别与保存。

---

## ✨ 功能特性

### 🎯 核心功能
- **AI 智能识别** - 使用视觉语言模型（VLM）自动识别女装图片
- **宽松判断策略** - 宁可误判不漏判，确保捕获所有女装图片
- **自动分类保存** - 按"群号/群员 QQ 号_QQ 名"目录结构自动组织
- **多格式支持** - 支持 JPG、PNG、GIF、WebP 等常见图片格式

### 🎬 高级功能
- **GIF 动图处理** - 自动提取 GIF 关键帧进行识别
- **忽略 GIF 选项** - 可配置跳过所有 GIF 图片
- **SMTP 邮件推送** - 每日定时发送统计日报到邮箱
- **多模型支持** - 支持配置专用识别模型

### ⚡ 性能优化
- **异步处理** - 所有 IO 操作使用异步方式，不阻塞主事件循环
- **智能缓存** - 图片识别结果缓存，避免重复识别
- **资源管理** - 自动清理临时文件，完善的异常处理

---

## 📦 快速开始

### 安装方式

#### 方式一：通过 AstrBot 插件市场（推荐）

在 AstrBot 插件管理中搜索并安装 `astrbot_plugin_cosplay_saver`。

#### 方式二：手动安装

```bash
# 1. 克隆或下载插件到 AstrBot 的 data/plugins 目录
cd /path/to/AstrBot/data/plugins
git clone https://github.com/nagatoquin33/astrbot_plugin_cosplay_saver.git

# 2. 安装依赖
pip install -r astrbot_plugin_cosplay_saver/requirements.txt

# 3. 在 AstrBot 管理界面启用插件
```

### 依赖要求

- Python 3.10+
- AstrBot 4.10.4+
- Pillow >= 10.0.0
- numpy >= 1.24.0

---

## ⚙️ 配置说明

### 基础配置

```json
{
  "save_cosplay_images": true,
  "cosplay_detection_threshold": 0.6,
  "cosplay_vision_provider_id": "",
  "vision_provider_id": "",
  "ignore_gif": false,
  "smtp": {
    "enabled": false,
    "smtp_server": "smtp.qq.com",
    "smtp_port": 587,
    "sender_email": "",
    "sender_password": "",
    "receiver_email": "",
    "use_tls": true,
    "send_time": "08:00"
  }
}
```

### 配置项详解

#### 女装图片识别

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `save_cosplay_images` | bool | `true` | 是否开启女装图片保存 |
| `cosplay_detection_threshold` | float | `0.6` | 识别阈值（0.3-0.9，越低越宽松） |
| `cosplay_vision_provider_id` | string | `""` | 女装识别专用模型（留空使用默认） |
| `vision_provider_id` | string | `""` | 视觉模型（留空使用全局默认） |
| `ignore_gif` | bool | `false` | 是否忽略 GIF 图片 |

#### SMTP 邮件推送

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `enabled` | bool | `false` | 是否启用邮件推送 |
| `smtp_server` | string | `""` | SMTP 服务器地址 |
| `smtp_port` | int | `587` | SMTP 端口 |
| `sender_email` | string | `""` | 发件人邮箱 |
| `sender_password` | string | `""` | 邮箱授权码 |
| `receiver_email` | string | `""` | 收件人邮箱 |
| `use_tls` | bool | `true` | 是否使用 TLS 加密 |
| `send_time` | string | `"08:00"` | 每日发送时间（24 小时制） |

---

## 📧 SMTP 邮件推送配置

### 配置步骤

#### 1. 获取邮箱授权码

**QQ 邮箱示例**：
1. 登录 QQ 邮箱网页版（mail.qq.com）
2. 进入"设置" → "账户"
3. 开启 "POP3/SMTP 服务"
4. 点击"生成授权码"
5. 获取授权码（不是登录密码！）

**其他邮箱**：
- 163 邮箱：设置 → POP3/SMTP/IMAP
- Gmail：设置 → 转发和 POP/IMAP → 启用 IMAP
- Outlook：设置 → 邮件 → 同步电子邮件

#### 2. 配置 SMTP 参数

```json
{
  "smtp": {
    "enabled": true,
    "smtp_server": "smtp.qq.com",
    "smtp_port": 587,
    "sender_email": "your_email@qq.com",
    "sender_password": "your_auth_code",
    "receiver_email": "receiver@qq.com",
    "use_tls": true,
    "send_time": "08:00"
  }
}
```

#### 3. 常用邮箱 SMTP 配置

| 邮箱服务商 | SMTP 服务器 | 端口 | 加密方式 |
|-----------|------------|------|---------|
| **QQ 邮箱** | smtp.qq.com | 587/465 | TLS |
| **163 邮箱** | smtp.163.com | 587/465 | TLS |
| **126 邮箱** | smtp.126.com | 587/465 | TLS |
| **Gmail** | smtp.gmail.com | 587 | TLS |
| **Outlook** | smtp-mail.outlook.com | 587 | TLS |
| **新浪邮箱** | smtp.sina.com | 587 | TLS |

#### 4. 测试发送

配置完成后，重启插件，系统会自动验证配置。如需测试，可等待次日自动发送或手动触发（待实现命令功能）。

### 日报内容示例

**邮件主题**：🌟 女装图片统计日报 - 2026-03-13

**邮件内容**：
- 📊 **总体统计**
  - 保存图片总数：156 张
  - 活跃群组数：8 个
  - 活跃用户数：45 人

- 📈 **群组详情**
  - 群号、活跃用户数、保存图片数、用户列表

- 📅 **统计信息**
  - 统计日期、报告生成时间

---

## 🎯 使用说明

### 自动保存

插件会自动监听所有群聊消息中的图片，检测到女装图片后自动保存到：

```
数据目录/cosplay/群号/群员 QQ 号_QQ 名/时间戳_图片名.jpg
```

### 目录结构

```
data/
└── astrbot_plugin_cosplay_saver/
    └── cosplay/
        ├── 12345678/
        │   ├── 111111_小明/
        │   │   ├── 20260313_120000_image1.jpg
        │   │   └── 20260313_150000_image2.png
        │   └── 222222_小红/
        │       └── 20260313_180000_image3.jpg
        └── 87654321/
            └── 333333_小美/
                └── 20260313_200000_image4.gif
```

### 识别阈值调整

**推荐配置**：

| 场景 | 阈值 | 说明 |
|------|------|------|
| **宽松模式** | 0.5-0.6 | 推荐，平衡误判和漏判 |
| **非常宽松** | 0.3-0.5 | 几乎不会漏掉，但可能误判 |
| **严格模式** | 0.7-0.9 | 只保存明显的女装图片 |

### GIF 处理

- **ignore_gif = false**（默认）：正常处理 GIF 图片，提取关键帧识别
- **ignore_gif = true**：跳过所有 GIF 图片，不检测不保存

**建议**：
- 如果群聊中 GIF 很多且不想保存 → 开启 `ignore_gif`
- 如果想保存所有女装图片 → 关闭 `ignore_gif`

---

## 🔍 工作原理

```
消息监听
    ↓
检查图片（跳过 GIF 如果启用）
    ↓
下载原图
    ↓
AI 识别（VLM 模型）
    ↓
结果解析（宽松判断）
    ↓
保存文件（群号/用户/图片）
    ↓
缓存结果（避免重复）
    ↓
定时统计（每日）
    ↓
SMTP 推送（邮件日报）
```

---

## 🛡️ 隐私与安全

- ✅ **本地存储**：所有图片存储在本地，不会上传到任何服务器
- ✅ **权限控制**：支持删除功能，可随时清理不需要的图片
- ✅ **自动清理**：自动清理临时文件，避免磁盘占用
- ✅ **异常处理**：完善的异常处理和日志记录
- ✅ **加密传输**：SMTP 支持 TLS 加密，保护邮箱凭证

---

## ⚠️ 注意事项

### 模型费用
- 使用付费模型（如 GPT-4o、Claude）会产生费用
- 建议使用轻量免费模型或设置识别冷却时间
- GIF 动图会提取多帧识别，增加费用

### 存储管理
- 图片会持续累积，建议定期清理
- 可设置磁盘空间监控
- 重要图片建议备份

### 隐私保护
- 请确保在合适的群聊中使用
- 尊重他人隐私，不要滥用
- 遵守相关法律法规

### 性能优化
- 大量图片时建议开启 `ignore_gif`
- 可调整识别阈值减少误判
- 设置合理的模型调用频率

---

## 📊 插件结构

```
astrbot_plugin_cosplay_saver/
├── core/
│   ├── config.py                  # 配置管理（Pydantic）
│   ├── event_handler.py           # 事件处理（消息监听）
│   ├── image_processor_service.py # 图片处理（AI 识别）
│   ├── smtp_service.py            # SMTP 邮件服务
│   ├── daily_report_service.py    # 日报生成服务
│   └── task_scheduler.py          # 定时任务调度器
├── main.py                        # 插件入口
├── _conf_schema.json             # 配置 Schema
├── requirements.txt              # Python 依赖
├── metadata.yaml                 # 插件元数据
├── README.md                     # 文档
└── LICENSE                       # 许可证
```

---

## 🐛 问题反馈

遇到问题或有建议？欢迎：

- 📝 提 [Issue](https://github.com/WUHINS/astrbot_plugin_cosplay_saver/issues)
- 💬 加入 AstrBot 交流群讨论
- ⭐ 给项目一个 Star 支持

---

## 📝 更新日志

### v1.1.0 (2026-03-13)
- ✨ **新增 SMTP 邮件推送功能**
  - 每日定时发送统计日报
  - 支持 HTML 和纯文本格式
  - 支持多个邮箱服务商
- ✨ **新增忽略 GIF 选项**
  - 可配置跳过所有 GIF 图片
  - 减少识别费用和时间
- 🐛 修复已知问题
- 📚 完善文档

### v1.0.0 (2026-03-12)
- 🎉 初始版本发布
- ✨ 女装图片 AI 识别和自动保存
- ✨ 支持多模型轮询
- ✨ 宽松判断策略
- ✨ 自动分类保存

---

## 📄 许可证

MIT License

Copyright (c) 2026 nagatoquin33

详见 [LICENSE](LICENSE) 文件。

---

## 👥 作者

**WUHINS**

- GitHub: [@WUHINS](https://github.com/WUHINS)
- 项目：[astrbot_plugin_cosplay_saver](https://github.com/WUHINS/astrbot_plugin_cosplay_saver)

---

## 🙏 致谢

- [AstrBot](https://github.com/Soulter/AstrBot) - 强大的聊天机器人框架
- [Pillow](https://python-pillow.org/) - Python 图像处理库
- 所有贡献者和使用者

---

<div align="center">

**⚠️ 免责声明**

本插件仅供学习和娱乐使用。

请合理使用并遵守相关法律法规。

尊重他人隐私，不要滥用此插件。

---

Made with ❤️ by WUHINS

</div>
