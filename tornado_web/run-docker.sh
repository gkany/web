
label="tornado"
version="v0.1"
name=$label
if [ $# -gt 2 ]; then
    version=$1
    name=$2
fi
tag=${label}":"${version}

echo '>>> docker build '${tag}
docker build -t  ${tag}  .

echo ">>> docker run "${tag} " --> " ${name}
docker run --name  ${name} -e HOST_OPTS=`hostname`  -dit  -p 8051:8051   ${tag}

