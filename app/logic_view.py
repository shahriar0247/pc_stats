from app import app

filename = "stat_server"

@app.route("/get_cpu_usage")
def get_cpu_usage():
    with open(filename, "r") as f:
        cpu_usage = f.readline().split(",")[0]
    return cpu_usage

@app.route("/get_ram_usage")
def get_ram_usage():
    with open(filename, "r") as f:
        ram_usage = f.readline().split(",")[1]
    return ram_usage