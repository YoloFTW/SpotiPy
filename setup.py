import subprocess
import os

# Define the path to the requirements.txt file
req_file_path = "./requirements.txt"

# Use subprocess to run pip to install the requirements
subprocess.check_call(["pip", "install", "-r", req_file_path])

# Rename the .envTmp file to .env
env_temp_file = "./.envTmp"
os.rename(env_temp_file, ".env")