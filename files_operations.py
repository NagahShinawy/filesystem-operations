"""
created by Nagaj at 26/05/2021
"""
from abc import ABC, abstractmethod


class File(ABC):
    number_of_files = 0
    EXTENSIONS = [".xlsx", ".docx", ".png", ".jpg", ".mp3", ".mp4", ".pdf", ".exe"]
    BAD_CHARS = r"\/:?|*<>"

    def __init__(self, fname, extension):
        self.filename = fname
        self.extension = extension
        File.number_of_files += 1

    def __str__(self):
        return self.filename + self.extension

    def __getattribute__(self, attr):
        if attr == "filename":
            return super().__getattribute__("filename")
        return super().__getattribute__(attr)

    def __setattr__(self, key, value):
        if key == "extension":
            self.__validated_extension(value)
        if key == "filename":
            self.__validated_filename(value)
        super().__setattr__(key, value)

    @classmethod
    def __validated_extension(cls, value):
        if value not in cls.EXTENSIONS:
            raise ValueError(f"invalid extension '{value}'!")

    @classmethod
    def __validated_filename(cls, value):
        for char in value:
            if char in cls.BAD_CHARS:
                raise ValueError(f"invalid filename <{value}>. it contains <{char}>")

    @abstractmethod
    def show_fileinfo(self):
        print(f"File Name is: {self.filename}")
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
