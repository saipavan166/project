from django.contrib import admin
from django.urls import path
from django.urls import path
from django.views.generic import TemplateView
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='projecthomepage.html'), name='projecthomepage'),
    path('employerhomepage/', TemplateView.as_view(template_name='employerhomepage.html'), name='employerhomepage'),
    path('jobseekerhomepage/', TemplateView.as_view(template_name='jobseekerhomepage.html'), name='jobseekerhomepage'),
    path ('signup',views.signup, name='signup'),
    path ('signup1',views.signup1, name='signup1'),
    path ('login',views.login, name='login'),
    path ('login1',views.login1, name='login1'),
    path ('logout',views.logout, name='logout'),
]
