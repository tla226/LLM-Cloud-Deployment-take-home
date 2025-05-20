# this script will meeasure the time to process each request sent by the requests benchmark script

import time
import json #for data interchange from our requests

# not yet setup, so wont work, but this will import the send_request function from the send_requests.py benchmark script
from send_requests import send_request

def latency_measurement(apiLink, promptName, numReqs = 100):
    latencies = [] #store latencies of reqs

    for x in range(numReqs): # send arbitray number of request based on how much we want to test
        reqStart = time.time() # to hold start time of req based on sysclock
        apiResponse = send_request(apiLink, promptName)

        if apiResponse: # be sure we receive one
            totResponseTime = time.time() - reqStart
            latencies.append(totResponseTime) # add to our list of response times
            #Print to 4 dec places whether or not the request was recieved and latency calucalted
            print(f"Request properly receieved. Latency value: {totResponseTime:.4f} seconds")
        else:
            print("Request not received")


    #Avg latency across all requests
    avgLatency = sum(latencies) / len(latencies) if latencies else 0
    print(f"\nAverage latency across {numReqs} requests: {avgLatency:.4f} seconds")


if __name__ == "__main__":
    apiLink = ""  # Replace this with the server link/URL when I have GPU access 
    prompt = "" #replace with whatever prompt we want to send to the server
    latency_measurement(apiLink, prompt)

        
    
