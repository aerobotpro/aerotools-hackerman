from random import choice
chars = ['a','b','c','d','e','f','1','2','3','4','5','6','7','8','9','0']
class hashes:
    global chars
    def four_char():
        return str(choice(chars) + choice(chars) + choice(chars) + choice(chars))        
    def eight_char():
        return str(choice(chars) + choice(chars) + choice(chars) + choice(chars)
                   + choice(chars) + choice(chars) + choice(chars) + choice(chars))    
    def twelve_char():
        return str(choice(chars) + choice(chars) + choice(chars) + choice(chars)
                   + choice(chars) + choice(chars) + choice(chars) + choice(chars)
                   + choice(chars) + choice(chars) + choice(chars) + choice(chars))
    def sixteen_char():
        return str(choice(chars) + choice(chars) + choice(chars) + choice(chars)
                   + choice(chars) + choice(chars) + choice(chars) + choice(chars)
                   + choice(chars) + choice(chars) + choice(chars) + choice(chars)
                   + choice(chars) + choice(chars) + choice(chars) + choice(chars))    
