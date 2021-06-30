#This python script handles the settings file, which means:
#version support, checking if it exists, default settigns
#Current settings version: 0
import os
import pathlib
import json

#Set the working directory to "code"
os.chdir(pathlib.Path(__file__).parent.resolve())

default_settings = {
    "version": 0,
    "port": 80,
    "pump_intensity": 30,
    "start_server" : True
}

class Settings:
    current_settings = default_settings
    
    def __init__(self):
        if not os.path.isfile('settings.json'):
            with open('settings.json', 'w', encoding='utf-8') as file:
                json.dump(default_settings, file)
        else:
            with open('settings.json',  encoding='utf-8') as file:
                self.current_settings = json.loads(file.read())
            if not self.check_current():
                with open('settings.json', 'w', encoding='utf-8') as file:
                    json.dump(self.current_settings, file)        
        
    #Check and correct version of settings
    #Return true if not modified
    def check_current(self):
        ret = True
        for key in default_settings:
            if not key in self.current_settings:
                ret = False
                self.current_settings[key] = default_settings[key]
        return ret

    def get_port(self):
        return self.current_settings["port"]

    def get_pump_intensity(self):
        return self.current_settings["pump_intensity"]
    
    def get_start_server(self):
        return self.current_settings["start_server"]