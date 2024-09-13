# from math import pi,sin,cos
try :
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

from primitives import disk,cylinder,cone, torus, cube_colored, stick, rectangle



# TODO : create 3D axe with disk,cylinder,cone
def axe(base, height, slices=10, stacks=5):
   base_radius = base
   handle_height = height * 0.8
   head_height = height * 0.2
   head_base = base * 1.01  

   # Handle
   glPushMatrix()
   cylinder(base_radius * 0.2, base_radius * 0.2, handle_height, slices, stacks)
   glPopMatrix()

   # Axe head
   glPushMatrix()
   glTranslatef(0, 0, handle_height)
   cone(head_base, head_height, slices, stacks)
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
def wheel(size, n_bolts=5):
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
def car(size):

   glPushMatrix()
 
   glTranslatef(0, size, 0)
   glScalef(2, 1, 1)
   cube_colored(size)

   # Placer les roues
   wheel_size = size * 0.5
   wheel_offset = size * 1

   # Avant gauche
   glPushMatrix()
   glTranslatef(-wheel_offset, -size, wheel_offset)
   wheel(wheel_size)
   glPopMatrix()
   # Avant droite
   glPushMatrix()
   glTranslatef(wheel_offset, -size, wheel_offset)
   wheel(wheel_size)
   glPopMatrix()


   # Arrière gauche
   glPushMatrix()
   glTranslatef(-wheel_offset, -size, -wheel_offset)
   glRotatef(180, 0, 1, 0)
   wheel(wheel_size)
   glPopMatrix()
   # Arrière droite
   glPushMatrix()
   glTranslatef(wheel_offset, -size, -wheel_offset)
   glRotatef(180, 0, 1, 0)
   wheel(wheel_size)
   glPopMatrix()

   glPopMatrix()
