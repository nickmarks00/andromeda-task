import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class FeedMotorNode(Node):

    def __init__(self):
        super().__init__("feed_motor")
        self.sensor_subscriber_ = self.create_subscription(
            Bool, "motion_detected", self.motor_callback, 10
        )

    def motor_callback(self, msg: Bool):
        if msg.data:
            self.get_logger().info("Feeding motor activated...")


def main(args=None):
    rclpy.init(args=args)
    node = FeedMotorNode()
    rclpy.spin(node)
    rclpy.shutdown()
