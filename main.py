print("[INFO]: INITIALIZING")

import asyncio

import importlib

import time

import uvloop

from aiohttp import ClientSession

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from motor.motor_asyncio import AsyncIOMotorClient as Bot

from Music.config import MONGO_DB_URI as mango

from pyrogram import Client,idle

from pyrogram import Client as Bot

from Music.converter.cli import app, userbot

from Music import config

from Music.config import (

    API_HASH,

    API_ID,

    BOT_TOKEN,

    LOG_GROUP_ID,

    MONGO_DB_URI,

    OWNER_ID,

    SUDO_USERS,

)

def initialize():

    global dbb

    dbb = {}

### Mongo DB

MONGODB_CLI = Bot(mango)

db = MONGODB_CLI

pymongodb = ""

### Boot Time

boottime = time.time()

### Clients

app = app

userbot = userbot

initialize()

print("[INFO]: INITIALIZING DATABASE")

MONGODB_CLI = MongoClient(MONGO_DB_URI)

db = MONGODB_CLI.wbb

SUDOERS = SUDO_USERS

OWNER = OWNER_ID

async def load_sudoers():

    global SUDOERS

    print("[INFO]: LOADING SUDO USERS")

    sudoersdb = db.sudoers

    sudoers = await sudoersdb.find_one({"sudo": "sudo"})

    sudoers = [] if not sudoers else sudoers["sudoers"]

    for user_id in SUDOERS:

        if user_id not in sudoers:

            sudoers.append(user_id)

            await sudoersdb.update_one(

                {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True

            )

    SUDOERS = (SUDOERS + sudoers) if sudoers else SUDOERS

    print("[INFO]: LOADED SUDO USERS")

loop = asyncio.get_event_loop()

loop.run_until_complete(load_sudoers())

Music_START_TIME = time.time()

loop = asyncio.get_event_loop()

BOT_ID = 0

BOT_NAME = ""

BOT_USERNAME = ""

ASSID = 0

ASSNAME = ""

ASSUSERNAME = ""

ASSMENTION = ""

print("[INFO]: INITIALIZING BOT CLIENT")

app = Client(

    "MusicBot",

    API_ID,

    API_HASH,

    bot_token=BOT_TOKEN,

)


client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)

def all_info(app, client):

    global BOT_ID, BOT_NAME, BOT_USERNAME

    global ASSID, ASSNAME, ASSMENTION, ASSUSERNAME

    getme = app.get_me()

    getme1 = client.get_me()

    BOT_ID = getme.id

    ASSID = getme1.id

    if getme.last_name:

        BOT_NAME = getme.first_name + " " + getme.last_name

    else:

        BOT_NAME = getme.first_name

    BOT_USERNAME = getme.username

    ASSNAME = (

        f"{getme1.first_name} {getme1.last_name}"

        if getme1.last_name

        else getme1.first_name

    )

    ASSUSERNAME = getme1.username

    ASSMENTION = getme1.mention

    

def init_db():

    global db_mem

    db_mem = {}

init_db()

print("[INFO]: STARTING BOT CLIENT")

with app:
    if __name__=="__main__":
        print("done")
    idle()
    

print("[INFO]: STARTING ASSISTANT CLIENT")

with client:
    if __name__=="__main__":
        print("done")
    idle()
    
print("[INFO]: LOADING BOT/ASSISTANT PROFILE INFO")

all_info(app, client)

print("[INFO]: LOADED BOT/ASSISTANT PROFILE INFO")
