
# 方式一：
## docker-compose  
``` shell    
./compose-docker.sh  
```
注意：docker-compose里面使用环境变量之前，需要先设置环境变量  

# 方式二：
## docker build and run  
```
 ./run-docker.sh  tag_version  name
```


# 查看log
``` shell
docker-compose  logs
```  
  
``` shell 
docker logs  name
```  

## test  
``` shell
 curl  127.0.0.1:9999
``` 

