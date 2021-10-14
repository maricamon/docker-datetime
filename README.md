## Flask app on Docker container

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
- Sample output: 
  > Running on http://172.17.0.5:5000/
```

To access container, open another terminal and run command 
```
curl -X GET -H "Content-Type: application/json" -d '{"timezone":"Asia/Manila"}' http://127.0.0.1:5000/
- Sample output:
  > {"datetime":"2021-10-14 16:07:22"}
```