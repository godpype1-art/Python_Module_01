class Plant:

    class Stats:

        def __init__(self) -> None:
            self._age_counter: int = 0
            self._grow_counter: int = 0
            self._show_counter: int = 0

        def Stats(self) -> None:
            print(
                f"Stats: {self._grow_counter} grow, "
                f"{self._age_counter} age, {self._show_counter} show"
                )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = height
        self._age: int = age
        self._stats = self.Stats()

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = new_height
        print(f"Height updated: {round(self._height)}cm")

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = new_age
        print(f"Age updated: {round(self._age)} days")

    def grow(self) -> None:
        self._height += 0.8
        self._stats._grow_counter += 1

    def age(self) -> None:
        self._age += 1
        self._stats._age_counter += 1

    def show(self) -> None:
        self._stats._show_counter += 1
        print(f"{self.name}: {round(self._height)}cm, {self._age} days old")

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    @staticmethod
    def check_age(age: int) -> None:
        print(f"Is {age} days more than a year? -> {age > 365}")


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def grow(self) -> None:
        self._height += 8.0
        self._stats._grow_counter += 1

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self.bloomed is True:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds += 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    _stats: "Stats"

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_counter: int = 0

        def Stats(self) -> None:
            super().Stats()
            print(f"{self._shade_counter} shade")

    def __init__(
            self, name: str, height: float, age: int, trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats = Tree.Stats()

    def produce_shade(self) -> None:
        self._stats._shade_counter += 1
        print(f"Tree {self.name} now produces a shade of ", end="")
        print(f"{round(self._height, 1)}", end="")
        print(f"cm long and {round(self._trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: float,
            age: int, harvest_season: str, nutritional_value: int
            ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def grow(self) -> None:
        self._height += 2.1

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1


def show_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant._stats.Stats()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    show_stats(rose)
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_stats(oak)
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    show_stats(sunflower)
    print()
    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    show_stats(unknown)


if __name__ == "__main__":
    main()
