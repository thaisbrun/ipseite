import debug_toolbar.urls
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from djangoProject import settings
from ipseite.views import add_to_cart, event_detail, concerts, festivals, cart, delete_cart, delete_orderFromCart
from accounts.views import signup, logout_user, login_user, my_account, delete_user
from django.urls import path, include
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('signup/', signup, name="signup"),
                  path('login/', login_user, name="login"),
                  path('logout/', logout_user, name="logout"),
                  path('my_account/', my_account, name="my_account"),
                  path('delete_user',delete_user, name="delete_user"),
                  path('concerts', concerts, name="concerts"),
                  path('festivals', festivals, name="festivals"),
                  path('', include('ipseite.urls')),
                  path('', include('payments.urls')),  # new
                  path('event/<str:slug>', event_detail, name="event_detail"),
                  path('cart/', cart, name="cart"),
                  path('cart/delete', delete_cart, name="delete_cart"),
                  path('cart/delete_orderFromCart/<str:id>', delete_orderFromCart, name="delete_orderFromCart"),
                  path('__debug__/', include(debug_toolbar.urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
