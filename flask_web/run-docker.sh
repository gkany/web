
label="flask"
version="v0.1"
name=$label
default=8041
if [ $# -gt 2 ]; then
    version=$1
    name=$2
fi
tag=${label}":"${version}

echo '>>> docker build '${tag}
docker build -t  ${tag}  .

echo ">>> docker run "${tag} " --> " ${name}
docker run --name  ${name} -e HOST_OPTS=`hostname`  -dit  -p ${default}:${default}  ${tag}

