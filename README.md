# Simple GKE Server

##Step 1: Setup GCP
Create a new google cloud project.

Enable IAM api in cloud console.
Run `gcloud init`.  Create a new configuration for your project.  Make sure you are logged in.

Retrieve the default application credential for your project.  Will need this to upload to GCR using gcloud tool.  This will override any other default application credential that you have downloaded.
```
gcloud auth application-default login
```

Create a new container cluster in your Google Cloud project.  Click "more" to expose cloud access, change cloud platform to "enabled".

Get the cluster credential so that you can deploy your app to the cluster.
```
gcloud container clusters get-credentials <cluster_name> --zone <zone_name>
```

Credential is saved to `~/.kube/config` file.

Verify by running
```
kubectl config view
```

##Step 2: Build Container

Install Docker Engine.
https://docs.docker.com/engine/installation/

Create a local clone of the Simple GKE Server github repo.  
```
git clone https://github.com/blueandgold/SimpleGKEServer.git
```

Navigate to the top-level directory of your local git repo.

Build the docker image.
```
docker build -t us.gcr.io/<project id>/simple-gke-server:<tag> .  (note the trailing period)
```

Push the image to GCR.
```
gcloud docker push us.gcr.io/<project id>/simple-gke-server:<tag>
```

##Step 3: Deploy to GKE

Create the initial service.
```
kubectl run simple-gke-server  --image=us.gcr.io/<project_id/<image>:<tag> --port=8888
```

Check the kubernetes UI.
Get the ip, username, password of the kubernete UI's
cloud console > container engine > endpoint; click show credential to get the username and password
https://<ip_of_ui>/ui   (note: must be https; ignore chrome warning)

Create a load balancer & firewall.
```
kubectl expose deployment simple-gke-server --type="LoadBalancer"
```

Retrieve the external ip of the load balancer; might take a couple of minutes.
```
kubectl get services simple-gke-server
```

Test the application is running.
```
http://<external ip>:8888
```

Check stackdriver on cloud console to see the log message.
filter on container engine > simplecluster > default, simple gke server

Test the IAM api.

list the service accounts in the project
```
http://<external_ip>:8888/service_account/list?project_id=<project id>
```

list the keys in a service account
```
http://<external_ip>:8888/service_account_key/list?project_id=<project id>&service_account_id=<service account id>
```

##Step 4: Deploy A Code Change

Make a code change in your local repo.  Don't need to commit.
Verify your code change works, by testing it locally.

```
python main.py
```

http://localhost:8888

If necessary, you might need to install these dependencies to run the local server:
```
virtualenv venv
source venv/bin/activate
pip install webapp2
pip install webob
pip install google-api-python-client
pip install Paste
```

Build a new container image.
```
docker build -t us.gcr.io/<project id>/simple-gke-server:v2 .  (note the period, and the new version)
```

Push the new container image.
```
gcloud docker push us.gcr.io/<project id>/simple-gke-server:v2
```
Deploy the new container image.
```
kubectl set image deployment/<cluster name> <cluster name>=us.gcr.io/<project id>/<image name>:<tag>
```

References:
http://kubernetes.io/docs/hellonode/
