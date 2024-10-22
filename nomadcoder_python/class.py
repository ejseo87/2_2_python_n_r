class Person:
  def __init__(self, name, age):
    self.name = name
    self.age= age
  def disp(self):
    print(self.name)
    print(self.age)
      
p = Person('Tom', 28)
p.disp()
p2 = Person('홍길동', 999)
p2.disp()

class Man:
  def __init__(self, name):
    self.name = name
    print("Initialized!")
  def hello(self):
    print("Hello "+self.name+"!")
  def goodbye(self):
    print("Goodbye "+self.name +"!")

m = Man("Nico")
m.hello()
m.goodbye()