from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^card/(?P<card_id>[0-9a-fA-F]+)', 'felicasite.simpleserver.views.card'),
)
