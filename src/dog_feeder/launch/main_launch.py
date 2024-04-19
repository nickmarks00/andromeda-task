from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    ld = LaunchDescription()

    sensor_node = Node(package="dog_feeder", executable="arduino_sensor")
    motor_node = Node(package="dog_feeder", executable="feed_motor")
    usb_cam = Node(package="dog_feeder", executable="usb_cam")
    cam_feed = Node(package="usb_cam", executable="usb_cam_node_exe")

    ld.add_action(sensor_node)
    ld.add_action(motor_node)
    ld.add_action(usb_cam)
    ld.add_action(cam_feed)

    return ld
