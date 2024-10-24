import time
import zmq
import random


def consumer():
    consumer_id = random.randrange(1, 10005)
    print("[INFO]: Worker ID: {}".format(consumer_id))
    context = zmq.Context()
    
    # Receive work from producer
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5557")
    
    # Push the work to result collector
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:5558")
    
    while True:
        work = consumer_receiver.recv_json()
        data = work["num"]
        result = {'consumer': consumer_id, 'num': data}
        if data%2 == 0:
            print("[INFO] Sending ")
            consumer_sender.send_json(result)
            
if __name__ == "__main__":
    consumer()