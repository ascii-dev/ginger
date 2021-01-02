from django.urls import path

from favorites.views.create_favorite import CreateFavoriteView


urlpatterns = [
    path('<str:article_id>/', CreateFavoriteView.as_view(), name='create-favorite'),
]
