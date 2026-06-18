# Simple TF Kinematics (ROS 2)

This project is a ROS 2 Python node that simulates a moving robot using TF (transform) frames
It publishes static and dynamic transforms and provides a service to query transforms between frames.

---

# TF Tree

```text
odom
  |
robot_base
  |
robot_top
````

---

# What this project does

* Creates a static transform between `robot_base → robot_top`
* Simulates robot motion in `odom → robot_base`
* Robot moves forward continuously in x direction
* Robot rotates slowly over time
* Rotation direction flips every 12 seconds
* Provides a ROS 2 service to get transforms between any two frames

---

# Important ROS Concepts Used

* TF (Transform system)
* Static and Dynamic Transform Broadcasters
* TF Buffer and Listener
* geometry_msgs (geometry messages for position and rotation)
* Quaternions for 3D rotation
* ROS 2 Services

---

# How it works

## 1. Static Transform

* Frame: `robot_base → robot_top`
* Fixed position:

  * x = 0
  * y = 0
  * z = 0.3
* No rotation (identity quaternion)
* Never changes

---

## 2. Dynamic Transform

* Frame: `odom → robot_base`
* Updates every 0.1 seconds
* Robot behavior:

  * Moves forward in x direction by 0.05 m each step
  * y = 0, z = 0
  * Slowly rotates around Z axis
  * Rotation is applied using quaternions
  * After 12 seconds, rotation direction is reversed

---

## 3. TF Lookup Service

Service name:

```
get_transform
```

### Request

```
string frame_id
string child_frame_id
```

### Response

```
geometry_msgs/TransformStamped transform
bool success
```

### Meaning

* Takes two frame names
* Uses TF buffer to find transform between them
* Returns combined transform if available
* Returns success = False if not available

---

# Setup and Build

## 1. Go to workspace and build

```bash
cd robot_ws
colcon build
```

---

## 2. Open RViz2 (new terminal)

```bash
rviz2
```

---

## 3. Source and run node (new terminal)

```bash
. install/setup.bash
ros2 run robot_py simple_tf_kinematics
```

---

# Example Service Call

```bash
ros2 service call /get_transform robot_msgs/srv/GetTransform "{frame_id: 'odom', child_frame_id: 'robot_top'}"
```

---

# Behavior Summary

* Robot starts at origin in odom frame
* Moves forward in small steps
* Rotates slowly while moving
* Rotation direction changes every 12 seconds
* TF tree updates continuously
* Other nodes can query transforms anytime

---

# Key Idea

This project demonstrates how ROS 2 TF works by:

* Broadcasting static and dynamic transforms
* Simulating robot motion in real time
* Using TF buffer to compute frame relationships
* Providing a service to query transforms between any frames

