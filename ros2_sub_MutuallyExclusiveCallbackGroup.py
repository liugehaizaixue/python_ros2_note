import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup, ReentrantCallbackGroup
import time
import asyncio
class MySubscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber')
        my_cb_group_1 = MutuallyExclusiveCallbackGroup()
        my_cb_group_2 = MutuallyExclusiveCallbackGroup()
        self.subscription_ = self.create_subscription(
            String,
            'my_topic',
            self.my_callback,
            10,
            callback_group=my_cb_group_1
        )
        self.subscription_2= self.create_subscription(
            String,
            'my_topic',
            self.my_callback_2,
            10,
            callback_group=my_cb_group_2
        )
        self.subscription_
        self.subscription_2
        self.id=0

    def send_func(self):
        print("send_func")

    def my_callback(self, msg):
        # 执行一些操作
        print('Received message:', msg.data)
        # 延时操作
        time.sleep(5)
        self.delayed_action(msg.data)

    def delayed_action(self,data):
        # 在延时后执行一些操作
        self.get_logger().info('Delayed action "%s"' % data)
    
    async def my_callback_2(self, msg):
        self.id +=1
        self.get_logger().info('my_callback_2: "%s"' % str(self.id))
        self.get_logger().info('my_callback_2: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    subscriber = MySubscriber()
    executor = MultiThreadedExecutor()
    executor.add_node(subscriber)
    try:
        subscriber.get_logger().info('Beginning client, shut down with CTRL-C')
        executor.spin()
    except KeyboardInterrupt:
        subscriber.get_logger().info('Keyboard interrupt, shutting down.\n')
    subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
