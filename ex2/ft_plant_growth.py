class Plant:
    def __init__(self, name, height, agee):
        self.name = name
        self.height = height
        self.agee = agee
    def grow(self):
        self.height += 6

    def age(self):
        self.agee += 6

    def get_info(self):
        print("=== Day 1 ===")
        print(f"{self.name}: {self.height}cm, {self.agee} days old")
        self.grow()
        self.age()
        print("=== Day 7 ===")
        print(f"{self.name}: {self.height}cm, {self.agee} days old")
        print("Growth this week: +6cm")

plant1 = Plant("Rose", 25, 30)

if __name__ == "__main__":
    plant1.get_info()