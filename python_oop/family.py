class Family:
    def __init__(self,black_hair,green_eyes,short_hair,short_height,red_nails,long_eyelashes):
        self.black_hair=black_hair
        self.green_eyes=green_eyes
        self.short_hair=short_hair
        self.short_height=short_height
        self.red_nails=red_nails
        self.long_eyelashes=long_eyelashes
    def printhair(self,black_hair):
        print(self.black_hair)
    def printeyes(self,green_eyes):
        print(self.green_eyes)
class mother(Family):
    def printhair(self,short_hair):
        print(self.short_hair)
    def printheight(self,short_height):
        print(self.short_height)
class me(mother):
    def printnails(self,red_nails):
        print(self.red_nails)
    def printeyelashes(self,long_eyelashes):
        print(self.long_eyelashes)
r=Family("black_hair1","green_eyes1","short_hair1","short_height1","red_nails1","long_eyelashes1")
f=mother("short_hair1","short_height1","red_nails1","long_eyelashes1","black_hair1","green_eyes1")
e=me("red_nails1","long_eyelashes1","short_hair1","short_height1","green_eyes1","black_hair1")
print(r.printhair("black_hair1"))
print(f.printheight("short_height1"))
print(e.printnails("red_nails1"))

