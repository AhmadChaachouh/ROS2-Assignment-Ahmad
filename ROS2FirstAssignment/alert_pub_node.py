import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32

class AlertPublisher(Node):

    def __init__(self):
        super().__init__('alert_publisher')
        self.subscription = self.create_subscription(
            Float32,
            'alert_trigger',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(String, 'alert', 10)

    def listener_callback(self, msg):
        temperature = msg.data
        self.get_logger().warn(f'Alert Triggered! Temperature: {temperature}')
        alert_msg = String()
        alert_msg.data = f'ALERT! Temperature {temperature} exceeds threshold!'
        self.publisher_.publish(alert_msg)

def main(args=None):
    rclpy.init(args=args)
    alert_publisher = AlertPublisher()
    rclpy.spin(alert_publisher)
    alert_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
