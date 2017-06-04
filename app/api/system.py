import psutil
import platform

from flask import jsonify
from time import time

from . import api


def tuple_to_dict(namedtuple):
    dictionary = {}
    for name in namedtuple._fields:
        dictionary[name] = getattr(namedtuple, name)
    return dictionary


@api.route('/system/resources', methods=['GET'])
def get_system_resources():
    return jsonify({
        'memory': tuple_to_dict(psutil.virtual_memory()),
        'cpu': psutil.cpu_percent(percpu=True),
        'disk_memory': tuple_to_dict(psutil.disk_usage('/')),
        'network': tuple_to_dict(psutil.net_io_counters()),
        'sensors': psutil.sensors_temperatures()
    })


@api.route('/system/information', methods=['GET'])
def get_system_information():
    return jsonify({
        'sys_info': tuple_to_dict(platform.uname()),
        'current_time':  int(round(time() * 1000)),
        'up_time': psutil.boot_time()
    })
