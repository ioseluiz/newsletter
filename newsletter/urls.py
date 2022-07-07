from django.urls import path 
from .views import newsletter_signup, newsletter_unsubcribe

app_name = "newsletter"

urlpatterns = [
    path('entrenamiento/', newsletter_signup, name="optin"),
    path('unsubscribe/', newsletter_unsubscribe, name="unsubscribe"),

]