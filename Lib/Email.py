import smtplib
import ssl


class Email:

    SmtpServer = "smtp.gmail.com"
    SenderEmail = "ap.4002.group2@gmail.com"
    SenderPassword = "xfkrlkgvdwrejrfx"
    Port = 465


    @staticmethod
    def Send(receiverEmail : str, message : str):
        """send email"""
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(Email.SmtpServer, Email.Port, context = context) as server:
                server.login(Email.SenderEmail, Email.SenderPassword)
                server.sendmail(Email.SenderEmail, receiverEmail, message)

        except Exception as e:
            print(str(e))
