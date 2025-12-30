class SecurePlant:
    def __init__(self, name, height, agee):
        self.name = name
        self.__height = height
        self.__agee = agee

    def create(self):
        print(f"Plant created: {self.name}")

    def get_height(self):
        return(self.__height)

    def get_age(self):
        return(self.__agee)

    def set_height(self, new_height):
        if new_height < 0:
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, new_age):
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age}cm [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__agee = new_age
            print(f"Height updated: {self.__agee} days [OK]")
    
    def get_info(self):
        print(f"Current plant: {self.name} ({self.__height}cm, {self.__agee} days)")

plant = SecurePlant("Rose", 25, 30)

if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant.create()
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print("\n\n")
    plant.get_info()
