import os
import optparse
import socket


class NetScan(object):
    """ NetScan object.
    Contains methods that facilitate
    network scanning and analysis.
    """

    @classmethod
    def conn_scan(self, target_host, target_port, verbose=False):
        """ Attempts to connect to a specific port
        on a target host and returns true if the port is open.
        """
        try:
            conn_socket = socket.socket(AF_INET, SOCK_STREAM)
            conn_socket.connect((target_host, target_port))
            send = 'Hello'
            conn_socket.send(send)
            results = conn_socket.recv(100)
            message = '[+] TCP open: {}\n[+] Results: {}'
            self._vprint(message.format(target_port, results), verbose)
            conn_socket.close()
            return True
        except:
            message = '[-] TCP closed: {}'
            self._vprint(message.format(target_port), verbose)
            return False

    @classmethod
    def port_scan(self, target_host, target_ports, verbose=False):
        """ Runs a scan on all specified ports of
        a target host.
        """
        try:
            target_ip = socket.gethostbyname(target_host)
        except:
            message = '[-] Cannot resolve {}: Unknown host'.format(target_host)
            self._vprint(message, verbose)
            return

        message = '[+] Scan results for: {}\n'
        try:
            target_name = socket.gethostbyaddr(target_ip)
            self._vprint(message.format(target_name[0]), verbose)
        except:
            self._vprint(message.format(target_ip), verbose)

        socket.setdefaulttimeout(1)
        return [port for port in target_ports if self.conn_scan(target_host,
                                                                int(port),
                                                                verbose)]

    def _vprint(data, verbose=True):
        if verbose:
            print(data)
