#!/usr/bin/env python

from motion_planner import MotionPlanner

mp = MotionPlanner(20, "169.254.74.58", 30000)
mp.move_to_home()
mp.move_to_grabbing_points(80, -500, 100, -500, 50)
