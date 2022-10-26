from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expenses_tracker_stan.web.validators import validate_name_consist_letters_only, ImageMaxSizeLimit


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 15
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15
    LAST_NAME_MIN_LEN = 2
    BUDGET_MIN_VALUE = 0
    IMAGE_MAX_SIZE_LIMIT = 5

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_name_consist_letters_only
        ]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_name_consist_letters_only,
        ]
    )

    budget = models.FloatField(
        default=0,
        validators=[
            MinValueValidator(BUDGET_MIN_VALUE),
        ]
    )

    profile_image = models.ImageField(
        upload_to='profile_image',  # this is optional
        null=True,
        blank=True,
        validators=[
            ImageMaxSizeLimit(IMAGE_MAX_SIZE_LIMIT, )
        ]
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Expense(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(max_length=TITLE_MAX_LEN,)

    expense_image = models.URLField()

    description = models.TextField(
        blank=True,
        null=True,
    )
    price = models.FloatField()
