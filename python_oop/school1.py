class school39:
    #constructor
    def __init__(self,director,teachers,sport_hall):
        self.director=director
        self.teachers=teachers
        self.sport_hall=sport_hall
    def printdirector(self,director):
        print(self.director)
    def printteachers(self,teachers):
        print(self.teachers)
    def printsport_hall(self,sport_hall):
        print(self.sport_hall)
v=school39("Ivan",10,"False")
print(v.printdirector("Ivan"))
print(v.printteachers(10))
v.printsport_hall("False")


