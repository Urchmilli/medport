from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('blog', views.blog, name='blog'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('appointment_successful', views.appointment_submitted, name='appointment_submitted'),
    path('signout', views.signout, name="signout"),
    # path('signupSuccessful', views.signupSuccessful, name='signupSuccessful'),
]
