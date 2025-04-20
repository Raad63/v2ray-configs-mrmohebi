import pybase64
import base64
import requests
import binascii
import os
from settings.setting import SETTINGS
from constants.content_manager import ContentManager
from utils import *

TIMEOUT = SETTINGS['timeout']

def filter_for_protocols(data, protocols):
    filtered_data = []
    for line in data:
        if any(protocol in line for protocol in protocols):
            filtered_data.append(line)
    return filtered_data

def ensure_directories_exist():
    output_folder = os.path.abspath(os.path.join(os.getcwd(), "../configs"))
    base64_folder = os.path.join(output_folder, "Base64")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if not os.path.exists(base64_folder):
        os.makedirs(base64_folder)

    return output_folder, base64_folder

def main():
    output_folder, base64_folder = ensure_directories_exist() 

    protocols = SETTINGS['sources']['protocols']
    files =SETTINGS['sources']['files']
    dirs = SETTINGS['sources']['dirs']

    decoded_files = decode_files_links(files)
    decoded_dirs = decode_dirs_links(dirs)

    combined_data = decoded_files + decoded_dirs
    merged_configs = filter_for_protocols(combined_data, protocols)

    # Clean existing output files
    output_filename = os.path.join(output_folder, "All_Configs_Sub.txt")
    filename1 = os.path.join(output_folder, "All_Configs_base64_Sub.txt")
    
    if os.path.exists(output_filename):
        os.remove(output_filename)
    if os.path.exists(filename1):
        os.remove(filename1)

    for i in range(20):
        filename = os.path.join(output_folder, f"Sub{i}.txt")
        if os.path.exists(filename):
            os.remove(filename)
        filename1 = os.path.join(base64_folder, f"Sub{i}_base64.txt")
        if os.path.exists(filename1):
            os.remove(filename1)

    # Write merged configs to output file
    with open(output_filename, "w") as f:
        f.write(ContentManager.get_v2ray())
        for config in merged_configs:
            f.write(config + "\n")

    # Split merged configs into smaller files (no more than 600 configs per file)
    with open(output_filename, "r") as f:
        lines = f.readlines()

    num_lines = len(lines)
    max_lines_per_file = 600
    num_files = (num_lines + max_lines_per_file - 1) // max_lines_per_file

    for i in range(num_files):
        profile_title = f"🆓 Git:Barry-far | Sub{i+1} 🫂"
        encoded_title = base64.b64encode(profile_title.encode()).decode()
        custom_fixed_v2ray = ContentManager.get_v2ray(encoded_title)

        input_filename = os.path.join(output_folder, f"Sub{i + 1}.txt")
        with open(input_filename, "w") as f:
            f.write(custom_fixed_v2ray)
            start_index = i * max_lines_per_file
            end_index = min((i + 1) * max_lines_per_file, num_lines)
            for line in lines[start_index:end_index]:
                f.write(line)

        with open(input_filename, "r") as input_file:
            config_data = input_file.read()
        
        output_filename = os.path.join(base64_folder, f"Sub{i + 1}_base64.txt")
        with open(output_filename, "w") as output_file:
            encoded_config = base64.b64encode(config_data.encode()).decode()
            output_file.write(encoded_config)

if __name__ == "__main__":
    main()