    
 #Jenkins config: 
 
 ## Prerequisites
    > image mjenkins already done (available in the folder mjenkins). 
 
 ### 1. Run socket montage: 
    > docker build -t mjenkins .

 ### 2. Data Container for persist the configuration.

    > docker run --name jenkins-data mjenkins echo "Jenkins Data Container"
    
 ### 3. Start jenkins on 8080 port: 
 
    > docker run -d --name jenkins -p 8080:8080 \
    --volumes-from jenkins-data \
    -v /var/run/docker.sock:/var/run/docker.sock \
    mjenkins

### 4. Acess http://localhost:8080 or {host}:8080:   
    
    >  4.1 Create new jobs.
    > 4.2 Put item_name: 'semantix_api'
    > 4.3 Select Freestyle project
    > 4.4 Defin Source Code Manangement (in this case the source is GitHub - GIT). 
    > 4.5 Insert the git repository link on the field
    
### Add build step and select Exec Shell. In the box copy the pipeline.txt on it.    

    > Set username and password in the pipeline.txt 
    
        
    
 
    
