from django.conf.urls import url, patterns

from stucampus.magazine.views import magazine_list, display, manage
from stucampus.magazine.views import ModifyView, AddView


urlpatterns = patterns(
    '',
    url(r'^list/(?P<name>.*)/$', magazine_list, name='list'),
    url(r'^display/(?P<id>\d)/$', display, name='display'),

    url(r'^add/$', AddView.as_view(), name='add'),
    url(r'^manage/$', manage, name='manage'),
    url(r'^modify/$',
        ModifyView.as_view(), name='modify'),
)