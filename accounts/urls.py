from django.conf.urls import url

from django.urls import path
from . import views
from django.conf.urls.static import  static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('signup/',views.signup_view,name="signup_view"),
   
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()