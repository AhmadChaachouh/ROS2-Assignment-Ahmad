from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'ROS2FirstAssignment'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ahmad',
    maintainer_email='ahmad.chaachouh.cad@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature_publisher = ROS2FirstAssignment.temperature_pub_node:main',
            'threshold_subscriber = ROS2FirstAssignment.threshhold_sub_node:main',
            'alert_publisher = ROS2FirstAssignment.alert_pub_node:main',
        ],
    },
)
