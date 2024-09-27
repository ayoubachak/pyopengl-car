# from math import pi,sin,cos
try :
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

from primitives import disk,cylinder,cone, torus, cube_colored, stick, rectangle

# car 
vehicle_position_y, vehicle_rotation_x, wheel_rotation_angle = 0, 0, 0
translation_speed = 0.1  
wheel_rotation_speed, wheel_rotation_direction= 5, 1  
vehicle_rotation_angle, vehicle_rotation_speed, vehicle_rotation_direction = 0, 5, 1

# TODO : create 3D axe with disk,cylinder,cone
def axe(base, height, thickness=0.2, slices=10, stacks=5):
   base_radius = base
   handle_height = height * 0.8
   head_height = height * 0.2
   head_base = base * 0.8  

   # Handle
   glPushMatrix()
   cylinder(base_radius * thickness , base_radius * thickness, handle_height, slices, stacks)
   glPopMatrix()

   # Axe head
   glPushMatrix()
   glTranslatef(0, 0, handle_height)
   cone(head_base , head_height, slices, stacks)
   glPopMatrix()

# TODO : redefine  WCS  with 3D axes (Ox,Oy,Oz)
def wcs_zxy(size):
   base = 0.2 * size
   height = 3 * size
   # Draw X-axis in red
   glColor3ub(255, 0, 0)  # Red
   glPushMatrix()
   glRotatef(+90, 0, 1, 0)
   axe(base=base, height=height)
   glPopMatrix()

   # Draw Y-axis in green
   glColor3ub(0, 255, 0)  # Green
   glPushMatrix()
   glRotatef(-90, 1, 0, 0)
   axe(base=base, height=height)
   glPopMatrix()

   # Draw Z-axis in blue
   glColor3ub(0, 0, 255)  # Blue
   glPushMatrix()
   glRotatef(0, 1, 0, 0)
   axe(base=base, height=height)
   glPopMatrix()

# TODO : create bolts 
def bolt(radius, height):
    stick(radius, radius, height, 7)
    glPushMatrix()
    glTranslatef(0, 0, height)
    glPopMatrix()

# TODO : create wheel with bolts 
def wheel(size, n_bolts=5, wheel_rotation_angle=0):

   glRotatef(wheel_rotation_angle, 0, 0, 1)

   glColor3f(0.0, 0.0, 0.0)  # Black color
   radius = size / 2
   height = size / 4
   
   cylinder(radius, radius, height, 20, 5)
   
   # Add a disk on the top of the cylinder
   glPushMatrix()
   glTranslatef(0, 0, height)
   disk(0, radius, 20, 5)
   glPopMatrix()

   # Add a disk on the bottom of the cylinder (
   glPushMatrix()
   glRotatef(180, 1, 0, 0) 
   disk(0, radius, 20, 5)
   glPopMatrix()

   # Add bolts around the wheel
   for i in range(n_bolts):
      angle = 360 / n_bolts * i
      glPushMatrix()
      glRotatef(angle, 0, 0, 1)
      glTranslatef(radius - (height * 0.5), 0, height / 2)  
      bolt(radius / 10, height)  
      glPopMatrix()

# TODO : create car : body (axe) + 4 wheels
def car(size, vehicle_position_y=0, vehicle_rotation_angle=0, wheel_rotation_angle=0, position : tuple = (0,0,0), theta=0):
   size = size / 2
   glPushMatrix()
   # glRotatef(vehicle_rotation_angle, 0, 1, 0)
   # glTranslatef(vehicle_position_y, 0, 0)
   # print("vehicle_position_y", vehicle_position_y)
   # print("wheel_rotation_angle", wheel_rotation_angle)
   glTranslatef(position[0],position[1],position[2])
   glRotatef(theta,0,1,0)
   print("position", position)
   print("theta", theta)

   glTranslatef(0, size, 0)
   glScalef(2, 1, 1)
   # cube_colored(size)
   # glTranslatef(0, 0, size)
   # cone(size, size, 20, 5)
   glPushMatrix()
   # glRotatef(90, 0, 1, 0)
   glTranslatef(0, -size/4, -size * 2 )
   axe(base=1.5*size, height=size *5, thickness=0.5)
   glPopMatrix()

   # Placer les roues
   wheel_size = size * 1
   wheel_offset = size * 1

   # Avant gauche
   glPushMatrix()
   glTranslatef(size/2, 0, 0)
   glTranslatef(-wheel_offset, -size, wheel_offset)
   glRotatef(-90, 0, 1, 0)
   wheel(wheel_size, wheel_rotation_angle=-wheel_rotation_angle)
   glPopMatrix()
   # Arrière gauche
   glPushMatrix()
   glTranslatef(-wheel_offset, -size, -wheel_offset)
   glTranslatef(size/2, 0, 0)
   glRotatef(-90, 0, 1, 0)
   wheel(wheel_size, wheel_rotation_angle=-wheel_rotation_angle)
   glPopMatrix()

   # Avant droite
   glPushMatrix()
   glTranslatef(wheel_offset, -size, wheel_offset)
   glTranslatef(-size/2, 0, 0)
   glRotatef(90, 0, 1, 0)
   wheel(wheel_size, wheel_rotation_angle=wheel_rotation_angle)
   glPopMatrix()
   # Arrière droite
   glPushMatrix()
   glTranslatef(wheel_offset, -size, -wheel_offset)
   glTranslatef(-size/2, 0, 0)
   glRotatef(90, 0, 1, 0)
   wheel(wheel_size, wheel_rotation_angle=wheel_rotation_angle)
   glPopMatrix()

   glPopMatrix()
