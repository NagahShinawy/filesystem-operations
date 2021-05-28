"""
created by Nagaj at 26/05/2021
"""
from files_operations import Base
from mixin import CRUDMixin


class Folder(Base, CRUDMixin):
    def __init__(self, foldername, sizeondisk=0, created=None, *args, **kwargs):
        Base.__init__(self, foldername, sizeondisk, created, *args, **kwargs)
        CRUDMixin.__init__(self)

    def __str__(self):
        return self.name
