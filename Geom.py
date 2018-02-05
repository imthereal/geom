#  File: Geom.py

#  Description: basic geometry

#  Student Name: Audrey McNay

#  Student UT EID: alm5735

#  Partner Name: Samuel Dillon

#  Partner UT EID: SBD584

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 1/30/18

#  Date Last Modified: 2/1/18

import math

class Point(object):
  # constructor
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  # get distance
  def dist(self, other):
    return math.hypot(self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  def __str__(self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  def __eq__(self, other):
    tol = 1.0e-16
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Circle(object):
  # constructor
  def __init__(self, radius=1, x=0, y=0):
    self.radius = radius
    self.center = Point(x, y)

  # compute cirumference
  def circumference(self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area(self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside(self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside(self, c):
    distance = self.center.dist(c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c intersects this circle (non-zero area of overlap)
  def does_intersect(self, c):
    radius_difference = abs(self.radius - c.radius)  # difference of radii
    distance_centers = self.center.dist(c.center)  # distance between centers
    radius_added = self.radius + c.radius  # radii added
    return (radius_difference < distance_centers) and (distance_centers < radius_added)

  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  def circle_circumscribes(self, r):
    x = (r.ul.x + r.lr.x) / 2
    y = (r.ul.y + r.lr.y) / 2
    self.center = Point(x, y)
    self.radius = self.center.dist(r.ul)
    return

  # string representation of a circle
  def __str__(self):
    return str(self.center) + " : " + str(round(self.radius,2)) # (2.0, 1.0) : 3.0

  # test for equality of radius
  def __eq__(self, other):
    tol = 1.0e-16
    return ((abs(self.radius - other.radius) < tol) and (abs(self.radius - other.radius) < tol))

class Rectangle(object):
  # constructor
  def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point(ul_x, ul_y)
      self.lr = Point(lr_x, lr_y)
    else:
      self.ul = Point(0, 1)
      self.lr = Point(1, 0)

  # determine length of Rectangle (distance along the x axis)
  def length(self):
    return abs(self.lr.x - self.ul.x)

  # determine width of Rectangle (distance along the y axis)
  def width(self):
    return abs(self.ul.y - self.lr.y)

  # determine the perimeter
  def perimeter(self):
    return (2 * self.length()) + (2 * self.width())

  # determine the area
  def area(self):
    return self.length() * self.width()

  # determine if a point is strictly inside the Rectangle
  def point_inside(self, p):
    check_x = (self.ul.x < p.x) and (p.x < self.lr.x)
    check_y = (self.lr.y < p.y) and (p.y < self.ul.y)
    return (check_x and check_y)

  # determine if another Rectangle is strictly inside this Rectangle
  def rectangle_inside(self, r):
    if (self.ul.x > r.ul.x) or (self.ul.y < r.ul.x): # check if UL is within bounds
	    return False
    elif (self.lr.x < r.lr.x) or (self.lr.y > r.lr.y): # check if LR is within bounds
	    return False
    else:
	    return True
  '''
    if (self.ul.x > r.ul.x) or (self.ul.y < r.ul.x): # check if UL is within bounds
	    return False
    if (self.lr.x < r.lr.x) or (self.ul.y < r.ul.y): # check if UR is within bounds
	    return False
    if (self.lr.x < r.lr.x) or (self.lr.y > r.lr.y): # check if LR is within bounds
	    return False
    if (self.ul.x > r.ul.x) or (self.lr.y > r.lr.y): # check if LL is within bounds
	    return False
    return True
  '''
  # determine if two Rectangles overlap (non-zero area of overlap)
  def does_intersect(self, other):
    if (other.lr.y > self.ul.y):
	    return False
    elif (other.ul.x > self.lr.x):
	    return False
    elif (other.ul.y < self.lr.y):
	    return False
    elif (other.lr.x < self.ul.x):
	    return False
    return True  

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  def rect_circumscribe(self, c):
    ul_x = c.center.x - c.radius
    ul_y = c.center.y + c.radius
    lr_x = c.center.x + c.radius
    lr_y = c.center.y - c.radius
    self.ul = Point(ul_x, ul_y)
    self.lr = Point(lr_x, lr_y)

  # give string representation of a rectangle
  def __str__(self):
    return str(self.ul) + " : " + str(self.lr)

  # determine if two rectangles have the same length and width
  def __eq__(self, other):
    tol = 1.0e-16
    return ((abs(self.width() - other.width()) < tol) and (abs(self.length() - other.length()) < tol))

def main():
  # open the file geom.txt
  f = open("geom.txt")

 # create Point objects P and Q
  P = f.readline()
  P = P[0 : P.index("#")].strip()
  x_P , y_P = map(float, P.split(" "))
  P = Point(x_P, y_P)

  Q = f.readline()
  Q = Q[0 : Q.index("#")].strip()
  x_Q, y_Q = map(float, Q.split(" "))
  Q = Point(x_Q, y_Q)

  # print the coordinates of the points P and Q
  print ("Coordinates of P:", P)
  print("Coordinates of Q:", Q)

  # find the distance between the points P and Q
  print("Distance between P and Q:", round(P.dist(Q),2))

  # create two Circle objects C and D
 
  C = f.readline()
  C = C[0 : C.index("#")].strip()
  x_C, y_C, radius_C = map(float, C.split(" "))
  C = Circle(radius_C, x_C, y_C)
  
  D = f.readline()
  D = D[0 : D.index("#")].strip()
  x_D, y_D, radius_D = map(float, D.split(" "))
  D = Circle(radius_D, x_D, y_D)
  
  # print C and D
  print("Circle C:", str(C))
  print("Circle D:", str(D))

  # compute the circumference of C
  print("Circumference of C:", round(C.circumference(),2))

  # compute the area of D
  print("Area of D:", round(D.area(),2))

  # determine if P is strictly inside C
  if C.point_inside(P):
  	print("P is inside C")
  else:
  	print("P is not inside C")
  # determine if C is strictly inside D
  if D.circle_inside(C):
  	print("C is inside D")
  else:
  	print("C is not inside D")
  # determine if C and D intersect (non zero area of intersection)
  if C.does_intersect(D):
  	print("C does intersect D")
  else:
  	print("C does not intersect D")
  # determine if C and D are equal (have the same radius)
  if C == D:
  	print("C is equal to D")
  else:
  	print("C is not equal to D")
  # create two rectangle objects G and H
  G = f.readline()
  G = G[0 : G.index("#")].strip()
  ulx_G, uly_G, lrx_G, lry_G = map(float, G.split(" "))
  G = Rectangle(ulx_G, uly_G, lrx_G, lry_G)

  H = f.readline()
  H = H[0 : H.index("#")].strip()
  ulx_H, uly_H, lrx_H, lry_H = map(float, H.split(" "))
  H = Rectangle(ulx_H, uly_H, lrx_H, lry_H)

  # print the two rectangles G and H
  print("Rectangle G:", str(G))
  print("Rectangle H:", str(H))

  # determine the length of G (distance along x axis)
  print("Length of G:", str(G.length()))

  # determine the width of H (distance along y axis)
  print("Width of H:", str(H.width()))

  # determine the perimeter of G
  print("Perimeter of G:", str(G.perimeter()))

  # determine the area of H
  print("Area of H:", str(H.area()))

  # determine if point P is strictly inside rectangle G
  if G.point_inside(P):
  	print("P is inside G")
  else:
  	print("P is not inside G")
  # determine if rectangle G is strictly inside rectangle H
  if H.rectangle_inside(G):
  	print("G is inside H")
  else:
  	print("G is not inside H")
  # determine if rectangles G and H overlap (non-zero area of overlap)
  if G.does_intersect(H):
  	print("G overlaps H")
  else:
  	print("G does not overlap H")

  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  circ = Circle()
  circ.circle_circumscribes(G)
  print("Circle that circumscribes G:", str(circ))

  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle

  rec = Rectangle()
  rec.rect_circumscribe(D)
  print("Rectangle that circumscribes D:", str(rec))

  # determine if the two rectangles have the same length and width
  if G == H:
  	print("G is equal to H")
  else:
  	print("G is not equal to H")

  # close the file geom.txt
  f.close()


main()
