from django import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from core.views import CustomLoginView, cart, product_list, register, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', cart, name='cart'), 
    path('',include('core.urls')),
    path('accounts/',include('accounts.urls')),
    path('products/', product_list, name='products'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/register/', register, name='register'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)