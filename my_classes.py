import dbl
import discord
from discord.ext import commands

import asyncio
import requests
import logging

class cmd():
    cmd_name = dict()
    cmd_func = dict()
    
    def add_command(name, key, func):
        cmd_name[name] = key
        cmd_func[func] = func
    
    def run_cmd(name):
        return cmd_func[name]()
    
    def run_str(val):
        for i in cmd_name:
            if cmd_name[i] == val:
                return [i, run_cmd(i)]