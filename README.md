# fctc-air-django
Web backend for FCTC-Air project



## 环境搭建

### 安装 Python 虚拟环境

以 Ubuntu 为例，安装虚拟环境

```shell
sudo apt-get install python3-venv
```

创建虚拟环境

```shell
python3.7 -m venv py37-venv
```

激活虚拟环境

```shell
source py37-venv/bin/activate
```

关闭虚拟环境

```shell
deactivate
```



### 安装 Django

进入虚拟环境，安装 Django。

（1）在线安装 Django，指定版本安装，目前 2.2 LTS 的最新版为 2.2.16

```shell
pip install Django==2.2.16
```

默认会安装：`Django==2.2.16` 和 `pytz==2020.1`

（2）检测当前是否安装 Django 及版本

```shell
python -m django --version

2.2.16
```

或者使用 `pip freeze` 命令检查

```shell
pip freeze | grep Django

Django==2.2.16
```

此外，我们也可以先下载安装包，再指定安装包安装：

```shell
pip download django=2.2.16 -d ./
pip install Django-2.2.16-py2.py3-none-any.whl
```



### 创建项目

```shell
django-admin startproject webserver
```



### 运行项目

```shell
python manage.py runserver
```



### 创建应用

```shell
python manage.py startapp devices
```

