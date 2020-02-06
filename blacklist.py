class blacklist:
    
    def add(idd):
        with open("aero-data/data/blacklist", "a") as file: _ = file.write(f"\n{idd}")
            #check = read.split('\n')
            
            
    def check(idd):
        with open("aero-data/data/blacklist", "r") as file: this = file.read()
        if str(idd) in this.split('\n'):
            thing = True
        else:
            thing = False
        return thing    
