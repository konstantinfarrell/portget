from netscan import NetScan


def clear(n=100):
    print('\n'*n)


if __name__ == '__main__':

    target_host = '127.0.0.1'
    target_ports = [20, 21, 80, 220, 3096, 3306, 8000, 8080, 5000, 5050, 4000, 4040]

    clear()
    ports = NetScan.port_scan(target_host, target_ports, True)
    #print([port for port in ports])
