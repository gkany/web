# -*- coding:utf-8 -*-

import json
import datetime

import tornado.ioloop
import tornado.web
import tornado.httpserver

from tornado.options import define, options, parse_command_line

headers = {"content-type": "application/json"}

# 定义默认端口
define('port', default=8051, type=int, help="this is the port >for application")

# 权限验证
auth_list = {
    'origon': 'YnVmZW5nQDIwfshRlbmc='
}

class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-type, Accept, connection, User-Agent, Cookie, Authorization")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        remote_ip = self.request.remote_ip
        real_ip = self.request.headers.get('X-Real-IP')
        forwarded_ips  = self.request.headers.get('X-Forwarded-For')
        ip_data = 'remote_ip: {}, real_ip: {}, forwarded-for: {}'.format(remote_ip, real_ip, forwarded_ips)

        now_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        msg = '[{}] hello tornado web. ip data: {}'.format(now_time, ip_data)
        print(msg)
        return self.write(msg)

    def options(self):
        self.post()

    def post(self):
        auth = self.request.headers.get('authorization', '') 
        if auth not in auth_list.values():
            return self.write({'msg': 'no access authority!', 'code': '400'})

        remote_ip = self.request.remote_ip
        real_ip = self.request.headers.get('X-Real-IP')
        forwarded_ips  = self.request.headers.get('X-Forwarded-For')
        ip_data = 'remote_ip: {}, real_ip: {}, forwarded-for: {}'.format(remote_ip, real_ip, forwarded_ips)

        now_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        msg = '[{}] hello tornado web. ip data: {}'.format(now_time, ip_data)
        print(msg)
        return self.write({'msg': msg, 'code':'200'})

def main():
    print('------ tornado http server start --------')
    parse_command_line()
    # 1. 创建一个应用对象
    app = tornado.web.Application(
        handlers=[
            (r'/api/v1/test', MainHandler),
        ],
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(options.port, address='0.0.0.0')
    http_server.start(2) # 多进程
    tornado.ioloop.IOLoop.current().start() # 

if __name__ == '__main__':
    main()
