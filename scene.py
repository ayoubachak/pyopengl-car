# -*- coding: utf-8 -*-
from sys import argv, exit
from time import sleep
from math import pi,radians,sin,cos
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

from primitives import floor,wcs, cube_colored
from models import axe, wheel, car, wcs_zxy, bolt

#---------------------- initialisation --------------------------
size,theta,spin=1.0,0.0,0.0
ox,oy,oz=0,0,1
# camera position (spherical coordinates)
c_rho,c_phi,c_theta=5,0,0
c_position=[c_rho*sin(radians(c_phi)),0,c_rho*cos(radians(c_phi))]
# camera direction : WCS center
c_direction=[0,0,0]
# camera vertical axis : Oy
c_viewup=[0,1,0]

def gl_init() :
  # glClearColor(1.0,1.0,1.0,0.0);
  glClearColor(0.5,0.5,0.5,0.0)
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
  glEnable(GL_DEPTH_TEST)
  glEnable(GL_CULL_FACE)
  glShadeModel (GL_SMOOTH)
def glut_init() :
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE)
  glutInitWindowSize(1200,1000)
  glutInitWindowPosition(100,100)
  glutCreateWindow(sys.argv[0])
def glut_event():
  glutDisplayFunc(display)
  glutReshapeFunc(reshape)
  glutKeyboardFunc(on_keyboard_action)
  glutSpecialFunc(on_special_key_action)
  glutMouseFunc(on_mouse_action);

#----------------------gestion de scene ------------------------------


def display() :
  global size,spin
  global ox,oy,oz
  global c_position,c_direction,c_viewup
  gl_init()
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluLookAt(c_position[0],c_position[1],c_position[2],
            c_direction[0],c_direction[1],c_direction[2], 
            c_viewup[0],c_viewup[1],c_viewup[2])
  floor(10*size)
  wcs(4*size)
  # wcs_zxy(size * 0.5)
  # wheel(size,5)
  car(size)
  glPushMatrix()
  # glRotatef(spin,ox,oy,oz)
  # glColor3f(1.0,1.0,1.0)
  # square(size)
  # cube_colored(size)
  # wheel(size,3)
  # car(size)
  glPopMatrix()
  glutSwapBuffers()

def reshape(width,height) :
  glViewport(0,0, width,height)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(60.0,width*1.0/height, 1.0, 10.0)

# def reshape(w,h) :
#    glViewport (0,0,w,h)
#    glMatrixMode (GL_PROJECTION)
#    glLoadIdentity ()
#    glFrustum (-1.0, 1.0, -1.0, 1.0,  1.0, 10.0)

def animate() :
    global spin
    spin=spin+0.005
    if spin >= 360.0 :
        spin=spin%360.0
    glutPostRedisplay()


#---------------------- interacting ------------------------------
def on_keyboard_action(key, x, y) :
  global size
  global spin
  global c_theta
  global ox,oy,oz
  speed=1.0
  if key==b'a': 
   glutIdleFunc(animate)
  elif key==b'A': 
   glutIdleFunc(None)
  elif key==b'h':
    print("----------------------------------------\n")
    print("Documentation interaction  : ACHAK-Ayoub, BEN HASSOUNA-Mounir, EL ALAMI-Adam \n") 
    print("----------------------------------------\n") 
    print("a/A : lancer/Arreter l'animation \n")
    print("h : afficher cette aide \n")
    print("f : afficher les facettes (Face) \n")
    print("e : afficher les aretes (Edge) \n")
    print("v : afficher les sommets (Vertex) \n")
    print("c/C : afficher les faces CW/CCW \n")
    print("r/R : redimensionner l'objet \n")
    print("t/T : modifier l'angle de rotation \n")
    print("x : rotation autour de l'axe Ox\n")
    print("y : rotation autour de l'axe Oy\n")
    print("z : rotation autour de l'axe Oz\n")
    print("i : état initial \n")
    print("u/U : deplacer la camera en hauteur \n")
    print("key up : avancer la camera\n")
    print("key down : reculer la camera\n")
    print("key left: tourner la camera sur la gauche\n")
    print("key right: tourner la camera sur la droite\n")
    print("s : sortie d'application \n")
  elif key==b'f':
    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
  elif key==b'e':
    glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
  elif key==b's' :
    glPolygonMode(GL_FRONT_AND_BACK,GL_POINT)
  elif key==b'c' :
    glFrontFace(GL_CW)
  elif key==b'C' :
    glFrontFace(GL_CCW)
  elif key==b'r' :
    size-=0.1
  elif key==b'R' :
    size+=0.1
  elif key==b't' :
    spin-=1.0
  elif key==b'T' :
    spin+=1.0
  elif key==b'x' :
    ox,oy,oz=1,0,0
    spin=0.0
  elif key==b'y' :
    ox,oy,oz=0,1,0
    spin=0.0
  elif key==b'z' :
    ox,oy,oz=0,0,1
    spin=0.0
  elif  key == b'u' :
    c_theta+=0.1*speed
    c_position[1]=c_rho*sin(radians(c_theta))*cos(radians(c_phi))
  elif  key == b'U' :
    c_theta-=0.1*speed
    c_position[1]=c_rho*sin(radians(c_theta))*cos(radians(c_phi))
  elif key==b's' :
    exit(0)
  else :
    pass
  glutPostRedisplay()

def on_special_key_action(key, x, y) :
  global c_rho,c_phi,c_position
  speed=0.1
  if key ==  GLUT_KEY_UP :
      c_rho=c_rho-speed
      c_position[0]=c_rho*sin(radians(c_phi))
      c_position[2]=c_rho*cos(radians(c_phi))
  elif  key ==  GLUT_KEY_DOWN :
      c_rho=c_rho+speed
      c_position[0]=c_rho*sin(radians(c_phi))
      c_position[2]=c_rho*cos(radians(c_phi))
  elif key ==  GLUT_KEY_LEFT :
      c_phi=c_phi-5*speed
      c_position[0]=c_rho*sin(radians(c_phi))
      c_position[2]=c_rho*cos(radians(c_phi))
  elif  key ==  GLUT_KEY_RIGHT :
      c_phi=c_phi+5*speed
      c_position[0]=c_rho*sin(radians(c_phi))
      c_position[2]=c_rho*cos(radians(c_phi))
  else :
      pass
  glutPostRedisplay()

def on_mouse_action(button,state,x,y) :
  pass

if __name__ == "__main__" :
  glut_init()
  glut_event() 
  glutMainLoop()

