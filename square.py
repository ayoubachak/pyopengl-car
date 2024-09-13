# -*- coding: utf-8 -*-
from sys import argv, exit
from time import sleep
import math
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()
from primitives import wcs,square
#---------------------- initialisation --------------------------
size,theta,spin=1.0,0.0,0.0
ox,oy,oz=0,1,0

def gl_init() :
#  glClearColor(1.0,1.0,1.0,0.0);
  glClearColor(0.5,0.5,0.5,0.0)
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
  glEnable(GL_DEPTH_TEST)
  glEnable(GL_CULL_FACE)

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
##  glutSpecialFunc(on_special_key_action);
##  glutIdleFunc(animation)


#---------------------- affichage de scene ------------------------------
def display() :
  global size,theta,spin
  gl_init()
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  camera=[4,3,2,0,0,0,0,1,0]
#  camera=[0,0,2,0,0,0,0,1,0]
  gluLookAt(camera[0],camera[1],camera[2], 
            camera[3],camera[4],camera[5],
            camera[6],camera[7],camera[8])
#  glutWireCube(1)
  glRotatef(spin,0,1,0)
  wcs(size+1)
  glPushMatrix()
  glRotatef(theta,ox,oy,oz)
  square(size)
  glPopMatrix()
  glutSwapBuffers()

def reshape(width,height) :
  glViewport(0,0, width,height)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(60.0,width*1.0/height, 1.0, 10.0)

def animate() :
  global spin
  spin=spin+0.005
  if spin >= 360.0 :
    spin=spin%360.0
  glutPostRedisplay()

#---------------------- interaction ------------------------------
def on_keyboard_action(key, x, y) :
  global size,theta,spin
  global ox,oy,oz
  if key==b'a': 
   glutIdleFunc(animate)
  elif key==b'A': 
   glutIdleFunc(None)
  elif key==b'h':
    print("----------------------------------------\n")
    print("Documentation interaction  : Nom-Prenom \n") 
    print("----------------------------------------\n") 
    print("a/A : lancer/Arreter l'animation \n")
    print("h : afficher cette aide \n");
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
    print("q : sortie (exit) \n")
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
    theta-=1.0
  elif key==b'T' : 
    theta+=1.0
  elif key==b'x' :
    ox,oy,oz=1,0,0
    theta=0.0
  elif key==b'y' :
    ox,oy,oz=0,1,0
    theta=0.0
  elif key==b'z' :
    ox,oy,oz=0,0,1
    theta=0.0
  elif key==b'i' :
    theta,spin=0.0,0.0
  elif key==b'q' :
    exit(0)
  else :
    pass
  glutPostRedisplay()

def on_special_key_action(key,x,y) :
  pass

def on_mouse_action(button,state,x,y) :
  pass

if __name__ == "__main__" :
  glut_init()
  glut_event() 
  glutMainLoop()
