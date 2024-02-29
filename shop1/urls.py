
from django.contrib import admin
from django.urls import path,include
from products_app.views import *
from django.conf import settings
from django.conf.urls.static import static
from azbankgateways.urls import az_bank_gateways_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('shop/', shop,name="shop"),
    path('shop/category/<str:category>/',shop, name='shop2'),
    
    path('contact/', contact,name="contact"),
    path('about/', about,name="about"),
    path('login/', log,name="login"),
    path('sign/', sign,name="sign-up"),
    path('cart/', cart,name="cart"),
    path('addtocart/<adad>', addtocart,name="addcart"),
    path('delcart/<adad>', delcart,name="delcart"),
    path('edqnt/<adad>', edqnt,name="edqnt"),
    path('logout/', lout,name="lout"),
    path('error/', error,name="error"),
    path('success/', sc,name="sc"),
    path('successful/', successful,name="s"),
    path('unsuccessful/', unsuccessful,name=" uns"),
    path('pardahkt/', pardakht,name="pardakht"),
    path('bankgateways/', az_bank_gateways_urls()),
    path('callback-gateway/', callback_gateway_view),
    path('api/', include('product_manager.urls')),
    
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
