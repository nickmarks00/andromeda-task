# Andromeda Take Home Task

## Installation

### Docker
1. Clone the repository with `git clone`.
2. Change into the directory.
3. Run `docker build -t <container-name> .` to build container.
4. Run `docker run -it <container-name>` to launch package.

### Arduino Sensor
To run the code in `microcontroller/sensor.cpp`:
1. Install the necessary dependencies with APT
```bash
sudo apt-get install ros-iron-rosserial
sudo apt-get install ros-iron-rosserial-arduino
```
2. Connect the sensor to the appropriate pins. Ignoring the LED, it should be the same as here:
![](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2016/10/microphone-sound-sensor_bb.png?w=676&quality=100&strip=all&ssl=1)
3. Open the file in the Arduino IDE.

## Documentation

### System Diagram
Find here a system diagram highlighting the basic flow of information in my solution:
![](https://res.cloudinary.com/df6vf0noc/image/upload/v1713531148/system_diagram_bsk8h4.jpg)

Note that this assumes that the USB camera is plugged into the Raspbery Pi and the Docker container has been launched on the Pi as well.

### Testing
- I'd start by simulating the possible combinations of signals that the system could receive and ensure that the correct output is observed each time. For example, motion is detected and the camera is already recording should produce no additional firing of the feeding motor or any additional streaming process.
- I perhaps question the reliability of a microphone sensor for detecting the presence of a dog. I would test the threshold on the sensor to see how many false positives/negatives it captures.

### Considerations and Assumptions
- I have assumed here that the motor/camera recording should "run" for 5 seconds - not that this is realistic, but with the random polling of the motion detection every 1 second it was easy to test this way.
- There is also the assumption that the user has some way of playing back ROS 2 bag files. See **Next Steps** below for further discussion.

### Next Steps
- I would want to spend time figuring out how to save the ROS2 bags to file in a more useful format i.e. mp4.
- Could add a proper actuator that listens to the topic from teh feed motor to turn on when motion detected.

### Issues
- When running the package in the Docker container, it may not detect a USB camera connected to the system.
