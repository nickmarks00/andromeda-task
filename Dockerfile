FROM ros:iron

ENV ROS_DISTRO iron
ENV ROS_WS /ros_ws

RUN mkdir -p ${ROS_WS}/src

# Copy package into container
COPY ./src/dog_feeder/ ${ROS_WS}/src/dog_feeder/
RUN apt update && \
    rosdep update && \
    rosdep install --from-paths ${ROS_WS}/src --ignore-src -y
RUN apt install ros-iron-usb-cam -y

# Build the package
RUN /bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash && \
    cd $ROS_WS && \
    colcon build"

# Set the entry point
CMD ["/bin/bash", "-c", "source /opt/ros/$ROS_DISTRO/setup.bash && \
    source $ROS_WS/install/setup.bash && \
    ros2 launch dog_feeder main_launch.py"]
