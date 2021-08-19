from flask import Flask
from teska_monitor import telemetry

app = Flask(__name__)


TEMPLATE ="""
<h1>Monitoring</h1>
<p><strong>CPU_Nutzung: </strong>{cpu}</p>
<p><strong>Virtueller Ram: </strong>{mem}</p>
"""

@app.route("/")
def index():
   
    telper = telemetry.get_cpu_percent()
    telper = str(telper)

    telmem = telemetry.get_virtual_memory()
    telmem = str(telmem)    
   

    return TEMPLATE.format(cpu=telper, mem=telmem)


@app.route("/json")
def show_json():
    telper = telemetry.get_cpu_percent()  
    telmem = telemetry.get_virtual_memory()  
    output = {"cpu_usage": telper, "Virtueller Ram": telmem}

    return output

if __name__=="__main__":
    app.run(debug = True)    