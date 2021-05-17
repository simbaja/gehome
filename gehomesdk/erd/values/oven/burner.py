#not sure where this is used, but I found these mappings
#0x5778 = burner1
#0x5779 = burner2
#0x577a = burner3
#0x577b = burner4
#0x577c = burner5
#0x577d = burner6
#0x577e = burner1 + burner2

## These are guesses as to the meaning of the bits
## It's really hard to tell from what the app is showing in the interface, most aren't used
#burner.a = exists
#burner.b = on_off_only
#burner.c = something to do with sensor cooking...
#burner.d = something to do with being on... 
#burner.e = synchronized
#burner.f = on
#burner.g = power_pct

class Burner:
    def __init__(self, value: int, power: int):
        self.exists = self.shift(value, 0)
        #they skip the first bit shift (never stored, so not sure what it is)
        self.on_off_only = self.shift(value, 2) #b
        self.c = self.shift(value, 3) #c
        self.d = self.shift(value, 4) #d
        self.synchronized = self.shift(value, 5) #e
        self.on = self.shift(value, 6) #f

        self.power_pct = (~int("10000000", 2)) & power #g
        
    def shift(self, value: int, shift: int) -> bool:
        return ((value & (1 << shift)) >> shift) == 1
