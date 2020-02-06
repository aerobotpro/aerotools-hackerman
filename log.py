from datetime import datetime
class log:
    def log(thing):
        with open("aero-data/log.txt", "a") as myfile:
            time = str(datetime.now())
            thing = str(thing)
            myfile.write(f"\n[SYSTEM: AERO_TOOLS]\n[{time}]\n{thing}")
        return 0 
