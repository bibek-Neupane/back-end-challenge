from django.urls import path, include
from .views import ControlCreateView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = {
    path('control/', ControlCreateView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)