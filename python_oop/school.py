class school:
    #constructor
    def __init__(self,director,teachers,students,sport_hall):
        self.director=director
        self.teachers=teachers
        self.students=students
        self.sport_hall=sport_hall
    def printdirector(self,director):
        print(self.director)
    def printteachers(self,teachers):
        print(self.teachers)
n=school("Pencho",20,50,"true")
print(n.printdirector("Pencho"))
print(n.printteachers(20))

