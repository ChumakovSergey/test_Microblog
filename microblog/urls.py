from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import ApiView,PageView

urlpatterns = [
    path('',csrf_exempt(PageView.as_view())),
    path('messages/',csrf_exempt(ApiView.as_view()))
]