import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__("simple_subscriber")

        # type of messages, 
        # name of topic that the subscriber is going to listen to, 
        # function called whenever msg is reveived, 
        # size of message (buffer)
        self.subscriber_ = self.create_subscription(String, "chatter", self.msgCallback, 10)

    def msgCallback(self, msg):
        self.get_logger().info("I heard: %s" % msg.data)


def main():
    rclpy.init()
    simple_subscriber = SimpleSubscriber()
    rclpy.spin(simple_subscriber)  # keeping node up and running 
    simple_subscriber.distroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
        