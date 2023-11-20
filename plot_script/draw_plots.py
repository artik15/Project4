import matplotlib.pyplot as plot
import csv
from paramiko import SSHClient
from scp import SCPClient


RPI_FILEPATH = "/home/pi/"
RPI_FILENAME = "data.csv"
RPI_USERNAME = "pi"
RPI_PASSWORD = "raspberrypi"
RPI_IP="192.168.0.111"


def get_data():
    ssh_ob = SSHClient()
    ssh_ob.load_system_host_keys()
    ssh_ob.connect(RPI_IP, username=RPI_USERNAME, password=RPI_PASSWORD)
    scp = SCPClient(ssh_ob.get_transport())
    scp.get(RPI_FILENAME, remote_path=RPI_FILEPATH)
    scp.close()

def load_csv():
    speed = []
    time = []
    
    with open(RPI_FILEPATH, 'r') as f:
        csvreader = csv.reader(f, delimiter=',')
        for row in csvreader:
            time.append(row[0])
            speed.append(row[1])

    return time, speed

def visualize_data(data):
    (time, speed) = data
    fig, axis = plot.subplot(1,1)
    fig.plot(time, speed)
    axis[0, 0].set(xlabel="time, s", ylabel="Velocity")

if __name__ == "__main__":
    get_data()
    data = load_csv()
    visualize_data(data)