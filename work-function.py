from math import pi
def square(width,height):
    return width * height
ans1 = square(5,6)
  #คำสั่งหาพื้นที่สี่เหลี่ยม
def triangle(base,height):
    return base * height
ans2 = triangle(5,6)/2
  #คำสั่งหาพื้นที่สามเหลี่ยม
def circle(radius):
    return pi * (radius * radius)
ans3 = circle(10)
  #คำสั่งหาพื้นที่วงกลม
print(ans1)
print(ans2)
print(ans3)
#รัฐนันทื ถิรพัฒนานนท์ ม.6/14 เลขที่ 20