from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def products(self):
        return [products.title for products in Product.objects.filter(category_id=self.id)]

    def products_count(self):
        return Product.objects.filter(category_id=self.id).count()


class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def rating(self):
        if not self.reviews.count():
            return 0
        return sum([rating.stars for rating in self.reviews.all()]) / self.reviews.count()


STARS = (
    (1, '*'),
    (2, '* ' * 2),
    (3, '* ' * 3),
    (4, '* ' * 4),
    (5, '* ' * 5)
)


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(default=5, choices=STARS)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.product.title
