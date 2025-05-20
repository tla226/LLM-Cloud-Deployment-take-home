# this script will meeasure the time to process each request sent by the requests benchmark script
#Note, when using Google colab notebook, in new cell be sure to properly upload send_request file, or place script above this one
import time
import json #for data interchange from our requests

# not yet setup, so wont work, but this will import the send_request function from the send_requests.py benchmark script
from send_requests import send_request

def latency_measurement(apiLink, promptName, numReqs = 10):
    latencies = [] #store latencies of reqs

    for x in range(numReqs): # send arbitray number of request based on how much we want to test
        reqStart = time.perf_counter() # to hold start time of req based on sysclock, using perf_counter for better precision
        apiResponse = send_request(apiLink, promptName)

        if apiResponse: # be sure we receive one
            totResponseTime = time.perf_counter() - reqStart
            latencies.append(totResponseTime) # add to our list of response times
            #Print to 4 dec places whether or not the request was recieved and latency calucalted
            print(f"Request properly receieved. Latency value: {totResponseTime:.4f} seconds")
        else:
            print("Request not received")


    #Avg latency across all requests
    avgLatency = sum(latencies) / len(latencies) if latencies else 0
    print(f"\nAverage latency across {numReqs} requests: {avgLatency:.4f} seconds")


if __name__ == "__main__":
    apiLink = "http://localhost:8000"  # the link to the API server endpoint 
    prompt = "What is the weather like today?" #replace with whatever prompt we want to send to the server
    latency_measurement(apiLink, prompt)


    
