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
    "debug": False,
    "port": 80,
    "pump_intensity": 30,
    "start_server" : True,
    "schedule" : {
        "mon" : [],
        "tue" : [],
        "wed" : [],
        "thu" : [],
        "fri" : [],
        "sat" : [],
        "sun" : []
    }
}

class Settings:
    current_settings = default_settings
    update = None
    
    def __init__(self, update_function):
        self.update = update_function
        if not os.path.isfile('settings.json'):
            self.save()
        else:
            with open('settings.json',  encoding='utf-8') as file:
                self.current_settings = json.loads(file.read())
            ifsave, self.current_settings = self.check_default(self.current_settings)
            if ifsave:
                self.save()
    
    def load_new(self, settings):
        self.current_settings = Settings.check_with(settings, self.current_settings)[1]
        self.save()
        #Launch update parent update function on new settings
        self.update()
        
    
    def check_with(new_settings, source):
        ret = True
        for key in source:
            if not key in new_settings:
                ret = False
                new_settings[key] = source[key]
        return ret, new_settings
    
    #Check and correct version of settings
    #Return true if not modified
    def check_default(self, settings):
        return Settings.check_with(settings, default_settings)

    def get_field(self, field:str):
        if field in self.current_settings:
            return self.current_settings[field]
        else:
             raise Exception("No field called " + field + " in current_settings")

    def get_schedule(self, day:str = ""):
        if day == "":
            return self.get_field("schedule")
        else:
            return self.get_field("schedule")[day]

    def get_debug(self):
        return self.get_field("debug")

    def get_port(self):
        return self.get_field("port")

    def get_pump_intensity(self):
        return self.get_field("pump_intensity")
    
    def get_start_server(self):
        return self.get_field("start_server")
    
    def save(self):
        with open('settings.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.current_settings, indent=4))