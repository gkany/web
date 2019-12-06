
version=$1
name=$2
tag="tornado_web:v"${version}

docker build -t  ${tag}  .
docker run --name  ${name} -e HOST_OPTS=`hostname`  -dit  -p 8051:8051   ${tag}

