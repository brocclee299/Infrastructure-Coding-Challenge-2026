import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class AggregatorNode(Node):
    def __init__(self):
        super().__init__('aggregator_node')
        self.a = None
        self.b = None
        self.create_subscription(Float64, '/input_topic_a', self.callback_a, 10)
        self.create_subscription(Float64, '/input_topic_b', self.callback_b, 10)
        self.pub = self.create_publisher(Float64, '/output_topic', 10)

    def callback_a(self, msg):
        self.a = msg.data
        self.try_publish()

    def callback_b(self, msg):
        self.b = msg.data
        self.try_publish()

    def aggregate(self, a, b):
        return (a + b) / 2.0

    def try_publish(self):
        if self.a is None or self.b is None:
            return
        out = Float64()
        out.data = self.aggregate(self.a, self.b)
        self.pub.publish(out)
        self.get_logger().info(f'a={self.a} b={self.b} output={out.data}')


def main():
    rclpy.init()
    node = AggregatorNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
