from django.urls import path

from authors.views.single_author import SingleAuthorView


urlpatterns = [
    path('<str:author>/', SingleAuthorView.as_view(), name='single-author'),
]
