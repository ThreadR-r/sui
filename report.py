#!/usr/bin/python

import os
import datetime
import sys
import platform
import socket
import json

def pinghost(hostname):
    # Check os type to determine which ping command to use
    os_type = platform.platform()
    if "Windows" in os_type:
        response = os.system("ping -n 1 {0}".format(hostname))
    else:
        response = os.system("ping -c 1 {0}".format(hostname))
    return True if response == 0 else False

def checksock(hostname, port):
    if not isinstance(port, int):
        try:
            port = int(port)
        except ValueError:
            print('Port number is not numeric!')
            sys.exit()
    try:
        socket.create_connection((hostname, port), 2)
        return True
    except socket.error:
        print('%s failed on port: %s' % (hostname, str(port)))
        return False

def parsehost(hostfile):
    servers = []
    with open(hostfile, "r") as f:
        data = json.load(f)
        for item in data["apps"]:
                print(item)
                if not isinstance(item["port"], int):
                    print("%s Port: %s is not a number!" % (item["name"], item["port"]))
                    sys.exit()

                if item["hostname"]:
                    servers.append({"hostname": item["hostname"], "port": item["port"], "name": item["name"], "href": item["href"], "icon": item["icon"]})
                else:
                    servers.append({"hostname": "127.0.0.1", "port": item["port"], "name": item["name"], "href": item["href"], "icon": ite["icon"]})
    return servers

def updateInformations(output, host_dict):
    apps={"apps":host_dict}
    json.dumps(apps, sort_keys=True, indent=4)
    try:
        file_object = open(output, 'w')
        json.dump(apps, file_object)
    except FileNotFoundError:
        print(output + " not found. ")

def main():
    names_list = "apps.json"
    hosts = parsehost(names_list)
    for h in hosts:
        if h.get("port"):
            alive = checksock(h.get("hostname"), h.get("port"))
        else:
            alive = pinghost(h.get("hostname"))
        if alive:
            h.update(status="green")
        else:
            h.update(status="red")
    updateInformations(names_list, hosts)

if __name__ == "__main__":
    main()
