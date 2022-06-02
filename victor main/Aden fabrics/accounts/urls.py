from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings
from .import views
urlpatterns = [
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('login/', views.login,name='login'),
    path('dashbord/', views.dashboard,name='dashboard'),
    path('logout/', views.logoutUser, name='logout'),
    path('employee/', views.employee, name='employee'),
    path('editcustomer/<str:pk>/', views.editcustomer, name="editcustomer"),
    path('customer/', views.customer, name='customer'),
    path('addreport/', views.addreport, name='addreport'),
    path('report/', views.report, name='report'),
    path('editcustomer/<str:pk>/', views.editcustomer, name="editcustomer"),
    path('deletecustomer/<str:pk>/', views.deletecustomer, name="deletecustomer"),
    path('editreport/<str:pk>/', views.editreport, name="editreport"),
    path('deletereport/<str:pk>/', views.deletereport, name="deletereport"),
    path('track/', views.track,name="track"),
    path('search/', views.search,name="search"),
    path('addinventory/', views.addinventory, name='addinventory'),
    path('inventory/', views.inventory, name='inventory'),
    path('editinventory/<str:pk>/', views.editinventory, name="editinventory"),
    path('deleteinventory/<str:pk>/', views.deleteinventory, name="deleteinventory"),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

