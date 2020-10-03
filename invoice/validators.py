import os
from django.core.exceptions import ValidationError


def validate_file_attachment(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    max_size = 2097152
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

    if value.size > max_size:
        raise ValidationError("Please keep filesize under {}".format(max_size))
