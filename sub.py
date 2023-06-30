import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
import threading

class MySubscriber1(Node):
    def __init__(self):
        super().__init__('my_subscriber1')
        self.subscription = self.create_subscription(
            String,
            'topic1',
            self.callback,
            10
        )
    
    def callback(self, msg):
        # 执行一些操作
        self.get_logger().info('Subscriber 1: "%s"' % msg.data)
        time.sleep(10)
        self.get_logger().info('Subscriber 1: Finished')

class MySubscriber2(Node):
    def __init__(self):
        super().__init__('my_subscriber2')
        self.subscription = self.create_subscription(
            String,
            'topic2',
            self.callback,
            10
        )
    
    def callback(self, msg):
        # 执行一些操作
        self.get_logger().info('Subscriber 2: "%s"' % msg.data)
        time.sleep(5)
        self.get_logger().info('Subscriber 2: Finished')

