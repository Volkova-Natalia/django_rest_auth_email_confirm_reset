from .tokens import user_email_confirmation_token, user_email_password_reset_token
from ..settings import app_name

from django.core.mail import EmailMessage

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings


def send_user_email_confirmation(*, request, user):
    current_site = get_current_site(request)
    subject = 'Confirm your email'
    message = render_to_string(app_name + r'/user_email_confirmation.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': user_email_confirmation_token.make_token(user),
    })
    email = EmailMessage(subject, message, to=[user.email], from_email=settings.EMAIL_HOST_USER)
    email.send()


def send_user_email_password_reset_confirmation(*, request, user):
    current_site = get_current_site(request)
    subject = 'Confirm your password reset'
    message = render_to_string(app_name + r'/user_email_password_reset_confirmation.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': user_email_password_reset_token.make_token(user),
    })
    email = EmailMessage(subject, message, to=[user.email], from_email=settings.EMAIL_HOST_USER)
    email.send()
