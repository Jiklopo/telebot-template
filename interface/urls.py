from django.urls import path
from interface.views import *

urlpatterns = [
    path('controls', ControlView.as_view()),
    path('', IndexView.as_view())
]
