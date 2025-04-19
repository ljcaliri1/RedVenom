# RedVenom

**RedVenom** is a modular exploitation framework built by Red Halo for ethical hacking simulations and educational red team ops, It features flexible CLI interface, plug-and-play modules, and simulated attack capabilites.


## Features
- Modular exploit loader (`-m http`, `-m ftp`, etc.)
- Clean comman-line inferface
- ASCII banner via `pyfiglet`
- Simulated SQL injection exploit with realistic output
- Easily extendable module system

## Usage
```bash
python redvenom.py -t <target_ip> -m <module>

### Example
python redvenom.py -t 127.0.0.1 -m http


## License

This project is licensed under the [MIT License](LICENSE).


## Disclaimer
this project is for **educational purposes only.** Use only on system you own or have explicit permission to test


 
