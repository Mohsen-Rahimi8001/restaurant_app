import smtplib
import ssl


class Email:

    SmtpServer = "smtp.gmail.com"
    SenderEmail = "ap.4002.final.project.group2@gmail.com"
    SenderPassword = "aA!123456789"
    Port = 456


    @staticmethod
    def Send(receiverEmail : str, message : str):
        """send email"""
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(Email.SmtpServer, Email.Port, context = context) as server:
                server.login(Email.SenderEmail, Email.SenderPassword)
                server.sendmail(Email.SenderEmail, receiverEmail, message)

        except Exception:
            pass