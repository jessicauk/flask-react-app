class Computer:
  def config(self):
    print("i5, 16GB, 1TB")
c1 = Computer()
c2 = Computer()
print(type(c1))
c1.config()
Computer.config(c2)
