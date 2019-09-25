class SomeClass:
  variable_1 = "This is a class variable"
  variable_2 = 100

  def __init__(self, param1, param2):
    self.instance_var1 = param1
    self.instance_var2 = param2

  def create_array(self):
    self.array = []

  def insert_to_array(self, value):
    self.array.append(value)

  def get_array(self):
    return self.array

  @classmethod
  def class_method(cls):
    print("Class method was called")

# instance class
object1 = SomeClass("Something", 18)
object2 = SomeClass(28,6)

# class variables
object1.variable_1
object2.variable_1
print(object1.variable_1)
print(object1.variable_2)
print(object2.variable_1)
print(object2.variable_2)

# class intance variables
print(object1.instance_var1)
print(object2.instance_var1)

# class instance methods
object3 = SomeClass("a", "b")
object3.create_array()
object3.insert_to_array(22)
object3.insert_to_array(23)
object3.insert_to_array(24)
object3.insert_to_array(25)
print(object3.get_array())

# class method
SomeClass.class_method()

