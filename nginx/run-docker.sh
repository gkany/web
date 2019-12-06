
version=$1
name=$2
tag="nginx_test:v"${version}

docker build -t  ${tag}  .
docker run --name  ${name} -e HOST_OPTS=`hostname`  -dit  -p 8080:80  -p 8042:8042 -p  8052:8052 ${tag}


