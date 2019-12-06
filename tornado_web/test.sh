
base_url="127.0.0.1:8051"
echo $base_url
curl http://${base_url}/api/v1/test -H "Content-Type:application/json" -H "authorization:YnVmZW5nQDIwfshRlbmc="  -X POST --data '{"name": "zhang3", "age": 23}'

echo " "

