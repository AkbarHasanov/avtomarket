from flask import Flask, request
from telebot import types
from config import WEBHOOK_PATH
from bot.database.session import SessionLocal
from bot.bot import bot

app = Flask(__name__)

