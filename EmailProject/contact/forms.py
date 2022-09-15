from django import forms
from django.conf import settings
from django.core.mail import message, send_mail
from django.forms.fields import EmailField


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    inquiry = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)

    def get_info(self):
        cl_data = super().clean()

        name = cl_data.get("name").strip()
        from_email = cl_data.get("email")
        subject = cl_data.get("inquiry")

        msg = f"{name} with email {from_email} said:"
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get("message")

        return subject, msg

    def send(self):
        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS],
        )
