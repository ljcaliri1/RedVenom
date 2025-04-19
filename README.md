# RedVenom

**RedVenom** is a modular exploitation framework built by Red Halo for ethical hacking simulations and educational red team ops, It features flexible CLI interface, plug-and-play modules, and simulated attack capabilites.




## Overview 
RedVenom is a terminal-based payload launcher designed to simulate real-world attack chains in a safe, educational envirionment. It features custom payload generation, module-based execution, and encoded shell command support - perfect for red team practice, tool development, and portfolio showcasing.


## Features
- Modular exploit launcher with simulated payloads
- Payload helper with encoding and obfuscation options
- Command-line interface built with argparse
- Directory structure for expansion


## Requirements
- Python 3.10+
- pip
- Modules listend in 'requirements.txt'

Install with:
```bash
pip install -r requirements.txt


---
### **5. Running the Tool**
```markdown

## Payload System Overview

The `payload_helper.py` module contains reusable payload definitions, descriptions, and simulation logic.

### Available Payload Types:
-`reverse_shell`: Simulates a Bash reverse shell payload
- `bind_shell`: Simulates a netcat bind shell
- `custom_payload`: Demonstrates a user-defined shell command

These can be triggered via `redvenom.py` or `exploit_launcher.py` with:

```bash
python redvenom.py --module reverse_shell --target 127.0.0.1

---
### File Structure
RedVenom/
├── LICENSE                    # MIT License
├── README.md                  # Project documentation
├── redvenom.py                # Main exploit launcher entry point
├── exploit_launcher.py        # Original launcher script (legacy or modular core)
├── requirements.txt           # Python dependencies
├── utils/
│   └── payload_helper.py      # Simulated payloads and helper functions
└── modules/
    ├── exploit_ftp.py         # Placeholder or future FTP-based exploit module
    └── exploit_http.py        # Placeholder or future HTTP-based exploit module

---
## License

This project is licensed under the [MIT License](LICENSE).


## Disclaimer
this project is for **educational purposes only.** Use only on system you own or have explicit permission to test


 
