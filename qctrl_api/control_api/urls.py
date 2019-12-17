from django.urls import path, include, re_path
from .views import ControlCreateView
from .views import ControlRetrieveUpdateDeleteView
from .views import CsvUploadView


urlpatterns = [
    re_path(r'^control/$', ControlCreateView.as_view(), name="control_create"),
    re_path(r'^control/(?P<pk>[0-9]+)/$', ControlRetrieveUpdateDeleteView.as_view(), name="control_rud"),
    re_path(r'^control/(?P<file>[^/]+)$', CsvUploadView.as_view())
]

