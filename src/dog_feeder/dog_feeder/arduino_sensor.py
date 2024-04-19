import random
import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class SensorNode(Node):
    """
    This node mocks data published by the Arduino sensor
    """

    def __init__(self):
        super().__init__("arduino_sensor")
        self.is_triggered_ = False
        self.create_timer(
            1.0, self.mock_sensor
        )  # sample data from microphone every 1.0 seconds
        self.sensor_publisher_ = self.create_publisher(Bool, "motion_detected", 10)

        self.get_logger().info("Launched sensor node...")

    def mock_sensor(self):
        """
        This just takes a random value between [0,1] and uses that to determine whether the dog
        was detected by sensor or not, just to imitate randomness of real scenario
        """
        cmd = Bool()
        if not self.is_triggered_ and random.random() > 0.8:
            cmd.data = True
            self.get_logger().warn("Sensor has been triggered...")
            self.sensor_publisher_.publish(cmd)
            time.sleep(5)
        else:
            cmd.data = False
            self.sensor_publisher_.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node)
    rclpy.shutdown()
