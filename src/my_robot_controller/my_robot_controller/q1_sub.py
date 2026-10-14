#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import TaskOne

class T1_sub(Node):

    def __init__(self):
        super().__init__("task1_sub")
        self.subscription = self.create_subscription(TaskOne, "/taskone", self.sub_node, 10)

    def sub_node(self,msg):
        speed = msg.ang_vel * msg.radius
        self.get_logger().info("Longitudinal speed: " + str(speed) + " m/s ")

def main(args=None):
    rclpy.init(args=args)
    node = T1_sub()
    
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()