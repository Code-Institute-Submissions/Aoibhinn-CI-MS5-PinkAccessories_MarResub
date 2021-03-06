# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.utils.translation import gettext_lazy as _


# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Category(models.Model):
    """
    A class for the category model
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=254
    )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the category friendly name string
        Args:
            self (object): self.
        Returns:
            The category friendly name string
        """
        return self.friendly_name


class Product(models.Model):
    """
    A class for the product model
    """
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=254
    )
    description = models.TextField(
    )
    has_sizes = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )
    colour = models.CharField(
        max_length=254
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    pre_sale_price = models.DecimalField(
        verbose_name=_('Pre sale price'),
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )
    image = models.ImageField(
        null=True,
        blank=True
    )

    def __str__(self):
        """
        Returns the product name
        Args:
            self (object): self.
        Returns:
            The product name string
        """
        return self.name
