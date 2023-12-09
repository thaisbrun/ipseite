
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from djangoProject import settings
from ipseite.views import add_to_cart, event_detail
from accounts.views import signup, logout_user, login_user, my_account, delete_user

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('signup/', signup, name="signup"),
                  path('login/', login_user, name="login"),
                  path('logout/', logout_user, name="logout"),
                  path('my_account/', my_account, name="my_account"),
                  path('delete_user',delete_user, name="delete_user"),
                  path('', include('ipseite.urls')),
                  path('event/<str:slug>', event_detail, name="event_detail"),
                  path('ticket/<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
