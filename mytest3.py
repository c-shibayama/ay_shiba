#!/usr/bin/env python
from core_tool import *
import rospy
import math

# input position he hankei(r) niyotte ue mae wo erande idou
# and
# input word niyotte jouge zengo sayuu ni bisyou idou

def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):



  ct.robot.MoveToQ([-0.02225494707637879, 0.027604753814144237, 0.02256845844164128, -2.2001560115435073, -0.00047772651727832574, 0.6569580325147487, 0.0010119170182285682], 2.0, blocking=True)
  

  a = input()
  b = input()
  c = input()

  r = math.sqrt(a**2+b**2)

  print(r)

  if a == 0:
    theta = math.pi
  else: 
    theta = math.atan2(b, a)

    if r < 0.45:
      ct.robot.MoveToQ([-0.0222549, 0.2276047, 0.02256845844164128, -1.1001560115435073, -0.0004777, -1.8569580, 0.00101191], 2.0, blocking=True)

      ct.robot.MoveToQ([theta, 0.2276047, 0.02256845844164128, -1.1001560115435073, -0.0004777, -1.8569580, 0.00101191], 2.0, blocking=True)

    else:
      ct.robot.MoveToQ([theta, 0.027604753814144237, 0.02256845844164128, -2.2001560115435073, -0.00047772651727832574, 0.6569580325147487, 0.0010119170182285682], 2.0, blocking=True)

  x = list(ct.robot.FK())
  x1 = copy.deepcopy(x)
  x_traj = []
  t_traj = []
  x_traj.append(x1)
  t_traj.append(0.0)
  a1 = (float(a) - x1[0])/50
  b1 = (float(b) - x1[1])/50
  c1 = (float(c) - x1[2])/50

  for i in range(1, 50):
    t_traj.append(0.1*i)
    x2 = copy.deepcopy(x)
    x2[0] += a1*i
    x2[1] += b1*i
    x2[2] += c1*i
    x_traj.append(x2)

  ct.robot.FollowXTraj(x_traj, t_traj)
  rospy.sleep(6)

  x0 = list(ct.robot.FK())

  print(x0)

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

    elif c == 'back':
      ct.robot.MoveToX(x0,3.0,blocking=True)


    else:
      break

