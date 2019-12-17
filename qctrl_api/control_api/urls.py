from django.urls import path, include, re_path
from .views import ControlCreateView
from .views import ControlRetrieveUpdateDeleteView


urlpatterns = [
    re_path(r'^control/$', ControlCreateView.as_view(), name="control_create"),
    re_path(r'^control/(?P<pk>\d+)/$', ControlRetrieveUpdateDeleteView.as_view(), name="control_rud"),
]

