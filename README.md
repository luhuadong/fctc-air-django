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

作为 Python Web 框架，Django 需要 Python，在安装 Python 同时需要安装 pip。

（1）在线安装 Django，指定版本安装，目前 1.11 的最新版为 1.11.11

```shell
pip3 install django==1.11.11
```

默认会安装：`Django==1.11.11` 和 `pytz==2020.1`

（2）检测当前是否安装 Django 及版本

```shell
python3 -m django --version

1.11.11
```

或者使用 `pip3 freeze` 命令检查

```shell
pip3 freeze | grep Django

Django==1.11.11
```

此外，我们也可以先下载安装包，再指定安装包安装：

```shell
pip download django=1.11.11 -d ./
pip install Django-1.11.11-py2.py3-none-any.whl
```

