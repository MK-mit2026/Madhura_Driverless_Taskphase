
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import RT2String


class response_node(Node):

    def __init__(self):
        super().__init__("q2_node3")

        self.response_publisher = self.create_publisher(RT2String, "/task2_response", 10)

        self.result_subscriber = self.create_subscription(RT2String, "/task2_result", self.send_response, 10)

    def send_response(self, msg):
        if msg.data == "1":
            answer = "Yes"
        else:
            answer = "No"

        response_msg = RT2String()
        response_msg.data = answer
        self.response_publisher.publish(response_msg)

        self.get_logger().info(f"Sent response: {answer}")


def main(args=None):
    rclpy.init(args=args)

    node = response_node()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
