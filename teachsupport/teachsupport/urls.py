from django.contrib import admin
from django.urls import path
from tsm.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index, name='index'),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path('admin/', admin.site.urls),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)