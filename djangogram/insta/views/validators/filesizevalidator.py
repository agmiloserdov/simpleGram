from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator(BaseValidator):
    code = "invalid_filesize"
    """Параметр limit_value принимает в качестве значения допустимый размер файла в kB"""
    def __init__(self, message, limit_value=5000):
        super().__init__(limit_value, message)
        self.file_limit_size_bytes = limit_value * 1024
        self.message += f" Вы можете загрузить файл не более {limit_value} килобайт"

    def compare(self, file_size, limit):
        return self.file_limit_size_bytes <= file_size

    def clean(self, file):
        return len(file)
