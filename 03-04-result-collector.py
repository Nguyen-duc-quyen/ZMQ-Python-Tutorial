import time
import zmq
import pprint

def result_collector():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.connect("tcp://127.0.0.1:5558")
    collect_data = {}
    for x in range(1000):
        result = results_receiver.recv_json()
        if collect_data.has_key(result["consumer"]):
            collect_data[result["consumer"]] += 1
        else:
            collect_data[result["consumer"]] = 1
            
        if x == 999:
            print(collect_data)
            

if __name__ == "__main__":
    result_collector()