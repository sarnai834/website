from django.urls import path
from app import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('',views.index,name="index"),
    path('home/', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/angilalB/', views.angilalB, name='angilalB'),
    path('home/C/', views.angilalC, name='angilalC'),  
    path('home/D/', views.angilalD, name='angilalD'),
    path('home/E/', views.angilalE, name='angilalE'),
    path('home/uhat/', views.uhat, name='uhat'),
    path('home/home/uhzt/', views.uhzt, name='uhzt'),
    path('home/home/aa/', views.aa, name='aa'),
    path('home/home/jt/', views.jt, name='jt'),
    path('insert',views.insertData,name="insertData"),
    path('update/<id>',views.updateData,name="updateData"),
    path('delete/<id>',views.deleteData,name="deleteData"),
]