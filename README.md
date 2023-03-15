# code-stats.py
A recreation of Code::Stats in Python

# About
Trying to install [Code::Stats](https://codestats.net) on my server resulted in many errors. The setup process was quite complicated and having no experience with Elixir did not help the situation.

Looking at the API docs, I decided to create my own implementation of Code::Stats in a language I knew better: Python. So I implemented a very simple Django API as a backend for Code::Stats plugins.

# Requirements
Should work with Python 3.8 or newer.

Tested on Python 3.11.
It might also work with older Python versions. Feel free to try one and give me feedback on it!

Older versions of Django newer than 4.0 will also work.

# Installation
1. Clone the repository
    ```
    git clone https://github.com/hex-developer/code-stats.py.git
    ```
2. 
    ```
    cd code-stats.py/
    ```
3. Install dependencies
    ```
    pip3 install -r requirements.txt
    ```
4. Setup the database
    ```
    python3 manage.py migrate
    python3 manage.py createsuperuser
    ```
5. Run the server
    ```
    python3 manage.py runserver 0.0.0.0:8000
    ```
    Keep in mind that you can change the port
6. Log in to the admin interface and set it up according to your needs
    1. Navigate to the /admin url at the address you are hosting your server.<br>
    Example: http://127.0.0.1:8000/admin
    2. Log in with the username and password you used when setting up the database
    3. Create a machine with the name you want and copy your token. You can do this as many times as you want to.
    4. Log out
7. Setup your plugins with the following information:
    - The token for your machine
    - Your username
    - The address of your server with /api: http://127.0.0.1:8000/api

You are now ready to use your server!


# Contributing
All contributions are welcome!

Before opening an issue, make sure you have tested the problem with Python 3.11 and Django 4.1.7 installed, because you might have outdated versions.

# Plugins
You can find plugins from the official Code::Stats website [here](https://codestats.net/plugins).
Also I recommend the bash plugin [here](https://github.com/Freed-Wu/code-stats-bash)
