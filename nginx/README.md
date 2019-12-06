# 启动
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

# test  
``` shell
./test.sh  
``` 

# nginx 配置域名访问  
## nginx config  
配置server_name  
例如：  
``` text  
server_name tornado.test.net;  
```

## 宿主机host配置：  
``` text
localhost:nginx a123$ cat /etc/hosts | grep "test"
127.0.0.1   flask.test.net
127.0.0.1   tornado.test.net
localhost:nginx a123$ 
```

## 域名测试  
``` shell  
http://tornado.test.net:8052/api/v1/test  
http://flask.test.net:8042/api/v1/test  
```  
