"""
created by Nagaj at 26/05/2021
"""
from abc import ABC, abstractmethod


class File(ABC):
    number_of_files = 0

    def __init__(self, fname, extension):
        self.file_name = fname
        self.extension = extension
        File.number_of_files += 1

    def __str__(self):
        return self.file_name + self.extension

    @abstractmethod
    def show_fileinfo(self):
        print(f"File Name is: {self.file_name}")
        print(f"File Extension is: {self.extension}")


class Word(File):
    def __init__(self, fname, extension, released):
        self.released = released  #
        super().__init__(fname, extension)

    def show_fileinfo(self):
        super().show_fileinfo()
        print(f"App '{self.__class__}' Released: { self.released}")


class Excel(File):
    def __init__(self, filename, file_extension, usages):
        super().__init__(filename, file_extension)
        self.usg = usages

    def show_fileinfo(self):
        super().show_fileinfo()
        print(f"We are using excel for: {self.usg}")
