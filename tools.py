import psutil

def get_cpu_times():
    cpu_times = psutil.cpu_times()
    cpu_times_info = {
        "user":cpu_times.user,
        "system":cpu_times.system,
        "idle":cpu_times.idle,
        "interrupt":cpu_times.interrupt,
        "dpc":cpu_times.dpc,
    }
    return cpu_times_info

def get_cpu_count():
    cpu_count = psutil.cpu_count()
    return cpu_count

def get_virtual_memory():
    virtual_memory = psutil.virtual_memory()
    virtual_memory_info = {
        "total":virtual_memory.total,
        "available":virtual_memory.available,
        "percent":virtual_memory.percent,
        "used":virtual_memory.used,
        "free":virtual_memory.free,
    }
    return virtual_memory_info

def get_swap_memory():
    swap_memory = psutil.swap_memory()
    swap_memory_info = {
        "total":swap_memory.total,
        "used":swap_memory.used,
        "free":swap_memory.free,
        "percent":swap_memory.percent,
        "sin":swap_memory.sin,
        "sout":swap_memory.sout,
    }
    return swap_memory_info

def getloadavg():
    getloadavg = psutil.getloadavg()
    return getloadavg