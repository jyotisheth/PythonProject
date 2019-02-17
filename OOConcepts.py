class dog():
    counter = 0

    def __init__(self):
        self.__private_var=None
        self._protected_var=None
        self.public_var = None

    @classmethod
    def increment_counter(cls):
        cls.counter += 1
        print(cls.counter)

    def setVar(self):
        self.__private_var="private"
        self._protected_var="protected"
        self.public_var="public"
        self.myvar = "new"

    def printVar(self):
        print(self.__private_var)
        print(self._protected_var)
        print(self.public_var)
        print(self.myvar)

    def func_without_self():
        print("func_without_self")



d1 = dog()
d2 = dog()
d3 = dog()
print(d3.counter)

d1.setVar()
d1.printVar()
dog.increment_counter()
print("d3",d3.counter)

#dog.func_without_self()

#print()
