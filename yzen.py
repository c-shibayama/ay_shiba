#!/usr/bin/python
from core_tool import *

# yz heimen de en wo egaku

def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):
	r = 0.05
	x = list(ct.robot.FK())
	x1 = copy.deepcopy(x)
	x1[1] -= r
	ct.robot.MoveToX(x1, 1.0,  blocking=True)
	x_traj = []
	t_traj = []
	x_traj.append(x1)
	t_traj.append(0.0)
	for i in range(1, 50):
		t_traj.append(0.1*i)
		x2 = copy.deepcopy(x)
		x2[1] += -r*math.cos(3.0*0.1*i)
		x2[2] += r*math.sin(3.0*0.1*i)
		x_traj.append(x2)
	print t_traj
	print x_traj
	ct.robot.FollowXTraj(x_traj, t_traj)
