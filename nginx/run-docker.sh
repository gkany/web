
version=$1
name=$2
tag="nginx_test:v"${version}

docker build -t  ${tag}  .
docker run --name  ${name} -e HOST_OPTS=`hostname`  -dit  -p 127.0.0.1:8080:80   ${tag}


