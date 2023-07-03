from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup, ReentrantCallbackGroup
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import asyncio

class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')
        my_cb_group = ReentrantCallbackGroup()
        self.subscriber_ = self.create_subscription(
            String,
            'my_topic',
            self.callback_function,
            10,
            callback_group=my_cb_group
        )
        self.loop = asyncio.get_event_loop()  # 获取事件循环
    async def my_coroutine(self,msg):
        print("Coroutine executed start"+str(msg.data))
        await asyncio.sleep(5)
        print('Coroutine executed end'+str(msg.data))

    def callback_function(self, msg):
        task = self.loop.create_task(self.my_coroutine(msg))  # 创建任务并添加到事件循环中
        if self.loop.is_running():
            pass
        else:
            print("loop is not running , start loop")
            self.loop.run_until_complete(task)  # 运行任务直到完成

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()

    try:
        executor = MultiThreadedExecutor()
        executor.add_node(node)

        while rclpy.ok():
            executor.spin_once(timeout_sec=0.1)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()