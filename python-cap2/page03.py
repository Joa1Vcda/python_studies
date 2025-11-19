"""method init in class"""


class Car:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        pass


Car1 = Car("Fusca", "1994")
print(Car1.name, Car1.year)

Car2 = Car("Golf GTI", "2021")
print(Car2.name, Car2.year)


class camera:
    def __init__(self, name, recording=False, photo=False):
        self.name = name
        self.recording = recording
        self.photo = photo

    def rec(self):
        if self.recording == True:
            print(f"{self.name} is already recording")
            return

        self.recording = True
        print(f"{self.name} is recording...")

    def TakePhoto(self):
        if self.recording == True:
            print(f"{self.name} is alrealdy recording, can't take a photo")
            return
        c2.photo = True
        print("Photo taken successfully")


c1 = camera("Canon")
c1.rec()
c1.rec()
c2 = camera("Sony")
print(c1.recording)
print(c2.recording)
c2.TakePhoto()
print(c2.photo)
