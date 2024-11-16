from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    download_link = models.URLField(_('download link'), blank=True)
    purchase_link = models.URLField(_('purchase link'), blank=True)
    rating = models.FloatField(_('rating'), default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    categories = models.ManyToManyField(Category, related_name='games', blank=True)

    def __str__(self):
        return self.title

    def calculate_rating(self):
        reviews = self.review_set.all()
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            self.rating = total_rating / reviews.count()
        else:
            self.rating = 0
        self.save()

class Review(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField(_('rating'), validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(_('comment'), blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')

    def __str__(self):
        return f'Review by {self.user} for {self.game}'