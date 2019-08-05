class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(s):
    print("Hello my name is " + s.name)

p1 = Person("John", 36)
p1.myfunc()
