import os
import subprocess
import psycopg2
from dotenv import load_dotenv

# Looks for the .env file in the same directory as this file
load_dotenv()

# Variables:
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')



# Function to rar a directory
def rar_directory(directory_path, output_path, part_size=49):
    os.system(f"rar a -v{part_size}M {output_path} {directory_path}")

# Example usage
# rar_directory('/home/rootamin/Downloads/mpv-build', f'{BASE_DIR}/backups/backup.rar')


def get_db_dump(output_path):
    try:
        # Construct the pg_dump command
        dump_command = [
            'pg_dump',
            '-h', DB_HOST,
            '-p', DB_PORT,
            '-U', DB_USER,
            '-F', 'c',  # Custom format
            '-b',  # Include large objects
            '-v',  # Verbose mode
            '-f', output_path,  # Output file
            DB_NAME
        ]

        # Set the PGPASSWORD environment variable for the subprocess
        env = os.environ.copy()
        env['PGPASSWORD'] = DB_PASSWORD

        # Execute the pg_dump command
        subprocess.run(dump_command, env=env, check=True)
        print(f"Database dump saved to {output_path}")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while dumping the database: {e}")

# Example usage
output_file = os.path.join(BASE_DIR, 'backups', 'postgres.dumpfile')
get_db_dump(output_file)