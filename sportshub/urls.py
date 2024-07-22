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
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/', views.register , name = 'register'),
    path('login/', views.login),
    path('logout/', views.logout),
    path('gym/', views.gym , name = 'gym'),
    path('lib/', views.library , name = 'library'),
    path('medi/', views.medical , name= 'medical'),
    path('add/', views.add , name = 'add'),
    path('feed/', views.feedback , name = 'feedback'),
    path('sport/', views.sports , name = 'sports'),
    path('management/', views.management),
    path('profile/', views.profile, name='profile'),
    # path('editprofile/', views.edit_profile ),    
    path('event/', views.event, name = 'event'),
    path('fee/', views.fee , name = "fee"),
    path('plstat/', views.playerstats  ),
    path('plprofile/', views.player_profile  ),
    path('inst/', views.instruction ),
    path('participate/', views.participate ),
    path('previous_event/', views.previous_event ),
    path('remove_participation/', views.remove_participation),
    path('payment_handler/' , views.payment , name= 'paymenthandler'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)