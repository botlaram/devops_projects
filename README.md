# Demo project Jenkins-Sonarqube (Code Anaylsis)

1. As we are hosting Jenkins and Sonarqube on 8080 and 9090 respectively  
kill host (8080 and 9090)  if it is used in backend.

```shell
netstat -ano | findstr 9090 

netstat -ano | findstr 8080  

TCP    0.0.0.0:8080           0.0.0.0:0              LISTENING       7440  
TCP    [::]:8080              [::]:0                 LISTENING       7440  

taskkill /F /PID 7440
SUCCESS: The process with PID 7440 has been terminated.
```

2. build docker ./png/image following to the docker-compose.yaml file
```shell 
docker-compose up -d
```

3. URL for jenkins and sonarqube
   1. Jenkins URL: http://localhost:8080  
   Unlock Jenkins and complete the setup wizard using the initialAdminPassword.
   2. SonarQube URL: http://localhost:9000  
   Default credentials: admin/admin

4. Jenkins password
```shell
docker exec -it jenkins-container cat /var/jenkins_home/secrets/initialAdminPassword
```

5. To shutdown all containers
```shell
docker-compose down
```

6. Restart containers
```shell
docker-compose restart
or 
docker-compose restart <service-name>
or
docker-compose restart jenkins
docker-compose restart sonarqube
```

7. Update src code
   1. Browse [free-css](https://www.free-css.com/free-css-templates)  for css template, download any template.
   2. Create a branch in git Repo and commit the src code.

8. Create a wehbook in github
   1. In github > repository > setting > wehbook
   2. Add webhook payload url to "http://<ip-address>:8080/github-webhook/" (jenkins URL)
   3. Select
      * pull requests
      * push
      * Let me select individual events
   4. then select add Wehbook at bottom.

9. To trigger pipeline in Jenkins
   1. in Jenkins dashboard click on New
   2. Enter any item name and select Freestyle Project
   3. Select Source Code Management (GIT) and add Git clone URL (if GIT no option, download GIT plugin in Jenkins 
   4. Specify the respect branch. For eg(*/feat-branch)
   5. Select GitHub hook trigger for GITScm polling
   6. Then click on Save
   7. Select "Build Now" this will trigger a pipeline

10. Commit any file to the git repo and Jenkins build will trigger automatically

11. In Sonarqube select create a project manually
    1. Enter the details  
    ![Alt text](./png/image.png)
    2. Select Jenkins Option to analyze your repository.
    3. Analysis Method > Jenkins > Select GIT as platform
    4. Select Others  
    ![Alt text](./png/image-1.png)
    5. Copy the following code
    ![Alt text](./png/image-2.png)
    6. Under User Account > Security > Enter the name and generate token
    ![Alt text](./png/image-4.png)

12. In Jenkins install Sonarqube and SSHEasy2 plugin  
    1. Dashboard > Manage Jenkins > Plugins > Search [Sonarqube Scanner, SSHEasy2] install

13. Add Tools Configuration  
    1. Dashboard > Manage Jenkins > Tools
    2. Select SonarQube Scanner installations, Enter name and Save

14. In Jenkins Dashboard > Manage Jenkins > System
    1. Select SonarQube servers
    2. Enter the input for Name and Sonarqube URL
    ![Alt text](./png/image-5.png)
    3. In Server authentication token > Select Add > Jenkins
    4. In Kind select Secret Text
    5. Input Secret from (step 11.6)
    ![Alt text](./png/image-6.png)
    6. In Server authentication token > Select token name and Save

15. In Jenkins Add Sonar-Qube projectkey
    1. Dashboard > Automated-Pipeline > Configuration
    2. Select Build Steps
    3. Select Execute SonarQube Scanner
    4. Add projectKey(from Step 11.5) in Analysis properties

16. In Jenkins select respective Pipeline and Select Build Now

17. In Sonarqube > Project (you can watch scanning status)
![Alt text](./png/image-7.png)
