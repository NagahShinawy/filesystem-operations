"""
created by Nagaj at 26/05/2021
"""
from mixin import CRUDMixin


class Folder(CRUDMixin):
    def __init__(self, foldername):
        super().__init__()
        self.folder_name = foldername
        self.files = self.items

    def __str__(self):
        return self.folder_name
