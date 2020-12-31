from django.urls import path

from articles.views.all_articles import AllArticlesView


urlpatterns = [
    path('', AllArticlesView.as_view(), name='all-articles'),
]
