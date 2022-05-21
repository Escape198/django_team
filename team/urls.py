"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static  import static
from django.conf import settings

from users import views

#from rest_framework_swagger.views import get_swagger_view


#schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path('', views.all_users, name='home'),
    path('admin/', admin.site.urls),
    #path('api/', schema_view),
    path('basic_skill/', views.basic_skill_view, name='basic_skill'),
    path('profile/', views.profile_view, name='profile'),
    path('sign_in/', views.sign_in_view, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_out/', views.sign_out_view, name='sign_out'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
