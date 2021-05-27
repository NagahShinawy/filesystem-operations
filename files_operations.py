"""
created by Nagaj at 26/05/2021
"""
from abc import ABC, abstractmethod
from exceptions import InvalidCharForName, InvalidExtension


class Base:
    BAD_CHARS = r"\/:?|*<>"

    def __init__(self, name, *args, **kwargs):
        self.name = name

    @classmethod
    def _validated_name(cls, value):
        for char in value:
            if char in cls.BAD_CHARS:
                raise InvalidCharForName(
                    InvalidCharForName.message.format(
                        classname=cls.__name__, value=value, char=char
                    )
                )


class File(ABC, Base):
    number_of_files = 0
    EXTENSIONS = [".xlsx", ".docx", ".png", ".jpg", ".mp3", ".mp4", ".pdf", ".exe"]

    def __init__(self, fname, extension):
        super().__init__(fname)
        self.extension = extension
        File.number_of_files += 1

    def __str__(self):
        return self.name + self.extension

    def __setattr__(self, attribute, value):
        if attribute == "extension":
            self.__validated_extension(value)
        if attribute == "name":
            self._validated_name(value)
        super().__setattr__(attribute, value)

    @classmethod
    def __validated_extension(cls, value):
        if value not in cls.EXTENSIONS:
            raise InvalidExtension(
                InvalidExtension.message.format(value=value, extensions=cls.EXTENSIONS)
            )

    @abstractmethod
    def show_fileinfo(self):
        print(f"File Name is: {self.name}")
        print(f"File Extension is: {self.extension}")


class Word(File):
    def __init__(self, fname, extension, released):
        self.released = released
        super().__init__(fname, extension)

    def show_fileinfo(self):
        super().show_fileinfo()
        print(f"App '{self.__class__}' Released: {self.released}")


class Excel(File):
    def __init__(self, filename, file_extension, usages):
        super().__init__(filename, file_extension)
        self.usg = usages

    def show_fileinfo(self):
        super().show_fileinfo()
        print(f"We are using excel for: {self.usg}")
