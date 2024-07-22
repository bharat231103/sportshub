"""
URL configuration for sportshub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sports import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/', views.register , name = 'register'),
    path('login/', views.login),
    path('logout/', views.logout),
    #path('fees/', views.fees),
    # path('cric/', views.cricket , name = 'cricket'),
    path('gym/', views.gym , name = 'gym'),
    # path('kab/', views.kabaddi , name = 'kabaddi'),
    # path('kho/', views.kho , name = 'kho'),
    # path('basketball/', views.basketball , name= 'basketball'),
    path('lib/', views.library , name = 'library'),
    # path('tab/', views.table_tennis , name= 'table_tennis'),
    # path('tennis/', views.tennis , name = 'tennis'),
    # path('turf/', views.turf , name= 'turf'),
    path('medi/', views.medical , name= 'medical'),
    # path('foot/', views.football , name= 'football'),
    # path('chess/', views.chess , name= 'chess'), 
    # path('carr/', views.carrom , name= 'carrom'),
    path('add/', views.add , name = 'add'),
    path('feed/', views.feedback , name = 'feedback'),
    path('coach/', views.coach, name = 'coach'),
    path('spo/', views.sports , name = 'sports'),
]