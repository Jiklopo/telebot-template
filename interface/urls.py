from django.urls import path
from interface.views import *

urlpatterns = [
    path('', ControlView.as_view())
]
