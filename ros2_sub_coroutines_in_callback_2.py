import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import asyncio

class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')
        self.subscriber_ = self.create_subscription(
            String,
            'my_topic',
            self.callback_function,
            10
        )

    async def my_coroutine(self):
        print("qqq")
        await asyncio.sleep(5)
        print('Coroutine executed')

    def callback_function(self, msg):
        loop = asyncio.get_event_loop()  # 获取当前的事件循环
        task = loop.create_task(self.my_coroutine())  # 创建任务并添加到事件循环中
        loop.run_until_complete(task)  # 运行任务直到完成

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()

    try:
        executor = rclpy.executors.SingleThreadedExecutor()
        executor.add_node(node)

        while rclpy.ok():
            executor.spin_once(timeout_sec=0.1)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
