# namedtuples for creatings read only tuples. 
from collections import namedtuple

Point = namedtuple("Point",["x", "y"])


p1 = Point(x=1,y=2)
print(p1.__len__())
print(p1)
print(p1.x)
print(p1.y)
