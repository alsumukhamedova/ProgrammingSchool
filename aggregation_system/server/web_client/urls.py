from django.urls import path

# from .views import ResultSendView, CheckSendView
from .views import send_result, check_send


"""Links in web_client app"""

urlpatterns = [
    path('check/', check_send),
    path('result/', send_result)
]