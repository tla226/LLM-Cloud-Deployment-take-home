Steps for endpoint deployment on Google Colab Notebook
Open new notebook --> connect to T4

0. Be sure the environment is set up with python 3.10 for compatability with TinyLlama

1. install pytorch with proper versions
!pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 torchaudio==2.0.2+cu118 -f https://download.pytorch.org/whl/torch_stable.html

2. install vllm
!pip install vllm

3. Clone tinyllama Repo
!git clone https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0 /content/TinyLlama-1.1B-Chat-v1.0

4. Optional: check to make sure it cloned properly 
!ls /content/TinyLlama-1.1B-Chat-v1.0\

5. Start the API server (running in the background)
!nohup python3 -m vllm.entrypoints.openai.api_server --model /content/TinyLlama-1.1B-Chat-v1.0 --port 8000 --host 0.0.0.0 --dtype=half > server.log 2>&1 &
    - nohup runs it in the background
    - vllm... is the api server entrypoint 
    - --model is the TinyLlama llm model we want to deploy,
        ->Must provide full path from where we cloned the github repo
    - Port and host are specified to run locally
    - --dtype == half casts torch.bfloat16 to torch.float16 to fit limit
    - > send the results to server.log to check output

6. Optional:  to check last x lines of the server log
    - !tail -n 30 server.log

7. Run benchmark request script
8. Run latency script (be sure to upload request file or simply add it to the same code cell for Google Colab notebook)
9. Run Throughput script (be sure to upload request file or simply add it to the same code cell for Google Colab notebook)
10. Check GPU utilization using built in nvidia features
    - !nvidia-smi
    
