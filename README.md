# learn_kube
Trying to learn Kubernetes CNCF landscape tools by doing. 

Thinking something like:  

1: start  
make easy python
make into docker image
push to dockerhub
get kubernetes for server and service with deployment on minikube

2: helm  
turn into helm chart to do things from 1

3: more k8s  
liveness, configmap, values, secrets, pod security policies
* get connection to the mysql deployment with login (have test.py that does this just isn't in the server code yet)
* find out how to get password from secret to connect (right now it's password with test dB but can I dynamically get the dB name from mysql values yaml? or maybe who cares, that doesn't have to be dynamic, it can be given in a configmap to the code that makes it maybe?)
	* You can override the value in the subchart https://helm.sh/docs/topics/chart_template_guide/subcharts_and_globals
	* Then can I use that populated from a secret? Looks like it, we can override the values and that will populate the secrets yaml that makes the secrets
		Then we could eventually move that initial definition out to vault. 
* make my own secrets for password mysql dB that gets drawn from the values file that gets drawn from env? 

4: get ready for dB  
secret stoage w/ vault and use (off cluster probably w/ exposed port) 

5: dB  
add a mysql dB (off cluster w/ docker and exposed port, just pretend) and have server talk to that, maybe use helm requirement for mysql and put onto cluster? 

6: native dB  
vitess

: storage
have python server write files and shit, 3x server share storage, PVC things? 
