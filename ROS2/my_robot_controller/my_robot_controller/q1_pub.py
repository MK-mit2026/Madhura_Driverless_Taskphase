#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import TaskOne

class T1_pub(Node):
    def __init__(self):
        super().__init__("T1_pub")
        self.publisher = self.create_publisher(TaskOne, "/taskone", 10)

    def publish_values(self, ang_vel, radius):
        msg = TaskOne()
        msg.ang_vel = ang_vel
        msg.radius = radius

        self.publisher.publish(msg)
        self.get_logger().info("Published: angular velocity = " + str(ang_vel) + " radius = " + str(radius))

def main(args=None):
    rclpy.init(args=args)
    node = T1_pub()
    ang_vel = float(input("Enter angular velocity: "))
    radius = float(input("Enter radius: "))
    
    node.publish_values(ang_vel, radius)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()