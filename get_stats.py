#!/usr/bin/env python
import psutil
import time

def get_cpu_usage():
    return str(psutil.cpu_percent()) + "%"


def get_ram_usage():
    return str(psutil.virtual_memory().percent) + "%"

def get_all_stat():
    return get_cpu_usage() + "," + get_ram_usage()

def write_to_file():
    with open("stat_client", "w") as f:
        f.write(get_all_stat())

def keep_writing():
    while True:
        time.sleep(1)
        write_to_file()