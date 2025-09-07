import uuid
from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Sepatu Bola'),
        ('jersey', 'Jersey'),
        ('ball', 'Bola'),
        ('equipment', 'Peralatan Latihan'),
        ('accessories', 'Aksesoris'),
        ('other', 'Lainnya'),
    ]

    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    # Tambahan fitur
    item_views = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)
    stock = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - Rp{self.price:,}"
    
    @property
    def is_popular(self):
        return self.item_views > 5

    def increment_views(self):
        self.item_views += 1
        self.save()