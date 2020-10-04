from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def SendEmailToUsers(context_dict, user):

    if settings.DEBUG == True:
        context_dict['host'] = '127.0.0.1:8000'
    else:
        context_dict['host'] = "localhost"
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
            ['skakrecha@codal.com', ])
        email.content_subtype = "html"
        email.send()
