import rclpy
from rclpy.node import Node
import asyncio
from std_msgs.msg import String
class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')
        self.subscriber_ = self.create_subscription(
            String,
            'my_topic',
            self.callback_function,
            10
        )
        self.loop = asyncio.get_event_loop()  # 获取事件循环
        self.task_id = 1
    async def my_coroutine(self):
        # 这里添加协程的逻辑代码
        await asyncio.sleep(10)
        print('Coroutine executed'+str(self.task_id))

    def callback_function(self, msg):
        self.task_id += 1
        print("callback"+str(self.task_id))
        task = self.loop.create_task(self.my_coroutine())  # 创建任务并添加到事件循环
        self.loop.run_until_complete(task)  # 运行事件循环直到任务完成

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
