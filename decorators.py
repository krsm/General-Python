# -*- coding: utf-8 -*-
"""
simple study of decorators

"""


# First example
def outerfunction(outer):
    print("test")
    def innerfunction(inner):
        return outer(inner) + 1
    return innerfunction


@outerfunction
def addone(x):
    return x + 1


# Second Example
def wrapfunction(fn):
    print("Executing wrapfunction")

    def wrappedfunction():
        print("Calling %s inside wrappedfunction" % fn.__name__)
        # calling fn
        fn()
        print("Executed %s inside wrappedfunction" % fn.__name__)
    return wrappedfunction


@wrapfunction
def tobedecorated():
    print("Executing tobedecorated function")

if __name__ == "__main__":

    # pass
    # first example
    # print(addone(5))
    # second example
    tobedecorated()
