"""
created by Nagaj at 26/05/2021
"""
from mixin import CRUDMixin
from files_operations import Base


class Folder(Base, CRUDMixin):
    def __init__(self, foldername):
        Base.__init__(self, foldername)
        CRUDMixin.__init__(self)
        self.files = self.items

    def __str__(self):
        return self.name

    def __setattr__(self, key, value):
        if key == "name":
            self._validated_name(value)
        super().__setattr__(key, value)


# todo1: follow with islam and devops to fix deployment issues, conf[identity,