"""fyproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from imageprocessor import views
from homepage import views as v1
from django.conf.urls.static import  static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name="imageprocessor"
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',v1.home,name='home'),
    path('accounts/', include('accounts.urls')),
    path('check/',views.home,name='home'),
    path('check/predictimage',views.predictimage,name='predictimage')
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
