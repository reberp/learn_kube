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

4: more k8s  
liveness, more than one of control and data planes, secrets, pod security policies

4: get ready for dB  
secret stoage w/ vault and use (off cluster probably w/ exposed port) 

3: dB  
add a mysql dB (off cluster w/ docker and exposed port, just pretend) and have server talk to that, maybe use helm requirement for mysql and put onto cluster? 

5: native dB  
vitess

: storage
have python server write files and shit, 3x server share storage, PVC things? 
