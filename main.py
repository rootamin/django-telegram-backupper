import os
from dotenv import load_dotenv

# Looks for the .env file in the same directory as this file
load_dotenv()

# Base directory variable
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Function to rar a directory
def rar_directory(directory_path, output_path, part_size=49):
    os.system(f"rar a -v{part_size}M {output_path} {directory_path}")

# Example usage
rar_directory('/home/rootamin/Downloads/mpv-build', f'{BASE_DIR}/backups/backup.rar')