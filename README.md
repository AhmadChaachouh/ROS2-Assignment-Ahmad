# ROS 2 Temperature Monitoring System

## Overview

This project implements a temperature monitoring system using ROS 2. The system consists of the following nodes:

- **Temperature Publisher Node**: Simulates a temperature sensor by publishing random temperature values to the `temperature` topic.
- **Threshold Subscriber Node**: Subscribes to the `temperature` topic, checks if the temperature exceeds a predefined threshold, and publishes a message to the `alert_trigger` topic if the threshold is exceeded.
- **Alert Publisher Node**: Subscribes to the `alert_trigger` topic and publishes an alert message to the `alert` topic.
- **Temperature Logger Node** (Bonus): Subscribes to the `temperature` topic and logs the temperature values over time to a log file.


## Setup

1. **Clone the repository**:

   ```bash
   git clone git@github.com:AhmadChaachouh/ROS2-Assignment-Ahmad.git ~/ros2_ws/src/ROS2FirstAssignment

2. **Navigate to the workspace**:

   ```bash
   cd ~/ros2_ws

3. **Build the package:**:

   ```bash
   colcon build

4. **Source the setup script:**:

   ```bash
   source install/setup.bash

## Running the system

You can launch the entire system using the provided launch file. This will start all the nodes (temperature publisher, threshold subscriber, alert publisher, and temperature logger).

 ```bash
    ros2 launch ROS2FirstAssignment launch.py