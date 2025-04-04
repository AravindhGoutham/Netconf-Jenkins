#!/usr/bin/env python3

import unittest
from netmiko import ConnectHandler
from getpass import getpass

# Router login credentials
username = 'lab'
password = 'lab123'

# Devices
devices = {
    'R1': {'device_type': 'cisco_ios', 'host': '198.51.100.11', 'username': username, 'password': password},
    'R2': {'device_type': 'cisco_ios', 'host': '198.51.100.12', 'username': username, 'password': password},
    'R3': {'device_type': 'cisco_ios', 'host': '198.51.100.13', 'username': username, 'password': password},
    'R4': {'device_type': 'cisco_ios', 'host': '198.51.100.14', 'username': username, 'password': password},
    'R5': {'device_type': 'cisco_ios', 'host': '198.51.100.15', 'username': username, 'password': password},
}


class TestNetconf(unittest.TestCase):

    def test_loopback_ip_r3(self):
        print("[TEST] Checking Loopback99 IP on Router R3")
        connection = ConnectHandler(**devices['R3'])
        output = connection.send_command("show run interface Loopback99")
        connection.disconnect()

        if "10.1.3.1 255.255.255.0" in output:
            print("[PASS] R3 Loopback99 is configured with 10.1.3.1/24")
        else:
            print("[FAIL] R3 Loopback99 is NOT configured with 10.1.3.1/24")
        self.assertIn("10.1.3.1 255.255.255.0", output)

    def test_single_area_r1(self):
        print("[TEST] Checking if R1 is in only one OSPF area")
        connection = ConnectHandler(**devices['R1'])
        output = connection.send_command("show run | section router ospf")
        connection.disconnect()

        area_lines = [line for line in output.splitlines() if "area" in line]
        areas = [line.strip().split()[-1] for line in area_lines if "network" in line]

        unique_areas = set(areas)
        if len(unique_areas) == 1:
            print(f"[PASS] R1 is configured for a single OSPF area: {unique_areas}")
        else:
            print(f"[FAIL] R1 has multiple OSPF areas: {unique_areas}")
        self.assertEqual(len(unique_areas), 1, f"R1 has multiple OSPF areas: {unique_areas}")

    def test_ping_r2_to_r5(self):
        print("[TEST] Pinging from R2's Loopback to R5's Loopback")
        connection = ConnectHandler(**devices['R2'])
        output = connection.send_command("ping 10.1.5.1")
        connection.disconnect()

        if "Success rate is 100 percent" in output:
            print("[PASS] Ping from R2 to R5 is successful")
        else:
            print("[FAIL] Ping from R2 to R5 failed")
        self.assertIn("Success rate is 100 percent", output, "Ping from R2 to R5 failed")


if __name__ == "__main__":
    unittest.main()
