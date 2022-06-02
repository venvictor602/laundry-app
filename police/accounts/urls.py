from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('', views.home, name='home'),
    path('jobs/', views.jobs, name='jobs'),
    path('<str:pk_test>/', views.jobdetails,name="jobdetails"),
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)