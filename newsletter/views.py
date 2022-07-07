from django.shortcuts import render
from newsletters.models import NewsletterUser
from django.core.checks import messages
from .forms import NewsletterUserSignUpForm
from django.conf import settings 
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage

# Create your views here.
def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.object.filter(email=instance.email).exists():
            messages.warning(request, 'Email alredy exists.')

        else:
            instance.save()
            messages.success(request, 'Le hemos enviado un correo')
            # Correo electronico
            subject="Libro de Fotografia"
            from_email=settings.EMAIL_HOST_USER
            to_email=[instance.email]

            html_template = 'newsletter/email_templates/welcome.html'
            html_message = render_to_string(html_template)
            message=EmailMessage(subject, html_message,from_email,to_email)
            message.content_subtype='html'
            message.send()

    context={
        'form': form,

    }
    return render(request, 'start-here.html', context)

def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)
    