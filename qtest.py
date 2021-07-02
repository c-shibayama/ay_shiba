#!/usr/bin/env python
from core_tool import *
import rospy
import math

# quqternion wo test

def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):



  ct.robot.MoveToQ([-0.02225494707637879, 0.027604753814144237, 0.02256845844164128, -2.2001560115435073, -0.00047772651727832574, 0.6569580325147487, 0.0010119170182285682], 2.0, blocking=True)
 
   
  pi1 = math.pi/2
  pi2 = math.pi
  q1 = [1*math.sin(pi1/2), 0*math.sin(pi1/2), 0*math.sin(pi1/2), math.cos(pi1/2)]
  q2 = [0*math.sin(pi2/2), 0*math.sin(pi2/2), 1*math.sin(pi2/2), math.cos(pi2/2)]
  q3 = MultiplyQ(q2,q1)
  print(q3)
  


  #x:pi/2 -> z:pi
  #[a, b, c] = [0.6, 0, 0.2]
  [a, b, c] = [0.6, 0, 0.2]
  
  
  
  if a == 0:
    theta = math.pi
  else: 
    theta = math.atan2(b, a)

  ct.robot.MoveToX([a, b, c, q3[0], q3[1], q3[2], q3[3]], 3.0, blocking=True)

  

  x = list(ct.robot.FK())

  print(x)

  i = 1
  while  i > 0:
    x = list(ct.robot.FK())
    q = list(ct.robot.Q())
    r = math.sqrt(x[0]**2+x[1]**2)
    c = raw_input()
    if c == 'w':
      x[0] = (r+0.1)*math.cos(theta)
      x[1] = (r+0.1)*math.sin(theta)
      ct.robot.MoveToX(x,3.0,blocking=True)
    elif c == 's':
      x[0] = (r-0.1)*math.cos(theta)
      x[1] = (r-0.1)*math.sin(theta)
      ct.robot.MoveToX(x,3.0,blocking=True)
    elif c == 'a':
      q[0] += 0.1
      ct.robot.MoveToQ(q,3.0,blocking=True)
    elif c == 'd':
      q[0] -= 0.1
      ct.robot.MoveToQ(q,3.0,blocking=True)
    elif c == 'c':
      x[2] -= 0.1
      ct.robot.MoveToX(x,3.0,blocking=True)
    elif c == 'r':
      x[2] += 0.1
      ct.robot.MoveToX(x,3.0,blocking=True)

    elif c == 'u':
      q[5] += 0.1
      ct.robot.MoveToQ(q,3.0,blocking=True)

    else:
      break


  #q = list(ct.robot.Q())
  #a = input()
  #q[6] += a
  #ct.robot.MoveToQ(q,3.0,blocking=True)

