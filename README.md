## Flask app on Docker container

A datetime app that accepts timezone as input and returns current date and time.
> Payload structure: {"timezone":"Asia/Manila"} \
  Response format: {"datetime":"YYYY-MM-DD HH:mm:ss"} 

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
> Sample output: `Running on http://172.17.0.5:5000/` \
  Take note of the url which will be used to access container 

To access container, run in another terminal
```
curl -X GET -H "Content-Type: application/json" -d '{"timezone":"Asia/Manila"}' http://172.17.0.5:5000/
```
> Sample output: `{"datetime":"2021-10-14 16:07:22"}`

Alternatively, to access container from outside the instance / from a different device, use **port forwarding** / **ssh tunneling**. 
Run commands in separate terminals 
```
ssh -L 8080:172.17.0.5:5000 ubuntu@<Public IP of container instance>
curl -X GET -H "Content-Type: application/json" -d '{"timezone":"Asia/Manila"}' http://127.0.0.1:8080/
```
> Sample output: `{"datetime":"2021-10-14 16:07:22"}` \
  Note the format of local port forwarding \
  `ssh -L [LOCAL_IP:]LOCAL_PORT:DESTINATION:DESTINATION_PORT [USER@]SSH_SERVER` \
  If `LOCAL_IP` is not defined, ssh client binds on the localhost `127.0.0.1`
