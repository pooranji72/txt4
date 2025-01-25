#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# (c) ACE

import os

class Config(object):

    # Bot token obtained from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

    # API ID and API Hash from Telegram (get them from https://my.telegram.org/auth)
    API_ID = int(os.environ.get("API_ID", "YOUR_API_ID"))
    API_HASH = os.environ.get("API_HASH", "YOUR_API_HASH")

    # Optionally, you can add a list of authorized users (user IDs)
    # This is useful for controlling who can use the bot
    AUTH_USERS = os.environ.get("AUTH_USERS", "YOUR_USER_IDS").split(",")

    # If you have an access token for the ClassPlus API, include it here
    CLASSPLUS_ACCESS_TOKEN = os.environ.get("CLASSPLUS_ACCESS_TOKEN", "YOUR_CLASSPLUS_ACCESS_TOKEN")
    
