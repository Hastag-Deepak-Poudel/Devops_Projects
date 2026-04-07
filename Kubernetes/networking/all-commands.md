1. To creae namespace:
	kubectl create ns my-namespace

2. To create serviceAccount:
	kubectl create serviceaccount <service-Acc-name> -n <your-namespace>

3. Check if serviceAccount exists:
	kubectl get sa <serviceAcc-name> -n <your-namespace>

4. Check if role exists:
	kubectl get role <role-metadata-name> -n <your-namespace>

5. Check if rolebinding exists:
	kubectl get rolebinding <RB-name> -n <your-namespace>


Final command to check if rolebinding works:
	
	kubectl auth can-i <role-verbs> pods \
  --as=system:serviceaccount:<service-Account-name>:<your-namespace> \
  -n <your-namespace>


example:	kubectl auth can-i list pods --as=service:serviceaccount:payments:payments-devs -n payments


you can change the role-verbs to check the roles like, create, delete, edit, etc. 
The result will come either yes/no


