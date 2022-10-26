from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_name_consist_letters_only(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters.')


@deconstructible
class ImageMaxSizeLimit:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, image):
        filesize = image.file.size
        megabyte_limit = self.max_size
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError(f"Max file size is {self.max_size:.2f} MB")
