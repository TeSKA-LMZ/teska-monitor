from flask import Flask
import telemetry

app = Flask(__name__)


TEMPLATE ="""
<h1>Monitoring</h1>
<p><strong>CPU Nutzung: </strong>{cpu}%</p>
<p><strong>Virtual Memory: </strong>{mem}%</p>
<p><strong>Total Memory: </strong>{total} GB</p>
"""

@app.route("/")
def index():
   
    # telper = telemetry.get_cpu_percent()
    # telper = str(telper)

    # telmem = telemetry.get_virtual_memory()
    # telmem = str(telmem)    
   
    data = telemetry.get_all()

    total = data["total_memory"]
    total_gb = round(total / 1024 / 1024 / 1024, 2)
    
    return TEMPLATE.format(cpu=data["cpu_usage"], mem=data["virtual_memory"], total=total_gb)


@app.route("/json")
def show_json():
    # telper = telemetry.get_cpu_percent()  
    # telmem = telemetry.get_virtual_memory()  
    # output = {"cpu_usage": telper, "Virtueller Ram": telmem}

    output = telemetry.get_all()

    return output

if __name__=="__main__":
    app.run(debug = True)    