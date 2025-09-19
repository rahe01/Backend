from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

import threading

class SendEmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)


    def run(self):
        self.email.send()


def send_activation_email(recipent_email, activation_url):
    subject = "Activate Your Account on " + settings.SITE_NAME
    from_email = 'no-reply@mailtrap.io'  # <-- eta use koren
    to_email = [recipent_email]

    # load html template
    html_content = render_to_string('account/activation_email.html', {'activation_url': activation_url, 'site_name': settings.SITE_NAME})

    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, "text/html")
    SendEmailThread(email).start()