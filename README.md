## Flask app on Docker container

A datetime app that accepts timezone as input and returns current date and time.
> Payload structure: {"timezone":"Asia/Manila"}
> Response format: {"datetime":"YYYY-MM-DD HH:mm:ss"} 

To install Docker 
```
sudo apt-get update
sudo apt-get install docker.io -y
```

To build and run Docker image
```
cd docker-datetime
docker build -t flask-datetime:v1 .
docker run flask-datetime:v1
```
> Take note of the url which will be used to access container 
  Sample output: 
  - `Running on http://172.17.0.5:5000/`

To access container, run in another terminal
```
curl -X GET -H "Content-Type: application/json" -d '{"timezone":"Asia/Manila"}' http://127.0.0.1:5000/
```
> Sample output: 
  - `{"datetime":"2021-10-14 16:07:22"}`