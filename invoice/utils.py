from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def SendEmailToUsers(context_dict, user):
    html_body = render_to_string(
        'email_template/invoice/daily_invoice_update.html',
        context_dict
    )
    subject = "Summary of yesterday's Invoices."
    # rendering the email_template
    if user:
        email = EmailMessage(
            subject, html_body,
            settings.EMAIL_HOST_USER,
            [user, ])
        email.content_subtype = "html"
        email.send()
