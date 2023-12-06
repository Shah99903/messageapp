class Message:
    def __init__(self, content, sender):
        self.content = content
        self.sender = sender

class Subscriber:
    def __init__(self, name):
        self.name = name

    def receive_message(self, message):
        print(f"{self.name} received a message from {message.sender}: {message.content}")

class Publisher:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def publish_messages(self, messages):
        for subscriber in self.subscribers:
            if subscriber.name in messages:
                message_content = messages[subscriber.name]
                message = Message(message_content, "Publisher")
                subscriber.receive_message(message)


if __name__ == "__main__":
    publisher = Publisher()

    subscriber1 = Subscriber("Subscriber1")
    subscriber2 = Subscriber("Subscriber2")

    publisher.add_subscriber(subscriber1)
    publisher.add_subscriber(subscriber2)

    messages_to_publish = {
        "Subscriber1": "Hello World!",
        "Subscriber2": "Hello World 2!"
    }

    publisher.publish_messages(messages_to_publish)

