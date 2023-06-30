import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
import asyncio
class MySubscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber')
        self.subscription_ = self.create_subscription(
            String,
            'my_topic',
            self.my_callback,
            10
        )
        self.subscription_2= self.create_subscription(
            String,
            'my_topic',
            self.my_callback_2,
            10
        )
        self.subscription_
        self.subscription_2

    def my_callback(self, msg):
        # 执行一些操作
        self.get_logger().info('1my_callback: "%s"' % msg.data)
        # 延时操作
        time.sleep(10)
        self.get_logger().info('2my_callback: "%s"' % msg.data)

 
    def my_callback_2(self, msg):
        self.get_logger().info('my_callback_2: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    subscriber = MySubscriber()
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
