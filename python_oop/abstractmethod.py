from abc import ABC,abstractmethod 
#include<....>
class Microprocessors:
    @abstractmethod
    def showmicroproc(self):
        print("RB2040")
    def showmicroproc(self):
        print("ATMEGA328P")
    def showmicroproc(self):
        print("ATTINY85")
m=Microprocessors()
m.showmicroproc()

