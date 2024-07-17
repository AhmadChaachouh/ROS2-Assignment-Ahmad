import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class ThresholdSubscriber(Node):

    def __init__(self):
        super().__init__('threshold_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'temperature',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Float32, 'alert_trigger', 10)
        self.threshold = 30.0  # set the temperature threshold

    def listener_callback(self, msg):
        temperature = msg.data
        self.get_logger().info(f'Received temperature: {temperature}')
        if temperature > self.threshold:
            self.get_logger().warn(f'Temperature {temperature} exceeds threshold {self.threshold}!')
            alert_msg = Float32()
            alert_msg.data = temperature
            self.publisher_.publish(alert_msg)

def main(args=None):
    rclpy.init(args=args)
    threshold_subscriber = ThresholdSubscriber()
    rclpy.spin(threshold_subscriber)
    threshold_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
