from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from api.models import AirData
from api.models import TestUsers

import paramiko
import psutil

CMD = {
    'cpu_cnt_phy': 'cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l',
    'cpu_cnt_log': 'cat /proc/cpuinfo | grep "processor" | wc -l',
    'cpu_info'   : 'cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c | sed "s/^[ \t]*//g"',
    'mem_stat'   : 'free -m',
    'disk_stat'  : 'df -h'
}

# Create your views here.


def get_host_stat(request, ip4addr):

    ssh = paramiko.SSHClient()
    # 避免连接未知主机时出错
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    cmd_file = open("./static/run.py", "r")
    cmd = cmd_file.read()

    # 连接远程主机
    try:
        ssh.connect(hostname=ip4addr, username="root", timeout=4.5)
    except:
        data = "error"
    else:
        data = exec_remote_cmd(ssh, cmd)
        # 关闭连接
        ssh.close()
    finally:
        return HttpResponse(data, content_type="application/json")


def exec_remote_cmd(ssh, cmd):
    """ 执行远程命令 """

    stdin, stdout, stderr = ssh.exec_command(cmd)
    res = stdout.read().decode()
    return res


def get_latest_data(request, deviceName):
    try:
        #s = AirData.objects.get(dn=deviceName)
        s = AirData.objects.filter(dn=deviceName).last()
        data = {'dn': s.dn, 'temp': s.temp, 'humi': s.humi, 'dust': s.dust, 'tvoc': s.tvoc, 'eco2': s.eco2, 'hcho': s.hcho}
        #return HttpResponse(s)
    except:
        data = {'error': 'No data'}
    finally:
        return JsonResponse(data)
        #return HttpResponse(s, content_type="application/json")


def test(request, id):
    try:
        s = TestUsers.objects.get(id=id)
        return HttpResponse(s)
    except:
        return HttpResponse("test failed")
