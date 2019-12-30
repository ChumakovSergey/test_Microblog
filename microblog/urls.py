from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import ApiView,PageView

urlpatterns = [
    path('',PageView.as_view()),
    path('messages/',ApiView.as_view())
]