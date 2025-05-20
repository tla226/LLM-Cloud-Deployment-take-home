import time
from send_requests import send_request

"""
The setup of the throughput measuremnet is similar to latency, though instead of measuring the time
for a singular instruction (in this case a request), we measure the total across all (arbitrary 100) requests
"""
def throughput_test(apiLink, prompt, numRequests=10):
    start_time = time.time()
    numSuccesses = 0

    # send 100 requests, and track the number of succesful responses
    for x in range(numRequests):
        response = send_request(apiLink,prompt)
        if response:
            numSuccesses += 1
    
    #get the duration of the 100 requests to calculate the throughput
    end_time = time.time()
    totDuration = end_time - start_time

    #units is requests/minute
    throughput = (numSuccesses/totDuration) * 60 if totDuration > 0 else 0

    print(f"Sent {numRequests} requests in {totDuration:.2f} seconds")
    print(f"Number of succesful responses received: {numSuccesses}")
    print(f"Throughput: {throughput:.2f} requests per minute")

    return numSuccesses, throughput

if __name__ == "__main__":
    apiLink = "http://localhost:8000" # replace with API server once I have it
    prompt = "What is the weather like today?"
    throughput_test(apiLink, prompt)


