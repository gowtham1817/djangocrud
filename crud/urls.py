from django.urls import path
from . import views 
urlpatterns = [
   path('register/',views.register,name='register'),
   path('login/',views.loginForm,name='loginForm'),
   path('logout/',views.logoutForm,name='logoutForm'),
   path('show',views.show,name='show'),
   path('form',views.form,name='form'),
   path('delete/<int:id>',views.deleteForm,name='deleteForm')

]