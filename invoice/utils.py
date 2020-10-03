from django.core.mail import send_mail
from django.conf import settings


def SendEmailToUsers(context_dict):
    html_body = render_to_string(
        'email_template/invoice/daily_invoice_update.html',
        context_dict
    )

    user = context_dict.get('manager')

    # rendering the email_template
    if user:
        email = EmailMessage(
            subject, html_body,
            settings.EMAIL_HOST_USER,
            [user,])
        email.content_subtype = "html"
        email.attach(pdf_name, open(
            pdf, "rb").read(), 'application/pdf')

        email.send()
