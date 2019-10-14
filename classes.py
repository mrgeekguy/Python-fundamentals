# Classes
# Everything in Python is class apart from Functions
# Name using Pascal case
# method - function that exists in a class
# object - something that resides inside memory

class Person:

    def __init__(self, name, age):      # 
        self.name = name                # method
        self.age = age

class Kid:
    
    def blah(self):
        print("I exist too!")           # expression

class Student(Person, Kid):             # can put () at the end as well in order to be able to inhert from another class
                                        # it will inherit Person function, but not __init__, so it must be called using super().
    counter = 0
    school = "1150 Academy"             # class attribute

    def __init__(self, name, grade, age):
        super().__init__(name, age)     # superceedes inheritance
        # built-in methods on classes
        # needs one parameter (self)
        # self is self-satisfying
        # these are instance attributes
        self.grade = grade              # instance - an occurence
        Student.counter += 1
    def have_birthday(self):
        self.age += 1
    
    def greeting(self):
        return f"Hello, my name is { self.name }. I am in grade { self.grade }"

new_student = Student("Justin", 8, 32)

new_student.greeting() # this is a method

print(new_student.greeting())

# two types of attributes 

s1 = Student(0, 1, 3)
s2 = Student(3, 3, 3)
s3 = Student (9, 0, 9)

print(s1.counter)

# Object Oriented Programming (OOP)
# APIE (4 pillars of OOP)
# Abstraction, Polymorphism, Inheritance,
# Abstraction - hiding lower level operations for user friendliness
#             - dealing with Ideas rather than Procedure
# Polymorphism - functions that operate differently depending on the data given
# Inheritance - bringing data and functionality in from a parent class or object
#               Single - inherting from one object
#               Multi-Level - chaining inheritance (layered)
#               Multiple - class inherits several other classes
#               Hierarchical - when a class is inherited by multiple classes
# Encapsulation - data and functions that manipulate that data are bundled together

name = "you"

def modd_change(to_change): # How to encapsulate data for SECURITY!
    to_change = "They"
    return to_change

name = modd_change(name)

