import smtplib
import asyncio
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from astrbot.api import logger


class SMTPService:
    """SMTP 邮件服务类，负责发送邮件。"""

    def __init__(self, plugin_instance: Any):
        """初始化 SMTP 服务。

        Args:
            plugin_instance: Main 实例，用于访问插件配置
        """
        self.plugin = plugin_instance
        self.smtp_config = plugin_instance.plugin_config.smtp

    def validate_config(self) -> tuple[bool, str]:
        """验证 SMTP 配置是否正确。

        Returns:
            tuple[bool, str]: (是否有效，错误信息)
        """
        if not self.smtp_config.enabled:
            return False, "邮件推送未启用"

        if not self.smtp_config.smtp_server:
            return False, "未配置 SMTP 服务器"

        if not self.smtp_config.sender_email:
            return False, "未配置发件人邮箱"

        if not self.smtp_config.sender_password:
            return False, "未配置邮箱授权码"

        if not self.smtp_config.receiver_email:
            return False, "未配置收件人邮箱"

        # 验证邮箱格式
        if "@" not in self.smtp_config.sender_email:
            return False, "发件人邮箱格式不正确"

        if "@" not in self.smtp_config.receiver_email:
            return False, "收件人邮箱格式不正确"

        return True, ""

    async def send_email(self, subject: str, content: str, html: bool = False) -> tuple[bool, str]:
        """发送邮件。

        Args:
            subject: 邮件主题
            content: 邮件内容
            html: 是否为 HTML 格式

        Returns:
            tuple[bool, str]: (是否成功，错误信息)
        """
        # 验证配置
        is_valid, error_msg = self.validate_config()
        if not is_valid:
            logger.error(f"[SMTP] 配置验证失败：{error_msg}")
            return False, error_msg

        try:
            # 创建邮件
            msg = MIMEMultipart()
            msg['From'] = self.smtp_config.sender_email
            msg['To'] = self.smtp_config.receiver_email
            msg['Subject'] = subject

            # 添加邮件内容
            content_type = 'html' if html else 'plain'
            msg.attach(MIMEText(content, content_type, 'utf-8'))

            # 连接 SMTP 服务器并发送邮件
            def _send():
                server = None
                try:
                    if self.smtp_config.use_tls:
                        # 使用 TLS 加密
                        server = smtplib.SMTP(self.smtp_config.smtp_server, self.smtp_config.smtp_port, timeout=30)
                        server.starttls()
                    else:
                        # 不使用加密
                        server = smtplib.SMTP(self.smtp_config.smtp_server, self.smtp_config.smtp_port, timeout=30)

                    # 登录
                    server.login(self.smtp_config.sender_email, self.smtp_config.sender_password)

                    # 发送邮件
                    server.sendmail(
                        self.smtp_config.sender_email,
                        self.smtp_config.receiver_email,
                        msg.as_string()
                    )
                finally:
                    # 确保连接被关闭
                    if server:
                        try:
                            server.quit()
                        except Exception:
                            pass

            # 在线程池中执行，避免阻塞事件循环
            await asyncio.to_thread(_send)

            logger.info(f"[SMTP] 邮件发送成功：{self.smtp_config.receiver_email}")
            return True, ""

        except smtplib.SMTPAuthenticationError as e:
            error_msg = f"SMTP 认证失败：{str(e)}"
            logger.error(f"[SMTP] {error_msg}")
            return False, error_msg

        except smtplib.SMTPConnectError as e:
            error_msg = f"SMTP 连接失败：{str(e)}"
            logger.error(f"[SMTP] {error_msg}")
            return False, error_msg

        except smtplib.SMTPException as e:
            error_msg = f"SMTP 错误：{str(e)}"
            logger.error(f"[SMTP] {error_msg}")
            return False, error_msg

        except Exception as e:
            error_msg = f"发送邮件失败：{str(e)}"
            logger.error(f"[SMTP] {error_msg}", exc_info=True)
            return False, error_msg

    async def send_test_email(self) -> tuple[bool, str]:
        """发送测试邮件。

        Returns:
            tuple[bool, str]: (是否成功，错误信息)
        """
        subject = "🌟 女装图片保存助手 - 测试邮件"
        content = f"""
<html>
<body>
    <h2>✅ 测试邮件发送成功！</h2>
    <p>恭喜！您的 SMTP 配置已正确设置。</p>
    <p>以下是您的配置信息：</p>
    <ul>
        <li><strong>SMTP 服务器：</strong>{self.smtp_config.smtp_server}:{self.smtp_config.smtp_port}</li>
        <li><strong>发件人：</strong>{self.smtp_config.sender_email}</li>
        <li><strong>收件人：</strong>{self.smtp_config.receiver_email}</li>
        <li><strong>加密方式：</strong>{"TLS 加密" if self.smtp_config.use_tls else "无加密"}</li>
        <li><strong>发送时间：</strong>{self.smtp_config.send_time}</li>
    </ul>
    <p>系统将在每天定时发送女装图片统计日报。</p>
    <hr>
    <p style="color: #666; font-size: 12px;">此邮件由 AstrBot 女装图片保存助手自动发送</p>
</body>
</html>
"""
        return await self.send_email(subject, content, html=True)
