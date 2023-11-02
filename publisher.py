class Publisher:
    def __init__(self, channel):
        self.channel = channel

    def publish(self, message, exchange='', routing_key='hello'):
        
        self.channel.basic_publish(exchange=exchange,
                                routing_key=routing_key,
                                body=message)
        
        print("[x] Sent 'Hello World!'")