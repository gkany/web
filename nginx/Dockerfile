# FROM代表此次构建的镜像以哪个镜像为基础
FROM nginx:1.10.3

MAINTAINER gkany

ENV DATA_DIR /data/web
ENV LOG_DIR /data/log/nginx
RUN mkdir /data/log/nginx -p

ADD nginx/html /data/web
ADD nginx/nginx.conf /etc/nginx/nginx.conf
ADD nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
ADD nginx/conf.d/flask.conf /etc/nginx/conf.d/flask.conf
ADD nginx/conf.d/tornado.conf /etc/nginx/conf.d/tornado.conf

EXPOSE 80
EXPOSE 8042
EXPOSE 8052

ENTRYPOINT nginx -g "daemon off;"


