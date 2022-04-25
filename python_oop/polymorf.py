class Dog:
    def sound(self):
        print("Baf")
    def sleep(self):
        print("sleep")
    def play(self):
        print("play")
class Cat:
    def sound(self):
        print("Meo")
    def sleep(self):
        print("sleep")
    def play(self):
        print("play")
cat=Cat()
dog=Dog()
for animal in (cat,dog):
    animal.sound()
    animal.sleep()
    animal.play()


