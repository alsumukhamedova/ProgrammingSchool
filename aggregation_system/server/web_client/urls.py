from django.urls import path

# from .views import ResultSendView, CheckSendView
from .views import send_result, check_send


"""Links in web_client app"""

urlpatterns = [
    path('check/', send_result),
    path('result/', check_send)
]