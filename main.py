import os
import subprocess
from dotenv import load_dotenv

import asyncio
from telegram import Bot
from telegram.error import TelegramError

# Looks for the .env file in the same directory as this file
load_dotenv()

# Variables:
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MEDIA_DIR = os.getenv('MEDIA_DIR')

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


# Function to rar a directory
def rar_directory(directory_path, output_path, part_size=49):
    os.system(f"rar a -v{part_size}M {output_path} {directory_path}")

# Example usage
# rar_directory('/home/rootamin/Downloads/mpv-build', f'{BASE_DIR}/backups/backup.rar')



# A function to dump the PostgreSQL database
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
# output_file = os.path.join(BASE_DIR, 'backups', 'postgres.dumpfile')
# get_db_dump(output_file)



# Telegram Section
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Function to send and delete files in a directory. Use it with asyncio.run()
async def send_and_delete_files(directory_path):
    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    await bot.send_document(chat_id=CHAT_ID, document=f)
                    print(f"Sent {file_path} to Telegram chat {CHAT_ID}")
                os.remove(file_path)
                print(f"Deleted {file_path}")
    except TelegramError as e:
        print(f"Error occurred while sending file: {e}")
    except OSError as e:
        print(f"Error occurred while deleting file: {e}")

# Example usage
# asyncio.run(send_and_delete_files('/home/rootamin/Downloads/YekanV3.0'))