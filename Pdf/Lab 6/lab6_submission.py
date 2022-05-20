my_name = "Furkan Cayci"
my_id = "12345678"
my_email = "furkancayci@gtu.edu.tr"

def problem0():
    '''Doctests
    >>> A = problem0()
    >>> ainst = A(3)
    >>> ainst.get_value()
    3
    >>> A = problem0()
    >>> ainst = A(1)
    >>> ainst.get_value()
    1
    >>> A = problem0()
    >>> ainst = A(-4)
    >>> ainst.get_value()
    -4
    >>> ainst.set_value(5)
    >>> ainst.get_value()
    5
    '''

    # p0 class is defined inside the function
    # if name is given in the problem, use that name as the class name.
    # If name is NOT given in the problem, pick a name yourself.
    # For example, you can just use p# structure.
    class p0:

        # These are class members. Make sure your indentation is correct.
        def __init__(self, x):
            self.a = x

        def get_value(self):
            return self.a

        def set_value(self, x):
            self.a = x

    # Make sure to always return the class
    # Otherwise we will not see it (i.e. NoneType),
    # and your problem will be marked 0.
    return p0


if __name__ == "__main__":

    # You can do checks like this. We will do this way.
    A = problem0()
    # A is the class name, and it is not the instance.
    # We now create an intance using A
    ainst = A(4)
    # Now that we have the instance, we can call the methods.
    assert 4 == ainst.get_value()
    ainst.set_value(5)
    assert 5 == ainst.get_value()

    # alternatively, you can set up doctests and run those
    # autocheck with doctest
    import doctest
    doctest.testmod()

    print("Completed all doctests.")

