class human:
    def __init__(self,eye_color,height,weight):
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
    hair_color = input("whats' your hair color? ")

    def blob(self):
        for i in range(100):
            print("blob")
arian = human("green","170cm","65kg")
print(arian.eye_color)
print(arian.hair_color)
arian.blob()
