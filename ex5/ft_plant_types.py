class Plant:
    def __init__(self, name, height, agee):
        self.name = name
        self.height = height
        self.agee = agee


class Flower(Plant):
    def __init__(self, name, height, agee, color, bloom):
        super().__init__(name, height, agee)
        self.color = color
        self.bloom = bloom

    def get_info(self):
        print(
            f"{self.name} (Flower): {self.height}cm, {self.agee} days, {self.color} color"
        )

    def is_bloom(self):
        if self.bloom:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} is not blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, agee, diameter, shade):
        super().__init__(name, height, agee)
        self.diameter = diameter
        self.shade = shade

    def get_info(self):
        print(
            f"{self.name} (Tree): {self.height}cm, {self.agee} days, {self.diameter}cm diameter"
        )

    def is_shade(self):
        print(f"{self.name} provides {self.shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, agee, harvest_season, vitamin):
        super().__init__(name, height, agee)
        self.name = name
        self.height = height
        self.agee = agee
        self.harvest_season = harvest_season
        self.vitamin = vitamin

    def get_info(self):
        print(
            f"{self.name} (Vegetable): {self.height}cm, {self.agee} days, {self.harvest_season} harvest"
        )

    def is_rich(self):
        print(f"{self.name} is rich in vitamin {self.vitamin}")


Rose = Flower("Rose", 25, 30, "red", True)
Qak = Tree("Qak", 500, 1825, 50, 78)
Tomat = Vegetable("Tomat", 80, 90, "summer", "C")

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("\n")
    Rose.get_info()
    Rose.is_bloom()
    print("\n")
    Qak.get_info()
    Qak.is_shade()
    print("\n")
    Tomat.get_info()
    Tomat.is_rich()
