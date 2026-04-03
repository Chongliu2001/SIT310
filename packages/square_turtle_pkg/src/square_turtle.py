#!/usr/bin/env python3
# Import Dependencies
import rospy 
from geometry_msgs.msg import Twist 
import time 

def move_turtle_square(): 
    # Initialize the ROS node with a unique name
    rospy.init_node('turtlesim_square_node', anonymous=True)
    
    # Create a publisher object to send velocity commands to the turtle
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) 
    rospy.loginfo("Turtles are great at drawing squares!")
    
    # Main loop: keep drawing squares until the node is stopped
    while not rospy.is_shutdown():
        # Repeat 4 times to complete one square
        for _ in range(4):
            # --- Phase 1: Move forward in a straight line ---
            cmd_vel_msg = Twist()
            cmd_vel_msg.linear.x = 2.0  # Set forward linear velocity (m/s)
            velocity_publisher.publish(cmd_vel_msg)
            rospy.sleep(2)  # Keep moving forward for 2 seconds
            
            # --- Phase 2: Stop forward movement ---
            cmd_vel_msg = Twist()
            cmd_vel_msg.linear.x = 0.0  # Set linear velocity to 0
            velocity_publisher.publish(cmd_vel_msg)
            rospy.sleep(0.5)  # Short pause for stability
            
            # --- Phase 3: Rotate 90 degrees in place ---
            cmd_vel_msg = Twist()
            cmd_vel_msg.angular.z = 1.57  # Set angular velocity (rad/s), ~90 degrees
            velocity_publisher.publish(cmd_vel_msg)
            rospy.sleep(1)  # Keep rotating for 1 second
            
            # --- Phase 4: Stop rotation ---
            cmd_vel_msg = Twist()
            cmd_vel_msg.angular.z = 0.0  # Set angular velocity to 0
            velocity_publisher.publish(cmd_vel_msg)
            rospy.sleep(0.5)  # Short pause before next side

if __name__ == '__main__': 
    try: 
        move_turtle_square() 
    except rospy.ROSInterruptException: 
        pass

