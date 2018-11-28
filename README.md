a backend server for [https://github.com/PanJiaChen/vue-admin-template](https://github.com/PanJiaChen/vue-admin-template)

1. closed csrf verify
2. allow origin all
3. apply the api of frontend template

```

manage.py makemigrations login
python manage.py migrate
python manage.py createsuperuser


python manage.py shell


```
## 部署

1. uwsgi安装前，必须对应版本安装 libpython3.x-dev
2. 根据提示apt安装依赖clang gcc ngix, `pip install wheel setuptools`
3. `pip install django-cors-headers`

https://blog.csdn.net/qq_28018283/article/details/77333822 跨域问题解决
