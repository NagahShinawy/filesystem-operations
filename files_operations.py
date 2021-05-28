"""
created by Nagaj at 26/05/2021
"""
from abc import ABC, abstractmethod

from exceptions import InvalidCharForName, InvalidExtension


class Base:
    BAD_CHARS = r"\/:?|*<>"

    def __init__(self, name, sizeondisk, created=None, *args, **kwargs):
        self.name = name
        self.sizeondisk = sizeondisk
        self.created = created

    @classmethod
    def _validated_name(cls, value):
        for char in value:
            if char in cls.BAD_CHARS:
                raise InvalidCharForName(
                    InvalidCharForName.message.format(
                        classname=cls.__name__, value=value, char=char
                    )
                )

    def __setattr__(self, attribute, value):
        if attribute == "name":
            self._validated_name(value)
        super().__setattr__(attribute, value)


class File(Base, ABC):
    number_of_files = 0
    EXTENSIONS = [".xlsx", ".docx", ".png", ".jpg", ".mp3", ".mp4", ".pdf", ".exe"]

    def __init__(self, fname, extension, sizeondisk=0, created=None, *args, **kwargs):
        super().__init__(fname, sizeondisk, created, *args, **kwargs)
        self.extension = extension
        File.number_of_files += 1

    def __str__(self):
        return self.name + self.extension

    def __setattr__(self, attribute, value):
        if attribute == "extension":
            self.__validated_extension(value)

        super().__setattr__(attribute, value)

    @classmethod
    def __validated_extension(cls, value):
        if value is not None and value not in cls.EXTENSIONS:
            raise InvalidExtension(
                InvalidExtension.message.format(value=value, extensions=cls.EXTENSIONS)
            )

    @abstractmethod
    def show_fileinfo(self):
        print(f"File Name is: {self.name}")
        print(f"File Extension is: {self.extension}")


class Word(File):
    def __init__(self, fname, extension, *args, **kwargs):
        super().__init__(fname, extension, *args, **kwargs)

    def show_fileinfo(self):
        super().show_fileinfo()
        print(f"App '{self.__class__}' Released: {self.created}")


class Excel(File):
    def __init__(self, filename, file_extension, usages, *args, **kwargs):
        super().__init__(filename, file_extension, *args, **kwargs)
        self.usg = usages

    def show_fileinfo(self):
        super().show_fileinfo()
        print(f"We are using excel for: {self.usg}")
