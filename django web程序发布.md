## Django 程序准备

1. 将开发依赖迁移到服务器上
```
开发端：
pip freeze > requirements.txt
服务器端：
pip3 install -r requirement.txt
```
2. setting.py设置更改

```
DEBUG=False   # 从Debug状态退出
ALLOWED_HOSTS = ['*'] # 任意主机均可访问项目
STATIC_URL = '/static/' # 静态文件地址
STATIC_ROOT= '/opt/MyProject/store/static/' # 静态文件根目录
```
3. 建立数据库:
+ 进入mysql命令行下，数据库名称最好与开发时相同
+ `create myproject` 
+ 收集静态文件`python3 manage.py collectstatic` （这是一个django命令）
+ 实装项目`python3 manage.py migrate` （这是一个django命令）
+ 导入数据库`source /opt/peizhi/myproject.sql;` （这是一个mysql命令）
+ 如果项目在开发过程中有数据要一同迁移，则需提前将数据导出，上传到服务器再按照上述命令导入；

##  uwsgi的原理与流程

+ 请求服务资源， nginx作为直接对外的服务接口,接收到客户端发送过来的http请求,会解包、分析， 如果是静态文件请求就根据nginx配置的静态文件目录，返回请求的资源， 如果是动态的请求,nginx就通过配置文件,将请求传递给uWSGI；
+ uWSGI 将接收到的包进行处理，并转发给wsgi；
+ wsgi根据请求调用django工程的某个文件或函数，处理完后django将返回值交给wsgi， wsgi将返回值进行打包，转发给uWSGI， uWSGI接收后转发给nginx,nginx最终将返回值返回给客户端(如浏览器)。 *注:不同的组件之间传递信息涉及到数据格式和协议的转换

## uwsgi.ini 配置文件常用选项
```
[uwsgi]
# http 或 socket ： 协议类型和端口号
socket = 127.0.0.1:9090
# 区别
# socket = 127.0.0.1:9090　　#启动端口9090的服务，需用nginx代理，可以对外提供服务。
# http-socket = 127.0.0.1:9090　　#启动端口9090的服务，可以直接对外提供服务。
processes ： 开启的进程数量
workers ： 开启的进程数量，等同于processes（官网的说法是spawn the specified number ofworkers / processes）
chdir ： 指定运行目录（chdir to specified directory before apps loading）
chdir = /app/mysit
wsgi-file ： 载入项目的wsgi-file（load .wsgi file）
wsgi-file = /usr/local/src/python-test/python-test.py  
stats ： 在指定的地址上，开启状态服务（enable the stats server on the specified address）
stats = 127.0.0.1:9191
plugins = python
threads ： 运行线程。由于GIL的存在，我觉得这个真心没啥用。（run each worker in prethreaded mode with the specified number of threads）
master ： 允许主进程存在（enable master process）
daemonize ： 使进程在后台运行，并将日志打到指定的日志文件或者udp服务器（daemonize uWSGI）。实际上最常用的，还是把运行记录输出到一个本地文件上。（肯定要启用，要不刷屏！！）
daemonize    = UWSGI.log 
pidfile ： 指定pid文件的位置，记录主进程的pid号。   （生成pid文件，以便stop uwsgi）
pidfile = 绝对路径/uwsgi.pid
vacuum ： 当服务器退出的时候自动清理环境，删除unix socket文件和pid文件（try to remove all of the generated file/sockets）
vacuum          = true
```

配置文件要点

+ uwsgi.ini配置文件在django项目总文件夹下面（注意路径）；

+ novel.conf配置文件在/etc/nginx/sites-available/下；

+ novel.conf配置文件在/etc/nginx/sites-enabled/下进行关联：ln -s /etc/nginx/sites-available/novel.conf ./novel.conf

+ setting.py在django文件下，接命令python3 manage.py collectstatic

+ mysql基础文件，libmysqld-dev需导入

+ 去隔壁服务器拿东西：ssh ubuntu@（目标内网IP）；scp novelsite.zip ubuntu@10.105.119.166（本机内网IP）:/home/ubuntu/

## Nginx配置模板 ( http=>server=>location 注意层级关系)
```
server {
listen 80;
server_name localhost; 
charset utf-8;
access_log /wwwroot/destiny/nginx_access.log; 
error_log /wwwroot/destiny/nginx_error.log;
client_max_body_size 75M;
location  /static  {
	alias /wwwroot/destiny/destiny/static;
} 
location  /  { 
    include  /etc/nginx/conf/uwsgi_params;
    uwsgi_pass 127.0.0.1:9090;
}
location /  {
	autoindex on;
    root  /wwwroot/
}
}
```
## 常用命令
```
uwsgi --ini uwsgi.ini # 启动uwsgi
uwsgi --stop uwsgi.pid # 关闭uwsgi
uwsgi.reload() # 重启uwsgi
service nginx start/status/stop
nginx -t # 检测配置文件是否错误
nginx -s reload # 热重载配置文件
tail -fn300 uwsgi.log # 滚动播放日志文件300行
netstat -tulnp # 查看端口及进程号
iftop # 查看流量监控，需安装
ps -ef|grep nginx # 查看相关功能进程
kill -9 1234 # 强制停止编号为1234的进程
```