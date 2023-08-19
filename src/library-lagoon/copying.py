import copy
from typing import *


class TestObject(object):
    member: object

    def __init__(self, member: object) -> None:
        self.member = member

    def __copy__(self) -> Self:

        return type(self)(self.member)


class BadImplementation(TestObject):
    def __deepcopy__(self, memodict: dict[int, object] = {}) -> Self:
        """

        This implementation of __deepcopy__() can`t deal with self-referential objects.
        
        """
        new: Self = type(self)(member=copy.deepcopy(self.member, memo=memodict))
        memodict[id(self)] = new
        return new


class GoodImplementation(TestObject):
    def __deepcopy__(self, memodict: dict[int, object] = {}) -> Self:
        new: Self = object.__new__(type(self))
        memodict[id(self)] = new
        new.member = copy.deepcopy(self.member, memo=memodict)
        return new

if __name__ == "__main__":
    simple = BadImplementation(["member objects will be deepcopied too"])
    self_referential_bad = BadImplementation(None)
    self_referential_bad.member = {"": self_referential_bad}
