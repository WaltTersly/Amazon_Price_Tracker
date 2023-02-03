import smtplib

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "terslyparadise@gmail.com"
MY_PASSWORD = "ndkabesfainbdzxo"

class NotificationsManager:
    
    def send_email(self, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr= MY_EMAIL, 
                to_addrs= MY_EMAIL,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n".encode()
            )

