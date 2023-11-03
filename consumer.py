class Consumer:
    def __init__(self, channel):
        self.channel = channel
        
    def consume(self) -> None:
        def __callback(ch, method, properties, body):
            print(f' [x] Received {body}')
        
        self.channel.basic_consume(queue='hello', on_message_callback=__callback, auto_ack=True)
        
        self.channel.start_consuming()
