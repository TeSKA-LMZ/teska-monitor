import psutil
import datetime
 #output = {"cpu_usage": telper, "Virtueller Ram": telmem}


def get_cpu_percent():
    pct = psutil.cpu_percent(interval=1)
    return pct


def get_cpu_temp():
    temp = psutil.sensors_temperatures()["coretemp"][0]
    return (temp.current)


def get_virtual_memory(option = "percent"):
    mem = psutil.virtual_memory()
    value = getattr(mem, option)
    return value


def get_disk_usage(option = "percent"):
    disk = psutil.disk_usage("/")
    value = getattr(disk, option)
    return value   



def get_boot_time():
    time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    return time

datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
'2014-01-12 22:51:00'    


def get_all():
    output = {
       "cpu_usage": get_cpu_percent(),
       "cpu_temperature": get_cpu_temp(),
       "total_memory": get_virtual_memory(option= "total"),
       "virtual_memory": get_virtual_memory(),
       "disk_usage": get_disk_usage(),
       "boot_time": get_boot_time()
    }

    return output    


if __name__=="__main__":
    import fire
    fire.Fire({
        "all": get_all,
        "cpu": get_cpu_percent,
        "mem": get_virtual_memory
    })


