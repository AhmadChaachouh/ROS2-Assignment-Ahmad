from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ROS2FirstAssignment',
            executable='temperature_publisher',
            name='temperature_publisher'
        ),
        Node(
            package='ROS2FirstAssignment',
            executable='threshold_subscriber',
            name='threshold_subscriber'
        ),
        Node(
            package='ROS2FirstAssignment',
            executable='alert_publisher',
            name='alert_publisher'
        )
    ])
