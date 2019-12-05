
version=$1
name=$2
tag="flask_web:v"${version}

docker build -t  ${tag}  .
docker run --name  ${name} -e HOST_OPTS=`hostname`  -dit  -p 9999:9999   ${tag}

