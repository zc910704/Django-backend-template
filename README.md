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
2. 