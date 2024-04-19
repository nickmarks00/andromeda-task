import os
import shutil
import subprocess
import threading

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Bool


class UsbCamNode(Node):

    def __init__(self):
        super().__init__("usb_cam")
        self.sensor_subscriber_ = self.create_subscription(
            Bool, "motion_detected", self.motor_callback, 10
        )  # subscribe to motion detection
        self.cam_subscriber_ = self.create_subscription(
            CompressedImage, "/image_raw/compressed", self.img_callback, 10
        )  # subscribe to USB camera feed
        self.bag_process = None
        self.record_timer = None
        self.motion_detected = False
        self.bag_count = 0

        if os.path.exists("captures/"):  # save all captures to here
            shutil.rmtree("captures/")

        os.mkdir("captures/")

    def motor_callback(self, msg: Bool):
        self.motion_detected = msg.data

    def img_callback(self, _: CompressedImage):
        if self.bag_process is None and self.motion_detected:
            self.get_logger().info("Recording started...")
            self.bag_process = subprocess.Popen(  # launch a bag record
                [
                    "ros2",
                    "bag",
                    "record",
                    "-o",
                    f"captures/camera_bag_{self.bag_count}",
                    "/image_raw",
                ],
                # stdin=subprocess.PIPE,
            )
            self.record_timer = threading.Timer(
                5.0, self.end_bag_recording
            )  # kill the process after 5 seconds
            self.record_timer.start()
            self.bag_count += 1

    def end_bag_recording(self):
        if self.bag_process is not None:
            self.get_logger().info("Recording ended...")
            self.bag_process.terminate()
            self.bag_process = None

    def on_quit(self):
        self.end_bag_recording()
        if self.record_timer is not None:
            self.record_timer.cancel()


def main(args=None):
    rclpy.init(args=args)
    node = UsbCamNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.on_quit()
        node.destroy_node()
        rclpy.shutdown()
