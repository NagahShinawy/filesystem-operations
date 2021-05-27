"""
created by Nagaj at 26/05/2021
"""
from abc import ABC


def breakline(char="#", times=50):
    print(char * times)


class CRUDMixin(ABC):
    """
    act like interface
    """

    def __init__(self, *args, **kwargs):
        self.items = []

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def list(self):
        for item in self.items:
            print(item)

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, item):
        return self.items[item]
