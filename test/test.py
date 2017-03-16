class hello:
    """
    an example class
    """

    def print(self, what):
        if what == 1:
            printString = 'world'
        else:
            printString = 'BSB'

        print('hello ' + printString)


myObject = hello()
myObject.print(0)
