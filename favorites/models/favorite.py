from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Favorite(models.Model):
    """
    Model representing user's favorite articles
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article_id = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} + {self.article_id}'

    class Meta:
        """
        Meta class.
        """

        verbose_name_plural = "Favorites"
        db_table = "favorites"
