#!/usr/bin/env python3
import os
import json
import base64
from typing import List, Dict, Any

def load_latest_configs() -> Dict[str, List[Dict[Any, Any]]]:
    """Load the latest configurations for each protocol."""
    configs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configs')
    configs = {}
    
    for filename in os.listdir(configs_dir):
        if filename.endswith('_latest.json'):
            protocol = filename.replace('_latest.json', '')
            with open(os.path.join(configs_dir, filename)) as f:
                configs[protocol] = json.load(f)
    
    return configs

def generate_subscription_content(configs: List[Dict[Any, Any]]) -> str:
    """Generate base64 encoded subscription content."""
    # Convert configs to V2Ray URI format
    uris = []
    for config in configs:
        protocol = config['protocol']
        if protocol in ['vmess', 'vless', 'trojan', 'ss']:
            uri = f"{protocol}://"
            if 'id' in config:
                uri += config['id']
            uri += f"@{config['server']}:{config['port']}"
            if 'path' in config:
                uri += config['path']
            uris.append(uri)
    
    # Join URIs with newlines and encode
    content = '\n'.join(uris)
    return base64.b64encode(content.encode()).decode()

def main():
    """Main function to generate subscription files."""
    configs = load_latest_configs()
    subs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'subscriptions')
    os.makedirs(subs_dir, exist_ok=True)
    
    # Generate protocol-specific subscriptions
    for protocol, protocol_configs in configs.items():
        content = generate_subscription_content(protocol_configs)
        with open(os.path.join(subs_dir, f"{protocol}.txt"), 'w') as f:
            f.write(content)
    
    # Generate all-in-one subscription
    all_configs = []
    for configs in configs.values():
        all_configs.extend(configs)
    
    content = generate_subscription_content(all_configs)
    with open(os.path.join(subs_dir, "all.txt"), 'w') as f:
        f.write(content)

if __name__ == "__main__":
    main() 