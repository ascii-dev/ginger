from django.urls import path

from favorites.views.all_favorites import AllFavoritesView
from favorites.views.create_favorite import CreateFavoriteView


urlpatterns = [
    path('<str:article_id>/', CreateFavoriteView.as_view(), name='create_favorite'),
    path('', AllFavoritesView.as_view(), name='all_favorites'),
]
