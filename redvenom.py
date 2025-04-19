#!/usr/bin/env python3
#!/usr/bin/env python3


import argparse
import sys
from modules import exploit_http, exploit_ftp #Placeholder modules

# CLI Banner
def banner():
    try:
        import pyfiglet
        ascii_banner = pyfiglet.figlet_format("RedVenom")
        print(ascii_banner)
        print("Red Halo - Exploitation Framework")
        print("Built for ethical operations | Stay White Hat\n")
    except ImportError:
        print("RedVenom - Red Halo Exploitation Framework")

# Argument parser

def parse_args():
    parser = argparse.ArgumentParser(
        prog="RedVenom",
        description="RedVenom - A modular exploitaion framework by Red Halo."
    )
    parser.add_argument("-t", "--target", help="Target IP or domain", required=True)
    parser.add_argument("-m", "--module", help="Exploit module to use", required=True)
    return parser.parse_args()

# Exploit module loader (stub)
def load_module(name, target):
    print(f"[+] Loading RedVenom module: {name}")
    if name == "http":
        exploit_http.run(target)
    elif name == "ftp":
        exploit_ftp.run(target)
    else:
        print(f"[-] Module '{name}' not found.")
        sys.exit(1)

# Main Entry
def main():
    banner()
    args = parse_args()
    load_module(args.module, args.target)

if __name__ == "__main__":
    main()
