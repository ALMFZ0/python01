class Plant:
    def __init__(self, name, height, agee):
        self.name = name
        self.height = height
        self.agee = agee
    def create(self):
        print(f"Created: {self.name} ({self.height}cm, {self.agee} days)")
        
    

list = [
    ["Rose", 25, 30],
    ["Oak", 200, 365],
    ["Cactus", 5, 90],
    ["Sunflower", 80, 45],
    ["Fern", 15, 120],
        ]
print("=== Plant Factory Output ===")

for i in list:
    plant = Plant(*i)
    plant.create()


print("Total plants created: 5")

