import unittest

from pkg.firewall_class import Firewall

class FirewallTesting(unittest.TestCase):

    def test_valid_ip_address(self):
        firewall_instance = Firewall('testing.csv')

        expected_output = True
        observed_output = firewall_instance.valid_ip_address('192.168.1.1')
        self.assertEqual(expected_output, observed_output)


    def test_not_a_valid_ip_address(self):
        firewall_instance = Firewall('testing.csv')

        expected_output = False
        observed_output = firewall_instance.valid_ip_address('456.168.1.1')
        self.assertEqual(expected_output, observed_output)


    def test_valid_accept_packet(self):
        firewall_instance = Firewall('testing.csv')

        expected_output = True
        observed_output = firewall_instance.accept_packet(
            "inbound",
            "tcp",
            23,
            "192.168.1.1"
        )
        self.assertEqual(expected_output, observed_output)


    def test_not_valid_port_accept_packet(self):
        firewall_instance = Firewall('testing.csv')

        expected_output = False
        observed_output = firewall_instance.accept_packet(
            "inbound",
            "tcp",
            234567,
            "192.168.1.1"
        )
        self.assertEqual(expected_output, observed_output)


    def test_not_valid_ip_address_accept_packet(self):
        firewall_instance = Firewall('testing.csv')

        expected_output = False
        observed_output = firewall_instance.accept_packet(
            "inbound",
            "tcp",
            23,
            "456.168.1.1"
        )
        self.assertEqual(expected_output, observed_output)


    def test_not_valid_direction_accept_packet(self):
        firewall_instance = Firewall('testing.csv')

        expected_output = False
        observed_output = firewall_instance.accept_packet(
            "test",
            "tcp",
            23,
            "192.168.1.1"
        )
        self.assertEqual(expected_output, observed_output)



    def test_not_valid_protocol_accept_packet(self):
        firewall_instance = Firewall('testing.csv')

        expected_output = False
        observed_output = firewall_instance.accept_packet(
            "inbound",
            "tcpp",
            23,
            "192.168.1.1"
        )
        self.assertEqual(expected_output, observed_output)


    def test_read_csv_output(self):
        firewall_instance = Firewall('testing.csv')

        expected_output = {'{"direction": "inbound", "protocol": "tcp", "port": "80", "ip_address": "192.168.1.2"}': True,
                           '{"direction": "outbound", "protocol": "tcp", "port": "10000-20000", "ip_address": "765.168.10.11"}': False}

        observed_output = firewall_instance.read_csv()
        self.assertEqual(expected_output, observed_output)








