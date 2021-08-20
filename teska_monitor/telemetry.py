import psutil
from teska_monitor import db

 #output = {"cpu_usage": telper, "Virtueller Ram": telmem}


def get_cpu_percent():
    pct = psutil.cpu_percent(interval=1)
    return pct
    

def get_virtual_memory(option = "percent"):
    mem = psutil.virtual_memory()
    value = getattr(mem, option)
    return value


def get_all(save=False, **kwargs):
    """Returns the current telemetry data
    :param save: If True, the telemetry data will be written into the database 
    :param kwargs: Additional params sent to db
    """
    output = {
       "cpu_usage": get_cpu_percent(),
       "total_memory": get_virtual_memory(option= "total"),
       "virtual_memory": get_virtual_memory()
    }

    # save if needed
    if save:
        db.save(**kwargs, **output)

    return output    


if __name__=="__main__":
    import fire
    fire.Fire({
        "all": get_all,
        "cpu": get_cpu_percent,
        "mem": get_virtual_memory
    })


