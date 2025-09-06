#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from turtlesim.msg import Pose

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ":: %.2f %.2f", data.x, data.y)

def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/turtle1/pose", Pose, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()