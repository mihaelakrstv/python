class Uni:
    #constructor
    def __init__(self,law,architecture):
        self.law=law
        self.architecture=architecture
    def printlaw(self,law):
        print(self.law)
    def printarchitecture(self,architecture):
        print(self.architecture)
class law(Uni):
    def __init__(self,family_law,criminal_law):
        self.family_law=family=law
        self.criminal_law=criminal_law
    def printfamily_law(self,family_law):
        print(self.family_law)
    def printcriminal_law(self,criminal_law):
        print(self.criminal_law)
class architecture(Uni):
    def __init__(self, math, drawing):
        self.math=math
        self.drawing=drawing
    def printmath(self,math):
        print(self.math)
    def printdrawing(self,drawing):
        print(self.drawing)
o=Uni("law1","architecture1")
p=law("family_law1", "criminal_law1")
h=architecture("math1", "drawing1")
print(h.math)
print(p.criminal_law)
print(o.law)

