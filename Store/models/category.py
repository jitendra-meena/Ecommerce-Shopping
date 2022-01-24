from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)

    # For get all categories from category model using decorator
    @staticmethod
    def get_all_catagories():
        return Category.objects.all()

    # for show category name.
    def __str__(self):
        return self.name
