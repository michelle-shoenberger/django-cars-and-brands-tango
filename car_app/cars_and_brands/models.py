from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=64)
    # cars - return a list of the cars associated with this brand id

    def __str__(self):
        return f'Brand {self.name}, {self.id}'

class Car(models.Model):
    name = models.CharField(max_length=64)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return f'{self.brand} {self.name}, {self.id}'










# class Brand(models.Model):
#     name = models.CharField(max_length=64)
#     # cars - many to one

#     def __str__(self):
#         return f'Brand {self.name}, {self.id}'

# class Car(models.Model):
#     name = models.CharField(max_length=64)
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')

#     def __str__(self):
#         return f'{self.brand} {self.name}, {self.id}'