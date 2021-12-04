from django.urls import path

from .views import ResultSendView, CheckSendView

"""
    Links in web_client app
"""

urlpatterns = [
    path('results/', ResultSendView.as_view()),
    path('check/', CheckSendView.as_view()),
]