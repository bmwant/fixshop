from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uawebteam14.views.home', name='home'),
    url(r'^cart/$', 'fixshop.views.cart', name='cart'),
    url(r'^catalog', 'fixshop.views.grid', name='grid'),
    url(r'^$', 'fixshop.views.index', name='index'),

    url(r'^item/(?P<item_id>[0-9]+)', 'fixshop.views.item_view', name='item_view'),
    url(r'^item/add/(?P<item_id>[0-9]+)', 'fixshop.views.add_to_cart', name='item_to_cart'),
    url(r'^cart/clear/$', 'fixshop.views.clear_cart', name='clear_cart'),
    url(r'^cart/checkout/$', 'fixshop.views.checkout', name='checkout'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
