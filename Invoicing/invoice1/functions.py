import logging
from django.core.mail import EmailMessage
from django.conf import settings
from smtplib import SMTPException

logger = logging.getLogger(__name__)

def emailInvoiceClient(to_email, from_client, filepath):
    try:
        from_email = settings.EMAIL_HOST_USER
        subject = '[PARAS] Invoice Notification'
        body = f"""
        Good day,

        Please find attached invoice from {from_client} for your immediate attention.

        regards,
        Invoice Generator.
        Paras Sonare
        """
        
        message = EmailMessage(subject, body, from_email, [to_email])
        message.attach_file(filepath)
        message.send()
        logger.info("Email sent successfully to %s", to_email)
    except SMTPException as e:
        logger.error("Failed to send email: %s", e)
        raise
    except Exception as e:
        logger.error("An unexpected error occurred: %s", e)
        raise
