import csv
import json

from typing import Dict

class Firewall():

    def __init__(self, path_to_file: str):
        self.path_to_file = path_to_file


    def valid_ip_address(self, ip_address: str) -> bool:
        """Returns boolean values on checking ip address validity"""
        list_new = ip_address.split('.')

        if len(list_new) != 4:
            return False

        for i in list_new:
            if not i.isdigit():
                return False
            if int(i) < 0 or int(i) > 255:
                return False

        return True


    def valid_ip_range(self, ip_address_range: str) -> bool:
        """Return boolean value on checking ip address range validity"""
        list_ip_ranges = ip_address_range.split('-')

        for ip in list_ip_ranges:
            if not self.valid_ip_address(ip):
                return False

        return True


    def accept_packet(self,
                      direction: str,
                      protocol: str,
                      port: int,
                      ip_address: str) -> bool:
        """Return boolean value checking rules for all four arguments"""

        if direction != 'inbound' and direction != 'outbound':
            return False

        if protocol != 'tcp' and protocol != 'udp':
            return False

        if int(port) < 1 or int(port) > 65535:
            return False

        if not self.valid_ip_address(ip_address):
            return False

        return True


    def read_csv(self) -> Dict[str, bool]:
        """Read csv file using dict reader and output a dict object"""
        final_result = {}
        try:
        with open(self.path_to_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if "-" in row['port']:
                    list_ports = row['port'].split('-')

                if "-" in row['ip_address']:
                    list_ips = row['ip_address'].split('-')

                if "-" in row['port'] and "-" in row['ip_address']:
                    a = self.accept_packet(row['direction'],
                                   row['protocol'],
                                   list_ports[0],
                                   list_ips[0])
                    b = self.accept_packet(row['direction'],
                                   row['protocol'],
                                   list_ports[1],
                                   list_ips[1])
                    c = self.accept_packet(row['direction'],
                                   row['protocol'],
                                   list_ports[0],
                                   list_ips[1])
                    d = self.accept_packet(row['direction'],
                                   row['protocol'],
                                   list_ports[1],
                                   list_ips[0])


                    key = json.dumps(row)
                    if not a or not b or not c or not d:
                        final_result[key] = False
                    else:
                        final_result[key] = True

                if "-" in row['port'] and "-" not in row['ip_address']:
                    a = self.accept_packet(row['direction'],
                                   row['protocol'],
                                   list_ports[0],
                                   row['ip_address'])
                    b = self.accept_packet(row['direction'],
                                   row['protocol'],
                                   list_ports[1],
                                   row['ip_address'])

                    key = json.dumps(row)
                    if not a or not b:
                        final_result[key] = False
                    else:
                        final_result[key] = True

                if "-" not in row['port'] and "-" in row['ip_address']:
                    a = self.accept_packet(row['direction'],
                                   row['protocol'],
                                   row['port'],
                                   list_ips[0])
                    b = self.accept_packet(row['direction'],
                                   row['protocol'],
                                   row['port'],
                                   list_ips[1])


                    key = json.dumps(row)
                    if not a or not b:
                        final_result[key] = False
                    else:
                        final_result[key] = True

                if "-" not in row['port'] and "-" not in row['ip_address']:
                    key = json.dumps(row)
                    if not self.accept_packet(row['direction'],
                                   row['protocol'],
                                   row['port'],
                                   row['ip_address']):
                        final_result[key] = False
                    else:
                        final_result[key] = True

        return final_result





