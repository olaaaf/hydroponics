import time
import os
from pathlib import Path

def file_name(index):
    fileName = index + ".txt"
    return os.path.join("logs", fileName)

class Debug:
    save = None
    log_index = ""
    
    def __init__(self):
        self.log_index = Debug.get_index()
        print ('Logging in the file: logs/' + self.log_index + ".txt")
    
    def get_index():
        #Set the current working directory
        os.chdir(Path(__file__).parent.resolve())
        #Create the logs directory, while checking if it does not exist
        if not Path('logs').is_dir():
            os.mkdir('logs')
        today = int(time.time())
        index = str(today)
        #Create the file if it does not exist
        if not Path('logs' + index + ".txt").is_file():
            with open(file_name(index), "w") as f:
                f.write(index + " log\n") 
        return index
    
    def open(self):
        #open the file with append mode
        self.save = open(file_name(self.log_index), "a+")
    
    def close(self):
        self.save.close()
        pass
    
    def write_line(message:str, type:str):
        index = Debug.get_index()
        with open(file_name(index), "a+") as save:
            save.write(type + ": " + message+"\n")
        
    
    def write(self, message:str, type):
        self.save.write(type + ": " + message+"\n")
        
        

