#!/usr/bin/env python

from motion_planner import MotionPlanner

mp = MotionPlanner(20, "169.254.74.58", 30000)
mp.move_to_home()
mp.move_to_grabbing_points(60, -350, 80, -450, -175)
mp.move_to_home()
mp.move_to_dropping_pos(-200,-350,100)
mp.move_to_home()
