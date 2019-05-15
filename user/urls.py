from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^stock/setting$',views.settings,name='settings'),
    url(r'^limit/(?P<stock_id>\d+)',views.limiting,name='limit'),
    url(r'^proceed/order/$', views.orders, name='orders'),
    url(r'^orders/supply/$', views.supplier, name='supplier'),
    url(r'^fridge/order/history$', views.order_history, name='order_history'),
    url(r'^fridge/receipt/$', views.receipt, name='receipt'),
    url(r'^orders/order/(?P<item_id>\d+)$', views.selected, name='selected'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
