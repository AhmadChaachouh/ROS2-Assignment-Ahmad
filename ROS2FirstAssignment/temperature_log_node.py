import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import os

class TemperatureLogger(Node):

    def __init__(self):
        super().__init__('temperature_logger')
        self.subscription = self.create_subscription(
            Float32,
            'temperature',
            self.listener_callback,
            10)
        self.log_file_path = os.path.join(os.path.expanduser('~'), 'temperature_log.txt')
        self.get_logger().info(f'Logging temperature data to {self.log_file_path}')

    def listener_callback(self, msg):
        temperature = msg.data
        self.get_logger().info(f'Received temperature: {temperature}')
        with open(self.log_file_path, 'a') as log_file:
            log_file.write(f'{temperature}\n')

def main(args=None):
    rclpy.init(args=args)
    temperature_logger = TemperatureLogger()
    rclpy.spin(temperature_logger)
    temperature_logger.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
