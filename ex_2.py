class MyNumbers():
   
    
  def __init__(self,n_start):
    self.n_start = n_start
    n_class = self.n_start
    
  def __iter__(self):
    self.a = self.n_start
    return self

  def __next__(self):
    x = self.a
    self.a += 2
    n_class = self.a
    return x

myclass = MyNumbers(5)
myiter = iter(myclass)

n = myiter.n_start
m = myclass.n_start
m2 = next(myclass)
print("start:",n,m,m2)

myclass2 = MyNumbers(8)
myiter2 = iter(myclass)
n = myiter2.n_start
m = myclass2.n_start
print("start2:",n,m,m2)

while n < 17:
    n = next(myiter)        
    m = next(myclass)
    print(n,m)
    
print("myclass.n_start:",myclass.n_start)