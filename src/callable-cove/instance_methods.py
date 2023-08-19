from types import MethodType, FunctionType


class TestClass:
    def method(self) -> None:
        pass


class MethodImplementation:  # TODO
    pass


if __name__ == "__main__":
    a = TestClass()

    assert a.method != TestClass.method  # a.method is a MethodType object, and TestClass.method is a function
    assert isinstance(a.method, MethodType)  # a.method is an instance of types.MethodType
    assert isinstance(TestClass.method, FunctionType)  # TestClass.method is an instance of FunctionType
    assert a.method is not a.method  # function`s __get__ recalculates it every time, so these two methods are equal, but not identical.

    assert a.method.__func__ is TestClass.method  # the __func__ attribute stores the function
    assert a.method.__self__ is a  # the __self__ attribute stores the instance
    assert a.method == MethodType(TestClass.method, a)  # an eqvivalent MethodType object can be created using types.MethodType

    print("assertions succeeded")

    """
    `a.method` is not the class attribute `method`, because functions are descriptors, and their __get__ (see feature-reef) method returns a MethodType object.
    Every MethodType object stores the function object which created it, in it`s __func__ attribute.
    They also store the object which should be passed to the function along with the other parameters.
    """
