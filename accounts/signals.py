# accounts/signals.py
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    print("\n\n======= Password Reset Token Created =======")
    print(f"User: {reset_password_token.user}")
    print(f"Token: {reset_password_token.key}")
    print(f"Reset Link: http://localhost:3000/reset-password?token={reset_password_token.key}")
    print("============================================\n\n")

    send_mail(
        subject="Password Reset for CoBright",
        message=f"Use this link to reset your password: http://localhost:3000/reset-password?token={reset_password_token.key}",
        from_email="noreply@cobright.com",
        recipient_list=[reset_password_token.user.email],
        fail_silently=False,
    )
