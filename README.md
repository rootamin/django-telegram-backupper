# A Tool For Backing Up Django Website Contents

## Introduction
This tool is designed to backup the contents of a Django website. It is a command line tool that can be run on a server to backup the contents of a Django website, such as media folder and it's database. The tool will backup the contents of the website to a specified directory on the server, upload it via a Telegram bot to an specified chat id and then remove the backup directory to preserve space on the server. By setting an interval, the tool can be run periodically to ensure that the website contents are regularly backed up.

It also compresses the backed up files in rar parts in order to bypass Telegrams upload limit on bots.

## Installation
#### Note that this tool is designed to be run on a linux server. You can also run it on a Windows machine, but you will need to install the necessary dependencies and make some modifications to the code.


To install the tool, you will need to download the source code from the GitHub repository. You can do this by running the following command in your terminal:
```
git clone https://github.com/rootamin/django-telegram-backupper.git
cd django-telegram-backupper
```

Now you need to install the required dependencies. You can do this by running the following command in your terminal. Use other package managers if you are not using apt:
```
sudo apt-get install rar unrar
```
Now you need to install the required python packages. You can do this by running the following command in your terminal:
```
pip install -r requirements.txt
```


## Configuration
You have to specify some variables in the .env file in order to run the tool. This is a template for this project. You can copy it and fill in the necessary values:
```
# Media folder path
MEDIA_DIR=/path/to/your/media/folder

# Database configuration
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

# Get the Telegram token from @BotFather
TELEGRAM_BOT_TOKEN=your_telegram_bot_token

# Get your chat id from @userinfobot it's an integer
CHAT_ID=your_chat_id

# This is in hours
BACKUP_INTERVAL=72
```


## Usage
To simply just running the tool, you can use the following command in your terminal:
```
python main.py
```
Note that the .env file has to be in the same directory as the main.py file.


## Running in the background
We have to create a systemd service in order to run the tool in the background. You can do this by creating a file in the /etc/systemd/system/ directory with the following content:
```
sudo nano /etc/systemd/system/django-backupper.service
```

Write the following template and modify the paths to your own paths:
```
[Unit]
Description=Django Backupper Service
After=network.target

[Service]
User=root
WorkingDirectory=/path/to/your/django-telegram-backupper
ExecStart=/usr/bin/python3 /path/to/your/django-telegram-backupper/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```
Now activate the service by running the following commands:
```
sudo systemctl enable django-backupper.service
sudo systemctl start django-backupper.service
```

Now the tool will run in the background and backup your website contents periodically.

# Final Notes
This tool is designed to be run on a linux server. You can also run it on a Windows machine, but you will need to install the necessary dependencies and make some modifications to the code. If you have any questions or issues, feel free to open an issue on the GitHub repository.

Be sure to configure the .env file correctly, otherwise the tool will not work as expected.

Make sure to have at least 2 times the size of your media folder in free space on your server, because the tool will compress the files in rar parts and then upload them to Telegram. This will require some additional space on your server.