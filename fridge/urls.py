from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$',views.watch_stock,name='stock'),
    url(r'^shoppingcart/add/(?P<item_id>\d+)/$',views.add,name='add_to_cart'),
    url(r'^cart/$',views.show,name='cart'),
    url(r'^cart/automate/$',views.showcheck,name='automate'),
    url(r'^orders/$',views.adm,name='admin_orders'),

]
# urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)