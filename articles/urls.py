from django.urls import path

from articles.views.all_articles import AllArticlesView
from articles.views.single_article import ArticleView


urlpatterns = [
    path('', AllArticlesView.as_view(), name='all-articles'),
    path('articles/<str:article_id>/', ArticleView.as_view(), name='single-article'),
]
