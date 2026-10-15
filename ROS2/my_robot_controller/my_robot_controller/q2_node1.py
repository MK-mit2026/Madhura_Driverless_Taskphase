#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import RT2String

class string_pub(Node):

    def __init__(self):
        super().__init__("q2_node1")
        self.publisher = self.create_publisher(RT2String, "/task2", 10)

    def string_pub(self, text):
        msg = RT2String()
        msg.data = text 
        self.publisher.publish(msg)
        self.get_logger().info("Published: " + text)


def main(args=None):
    rclpy.init(args=args)
    node = string_pub()

    try:
        while rclpy.ok():
            text = input("Enter a string (or 'quit' to stop): ")

            if text.lower() == "quit":
                break

            node.string_pub(text)

    except (KeyboardInterrupt, EOFError):
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()