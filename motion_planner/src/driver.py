#!/usr/bin/env python

import mover
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard %s", data.data)
    
def listener():

    rospy.init_node('UR5_driver', anonymous=True)

    rospy.Subscriber("UR5_command", String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
