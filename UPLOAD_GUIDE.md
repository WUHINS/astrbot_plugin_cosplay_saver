# Git 上传指南

由于你的系统没有安装 Git 命令行工具，以下是几种上传代码到 GitHub 的方法：

## 方法一：使用 GitHub Desktop（推荐）

1. **下载并安装 GitHub Desktop**
   - 访问：https://desktop.github.com/
   - 下载并安装

2. **克隆仓库**
   - 打开 GitHub Desktop
   - 选择 `File` → `Clone Repository`
   - 选择 URL 标签
   - 输入：`https://github.com/WUHINS/astrbot_plugin_cosplay_saver.git`
   - 选择本地路径：`C:\Users\HINS\Documents\Trae\astrbot_plugin_stealer`
   - 点击 Clone

3. **提交更改**
   - GitHub Desktop 会检测到所有更改
   - 在 Summary 输入：`feat: 女装图片保存助手 v1.1.0`
   - 在 Description 输入：`基于 astrbot_plugin_stealer 重构，新增 SMTP 邮件推送和忽略 GIF 功能`
   - 点击 `Commit to main`

4. **推送更改**
   - 点击右上角的 `Push origin` 按钮

## 方法二：使用 VS Code

1. **打开项目**
   - 用 VS Code 打开 `C:\Users\HINS\Documents\Trae\astrbot_plugin_stealer`

2. **配置 Git**
   - 点击左侧的 Git 图标（或按 `Ctrl+Shift+G`）
   - 如果是第一次使用，会提示安装 Git

3. **暂存更改**
   - 点击 `+` 号暂存所有文件
   - 或点击 `Changes` 上方的 `+` 号暂存所有

4. **提交更改**
   - 输入提交信息：`feat: 女装图片保存助手 v1.1.0`
   - 按 `Ctrl+Enter` 提交

5. **推送更改**
   - 点击底部的 `同步更改` 或 `发布分支` 按钮

## 方法三：安装 Git 命令行

1. **下载 Git**
   - 访问：https://git-scm.com/download/win
   - 下载并安装

2. **打开终端**
   ```bash
   cd C:\Users\HINS\Documents\Trae\astrbot_plugin_stealer
   ```

3. **执行上传命令**
   ```bash
   # 添加所有文件
   git add .
   
   # 提交
   git commit -m "feat: 女装图片保存助手 v1.1.0 - 基于 astrbot_plugin_stealer 重构，新增 SMTP 邮件推送和忽略 GIF 功能"
   
   # 添加远程仓库（如果还没有）
   git remote add origin https://github.com/WUHINS/astrbot_plugin_cosplay_saver.git
   
   # 推送
   git push -u origin main
   ```

## 方法四：使用 GitHub 网页上传（适合小文件）

1. **访问仓库**
   - 打开：https://github.com/WUHINS/astrbot_plugin_cosplay_saver

2. **上传文件**
   - 点击 `Add file` → `Upload files`
   - 拖拽文件到页面
   - 输入提交信息
   - 点击 `Commit changes`

## 推荐

**推荐使用 GitHub Desktop**，图形化界面操作简单，不需要记命令行。

## 注意事项

1. **确保已登录 GitHub**
   - 在上传前确保你已经登录到 GitHub 账号

2. **确认仓库权限**
   - 确保你有 `WUHINS/astrbot_plugin_cosplay_saver` 仓库的写入权限

3. **首次推送**
   - 如果是第一次推送到该仓库，可能需要输入 GitHub 账号密码或使用 Personal Access Token

## 提交信息模板

```
feat: 女装图片保存助手 v1.1.0

- 基于 astrbot_plugin_stealer 重构
- 移除表情包偷取和自动发送功能
- 新增 SMTP 邮件推送功能
- 新增忽略 GIF 选项
- 完善文档和配置
```

## 遇到问题？

如果遇到任何问题，可以：
1. 检查网络连接
2. 确认 GitHub 账号已登录
3. 确认仓库存在且有权限
4. 查看错误信息并搜索解决方案
