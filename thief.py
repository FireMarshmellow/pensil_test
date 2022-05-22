#   __  __      _ _               ______ _
#  |  \/  |    | | |             |  ____(_)
#  | \  / | ___| | | _____      _| |__   _ _ __ ___
#  | |\/| |/ _ \ | |/ _ \ \ /\ / /  __| | | '__/ _ \
#  | |  | |  __/ | | (_) \ V  V /| |    | | | |  __/
#  |_|  |_|\___|_|_|\___/ \_/\_/ |_|    |_|_|  \___|
#  https://www.mellowfire.com/
#  https://github.com/FireMarshmellow/Pentest-V1
import speedtest
import os
import socket
import multiprocessing
import subprocess
import smtplib, ssl
from requests import get

# pings all systems on network
def pinger(job_q, results_q):
    DEVNULL = open(os.devnull, "w")
    while True:
        ip = job_q.get()

        if ip is None:
            break

        try:
            subprocess.check_call(["ping", "-c1", ip], stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass


def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


# maps local network
def map_network(pool_size=255):
    ip_list = list()

    # get my IP and compose a base like 192.168.1.xxx
    ip_parts = get_my_ip().split(".")
    base_ip = ip_parts[0] + "." + ip_parts[1] + "." + ip_parts[2] + "."

    # prepare the jobs queue
    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [
        multiprocessing.Process(target=pinger, args=(jobs, results))
        for i in range(pool_size)
    ]

    for p in pool:
        p.start()

    # cue hte ping processes
    for i in range(1, 255):
        jobs.put(base_ip + "{0}".format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    # collect he results
    while not results.empty():
        ip = results.get()
        ip_list.append(ip)

    return ip_list


# gets wifi_name local_ip public_ip system_info
def extract_ip():
    #ssid = os.popen("sudo iwgetid -r").read()
    puip = get("https://api.ipify.org").content.decode("utf8")
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(("10.255.255.255", 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        st.close()

    #wifiname = "Wifi_name: " + ssid <--- linux only
    wifiname = 'no wifi name'
    localip = "Pi0_ip: " + IP
    publicip = "public IP: " + puip
    #system = "System info: ", os.uname() <--- linux only
    system = 'OS'
    return (
        wifiname,
        localip,
        publicip,
        system,
    )


### this is too powerfal for the pi zero ###
def scrap_network():
    print('Mapping...') #DEBUG
    print('list of IPs on network', map_network()) #DEBUG
    return "list of IPs on network", map_network()


def get_info():
    print('geting info') #DEBUG
    print(extract_ip()) #DEBUG
    return extract_ip()


# tests network speed
def speed_test():
    s = speedtest.Speedtest()
    down = "download speed is:", s.download()
    up = "upload speed is:", s.upload()
    return down, up