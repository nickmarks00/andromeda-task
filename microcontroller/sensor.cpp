#include <ros.h>
#include <std_msgs/Bool.h>

#define SENSOR 7

ros::NodeHandle node_handle;

std_msgs::Bool motion_bool;

ross::Publisher sensor_publisher("motion_detected",
                                 &motion_bool); // register the publisher

void setup() {

  node_handle.initNode();
  node_handle.advertise(sensor_publisher); // turn on publishing!
}

void loop() {
  int val = digitalRead(SENSOR);
  if (val == HIGH) { // sound detected from microphone
    motion_bool.data = true;
  } else {
    motion_bool.data = false;
  }

  sensor_publisher.publish(&motion_bool);
  node_handle.spinOnce();
  delay(250);
}
