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
        self.id=0

    async def exec(self,delay,callback,fut:asyncio.Future):
        # await asyncio.sleep(delay)
        callback()
        # fut.set_result(None)

    def send_func(self):
        print("send_func")

    def my_callback(self, msg):
        # 执行一些操作
        print('Received message:', msg.data)
        # 延时操作
        timer = self.create_timer(1.0, self.delayed_action)

    def delayed_action(self):
        # 在延时后执行一些操作
        self.get_logger().info('Delayed action "%s"' % str(self.id))
    
    async def my_callback_2(self, msg):
        self.id +=1
        self.get_logger().info('my_callback_2: "%s"' % str(self.id))
        self.get_logger().info('my_callback_2: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    subscriber = MySubscriber()
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
