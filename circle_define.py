def circle_area(x):
    num=x**2*3.14
    return num
def circle_circum(y):
    cir=y*2*3.14
    return cir
  

n=int(input('數字:'))
n=circle_area(n)
print(n)

m=int(input('數字:'))
m=circle_circum(m)
print(m)