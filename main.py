class foo:
 @classmethod
 def hi (cls):
    print(cls.__name__)

my_object = foo()
my_object.hi()


class bar:
    @staticmethod
    def hi():
        print("i dont want parameters")

another_object = bar()
another_object.hi()