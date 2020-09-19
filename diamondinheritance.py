class A:
  def met(self):
      print("This is class A")
class B(A):
  def met(self):
      print("This is class B")
class C(A):
    pass
class D(B,C):
    pass
a=A()
b=B()
c=C()
d=D()

print(d.met())