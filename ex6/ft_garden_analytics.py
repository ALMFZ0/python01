# class Normal Plant
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.growth = 0

    def grow(self, cm):
        self.height += cm
        self.growth += cm
        print(f"{self.name} grew {cm}cm")

    def get_info(self):
        return f"{self.name}: {self.height}cm"


# class FloweringPlant


class FloweringPlant(Plant):
    def __init__(self, name, height, color, blooming=True):
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming

        is_bloom = "(blooming)" if self.blooming else "(dormant)"

        def get_info(self):
            print(f"{self.name}: {self.height}cm, {self.color} " f" flowers {is_bloom}")


# class prizeFlower


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize):
        super().__init__(name, height, color)
        self.prize = prize

        def get_info(self):
            print(f"{self.get_info()}, Prize points: {self.prize}")


# class GardenManager


class GardenManager:
    total_gardens = 0

    class GardenStats:

        @staticmethod
        def calcule_total_grow(plants):
            total = 0
            for i in plants:
                total += i.growth
            return total

        @staticmethod
        def calcule_score(plants):
            total = 0
            for i in plants:
                total += i.height
            for i in plants:
                if isinstance(i, PrizeFlower):
                    total += i.prize * 4
            return total

        @staticmethod
        def calcule_plan_type(plants):
            normal = sum(1 for i in plants if type(i) is Plant)
            flowring = sum(1 for i in plants if type(i) is FloweringPlant)
            prize = sum(1 for i in plants if type(i) is PrizeFlower)
            return normal, flowring, prize

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def height_is_valid(self):
        for i in self.plants:
            if i.height < 0 or i.height > 1500:
                print("Height validation test: False")
                return False
        print("Height validation test: False")
        return True

    def report(self):
        print(f"=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for i in self.plants:
            print(f"- {i.get_info()}")

        total_grow = self.GardenStats.calcule_total_grow(self.plants)
        normal, flower, prize = self.GardenStats.calcule_plan_type(self.plants)
        print(f"Plants added: {len(self.plants)}, Total growth: {total_grow}")
        print(
            f"Plant types: {normal} regular, {flower} flowring, "
            f"{prize} prize flowers"
        )

    @classmethod
    def create_garden_network(cls, owner_names):
        print("\n=== Garden Management System Demo ===\n")
        network = []
        for name in owner_names:
            network.append(cls(name))
        return network

    def help_plants_grow(self, cm):
        print(f"{self.owner_name} is helping all plants grow...")
        for i in self.plants:
            i.grow(cm)


# ======= MAIN ========
# 1. Use Class Method to managers
alice_g, bob_g = GardenManager.create_garden_network(["Alice", "Bob"])

# 2. Setup Alice's Garden

p1 = Plant("Oak Tree", 100)
p2 = FloweringPlant("Rose", 25, "red")
p3 = PrizeFlower("Sunflower", 50, "yellow", 10)

alice_g.add_plant(p1)
alice_g.add_plant(p2)
alice_g.add_plant(p3)

# 3. Setup Bob's Garden
bob_g.add_plant(Plant("Bush", 40))
bob_g.add_plant(FloweringPlant("Daisy", 52, "white"))

# 3. Setup Bob's Garden

alice_g.help_plants_grow(1)

print()  # Empty line for formatting

alice_g.report()

# 6. Validate if every height is valid in Alice's Garden
print(alice_g.height_is_valid())

# 7. Scoring Logic
alice_score = alice_g.GardenStats.calcule_score(alice_g.plants)
bob_score = bob_g.GardenStats.calcule_score(bob_g.plants)
print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

# 8. Print Number of gardens managed (Class variable check)
print(f"Total gardens managed: {alice_g.total_gardens}")
