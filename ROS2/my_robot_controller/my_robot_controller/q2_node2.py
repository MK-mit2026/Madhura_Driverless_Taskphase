
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import RT2String


class palindrome_checker(Node):

    def __init__(self):
        super().__init__("q2_node2")

        self.result_publisher = self.create_publisher(RT2String, "/task2_result", 10)

        self.string_subscriber = self.create_subscription(RT2String, "/task2", self.check_string, 10)

        self.response_subscriber = self.create_subscription(RT2String, "/task2_response", self.show_response, 10)

    def check_string(self, msg):
        text = msg.data

        if text == text[::-1]:
            result = "1"
        else:
            result = "0"

        result_msg = RT2String()
        result_msg.data = result
        self.result_publisher.publish(result_msg)

        self.get_logger().info(
            f"String: {text}, sent result: {result}"
        )

    def show_response(self, msg):
        self.get_logger().info(f"Palindrome? {msg.data}")


def main(args=None):
    rclpy.init(args=args)

    node = palindrome_checker()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
