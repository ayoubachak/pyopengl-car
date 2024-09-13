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
   # Adjust these values based on how you want the axe to look
   base_radius = base
   handle_height = height * 0.8
   head_height = height * 0.2
   head_base = base * 1.01  # Wider than the handle

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
    # Set a unique color for the bolt, e.g., silver
    stick(radius, radius, height, 7)
    glPushMatrix()
    glTranslatef(0, 0, height)
    # No need for a separate disk on top as stick includes both ends
    glPopMatrix()

# TODO : create wheel with bolts 
def wheel(size, n_bolts=5):
   # Set a unique color for the wheel, e.g., black
   glColor3f(0.0, 0.0, 0.0)  # Black color
   radius = size / 2
   height = size / 4
   
   # Use cylinder for the wheel body
   cylinder(radius, radius, height, 20, 5)
   
   # Add a disk on the top of the cylinder
   glPushMatrix()
   glTranslatef(0, 0, height)
   disk(0, radius, 20, 5)
   glPopMatrix()

   # Add a disk on the bottom of the cylinder (to show from the opposite side)
   glPushMatrix()
   glTranslatef(0, 0, 0)  # No need to translate since it's the base
   glRotatef(180, 1, 0, 0)  # Rotate to make it face downwards
   disk(0, radius, 20, 5)
   glPopMatrix()

   # Add bolts around the wheel
   for i in range(n_bolts):
      angle = 360 / n_bolts * i
      glPushMatrix()
      glRotatef(angle, 0, 0, 1)
      # Adjust the translation to place bolts on the surface
      glTranslatef(radius - (height * 0.5), 0, height / 2)  # Adjusted translation
      bolt(radius / 10, height)  # Adjust bolt height if necessary
      glPopMatrix()

# TODO : create car : body (axe) + 4 wheels
def car(size):

   # Add wheels to the car
   glPushMatrix()
 
   # Créer le corps de la voiture (ici un cube coloré, mais tu peux utiliser une autre primitive)
   glTranslatef(0, size, 0)
   glScalef(2, 1, 1)
   glColor3f(0.8, 0, 0) # Couleur rouge pour le corps
   cube_colored(size) # Utiliser un cube pour représenter le corps de la voiture

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
