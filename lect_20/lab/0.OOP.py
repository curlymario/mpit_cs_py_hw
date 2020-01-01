class Dog:
    def __init__(self, name='Dog', angry=False, count=2):
        self.name = name
        self.angry = angry
        self.count = count

    def __str__(self):
        return self.name + ' ' + str(self.score)

    def say_bow(self):
        if self.angry:
            print('BOW', '-WOW' * (self.count - 1), sep='')
        else:
            print('Bow', '-wow' * (self.count - 1), sep='')

    def ping(self):
        self.angry = True

    def feed(self, food_count):
        if food_count > 10:
            self.angry = False

my_dog = Dog('Max', True, 3)
another_dog = Dog()
my_dog.say_bow()
another_dog.say_bow()

my_dog.feed(20)
my_dog.say_bow()
my_dog.ping()
my_dog.say_bow()

Dog.say_bow(my_dog) # = my_dog.say_bow()

str(my_dog)     # 'Max 3'

class A:
    def f(self):
        print('hello')

a = A()
type(a)                 # <class '__main__.A'>
type(A)                 # <class 'type'>
type(type)              # <class 'type'>
type(1)                 # <class 'int'>
type(int)               # <class 'type'>

type(A.f)               # <class 'function'>
type(a.f)               # <class 'method'>

m = a.f
m is A.f                # False
m.__func__ is A.f       # True
m.__self__ is a         # True
m.__func__(m.__self__)  # hello
m()                     # hello
a.f()                   # hello
A.f(a)                  # hello