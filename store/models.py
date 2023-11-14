from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    new = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    second_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_image_url(primary_image, fallback_image):
        """
        Retrieves the URL of the specified primary image. If the primary image is not available,
        falls back to the URL of the specified fallback image. If both images are unavailable,
        an empty string is returned.

        Parameters:
        primary_image: The primary image object.
        fallback_image: The fallback image object.

        Returns:
        str: The URL of the primary or fallback image, or an empty string if both are unavailable.
        """

        try:
            url = primary_image.url
        except ValueError:
            try:
                url = fallback_image.url
            except ValueError:
                url = ''
        return url

    @property
    def image_url(self):
        """
        Retrieves the URL of the primary image.

        Returns:
        str: The URL of the primary or fallback image, or an empty string if both are unavailable.
        """

        return self.get_image_url(self.image, self.second_image)

    @property
    def second_image_url(self):
        """
        Retrieves the URL of the secondary image.

        Returns:
        str: The URL of the secondary or fallback image, or an empty string if both are unavailable.
        """

        return self.get_image_url(self.second_image, self.image)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=9, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
