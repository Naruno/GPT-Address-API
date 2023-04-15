#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from naruno.apps.remote_app import Integration

from naruno.lib.encryption import encrypt, decrypt

import time
import fire
import pickle
import contextlib


import openai

class gptaapi:
    command_line = False
    def __init__(self, password,  encrypt_key=None, api_key=None, timeout=180, trusted_users=[], port=8000):
        self.encrypt_key = encrypt_key
        self.trusted_users = trusted_users
        self.integration = Integration("GPTAAPI", password=password, port=port)
        self.timeout = timeout + self.integration.wait_amount
        self.api_key = api_key
        openai.api_key = self.api_key




    
    def ask(self, user, message, encrypt_key):

        self.integration.send("message", message, user)
        start_time = time.time()
        while True:
            if time.time() - start_time > self.timeout:
                return "Timeout"
            data = self.integration.get()
            if data != []:
                for each in data:
                    if each["fromUser"] == user:
                        if time.time() - each["transaction_time"] < self.timeout:
                            if gptaapi.command_line:
                                self.close()
                            return decrypt(each["data"]["app_data"], encrypt_key)
            time.sleep(5)


    
    def add_user(self, user):
        self.trusted_users.append(user)

    def set_api_key(self, api_key):
        self.api_key = api_key

    def set_encrypt_key(self, encrypt_key):
        self.encrypt_key = encrypt_key

    def run(self):
        if self.api_key == None:
            raise Exception("API Key not provided")
        if self.encrypt_key == None:
            raise Exception("Encryption Key not provided")
        while True:
            data = self.integration.get()
            if data != []:
                for each in data:
                    if each["fromUser"] in self.trusted_users:
                        response = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[{"role": "user", "content": each["data"]["app_data"] }]
                            )["choices"][0]["message"]["content"]
                        response = encrypt(response, self.encrypt_key)
                        self.integration.send("reply", response, each["fromUser"])
            time.sleep(5)

    def close(self):
        self.integration.close()

def main():
    gptaapi.command_line = True
    fire.Fire(gptaapi)