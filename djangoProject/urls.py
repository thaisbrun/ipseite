
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from djangoProject import settings
from ipseite.views import artist_detail
from accounts.views import signup

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('signup/', signup, name="signup"),
                  path('', include('ipseite.urls')),
                  path('artist/<str:slug>', artist_detail, name="artist"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
