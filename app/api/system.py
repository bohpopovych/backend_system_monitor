import psutil
import platform

from time import time
from flask import jsonify
from flask_cors import cross_origin

from . import api


def tuple_to_dict(namedtuple):
    dictionary = {}

    for name in namedtuple._fields:
        dictionary[name] = getattr(namedtuple, name)
    return dictionary


def set_id_to_cpu(list):
    new_list = []
    count = 0

    for item in list:
        count += 1

        new_list.append({'id': count, 'load': item})
    return new_list


def sensors_data_compact(dict):
    new_list = []
    count = 0

    for item in dict:

        for i, value in enumerate(dict[item]):
            count += 1
            
            new_list.append({'id': count, 'name': dict[item][i][0], 'temp': dict[item][i][1]})
    return new_list


@api.route('/system/resources', methods=['GET'])
@cross_origin(origin="*")
def get_system_resources():
    return jsonify({
        'memory': tuple_to_dict(psutil.virtual_memory()),
        'cpu': set_id_to_cpu(psutil.cpu_percent(percpu=True)),
        'disk_memory': tuple_to_dict(psutil.disk_usage('/')),
        'network': tuple_to_dict(psutil.net_io_counters()),
        'sensors': sensors_data_compact(psutil.sensors_temperatures())
    })


@api.route('/system/information', methods=['GET'])
@cross_origin(origin="*")
def get_system_information():
    return jsonify({
        'sys_info': tuple_to_dict(platform.uname()),
        'current_time':  int(round(time())),
        'up_time': psutil.boot_time()
    })
