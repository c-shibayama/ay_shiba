
#!/usr/bin/env python
from core_tool import *
import rospy
import time
#from test5 import position2

def Run(ct,*args):
  ct.robot.OpenGripper()
  position2 = ct.GetAttr('obj1','position')
  if position2[0] == 0 and position2[1] > 0:
    theta = math.pi/2
  elif position2[0] == 0 and position2[1] < 0:
    theta = -math.pi/2
  else:
    theta = math.atan2(position2[1], position2[0])
  str = ct.GetAttr('obj2','which')
  if str == "side":
    print("The object's direction is side")
    ct.robot.MoveToQ([theta, 0.0276047, 0.0225684, -2.2001560, -0.0004777, 0.6569580, 0.0010118], blocking=True)
  elif str == "up":
    print("Object's direction is up")
    ct.robot.MoveToQ([-0.0222549, 0.2276047, 0.02256845844164128, -1.1001560115435073, -0.0004777, -1.8569580, 0.00101191], 2.0, blocking=True)
    rospy.sleep(2)
    ct.robot.MoveToQ([theta, 0.2276047, 0.02256845844164128, -1.1001560115435073, -0.0004777, -1.8569580, 0.00101191], 2.0, blocking=True)
  else:
    ct.robot.MoveToQ([theta, 0.0276047, 0.0225684, -2.2001560, -0.0004777, 0.6569580, 0.0010118], 2.0, blocking=True)
  print("The object's position is")
  print(position2[0],position2[1],position2[2])
  rospy.sleep(2)
  x = list(ct.robot.FK())
  x1 = copy.deepcopy(x)
  x_traj = []
  t_traj = []
  x_traj.append(x1)
  t_traj.append(0.0)
  a1 = (position2[0] - x1[0])/50
  b1 = (position2[1] - x1[1])/50
  c1 = (position2[2] - x1[2])/50
  for i in range(1, 50):
    t_traj.append(0.1*i)
    x2 = copy.deepcopy(x)
    x2[0] += a1*i
    x2[1] += b1*i
    x2[2] += c1*i
    x_traj.append(x2)
  ct.robot.FollowXTraj(x_traj, t_traj, blocking=True)
  rospy.sleep(2)
  ct.robot.MoveGripper(position2[3])
  rospy.sleep(2)
  x2[2] += 0.1
  ct.robot.MoveToX(x1, 2.0, blocking = True)
