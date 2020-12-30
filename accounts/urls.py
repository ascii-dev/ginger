from django.urls import path

from accounts.views.sign_up import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
