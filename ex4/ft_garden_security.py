class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age
        print(
            f"Plant created: {self.name}: "
            f"{self._height}cm, {self._age} days old"
        )

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

    def show(self) -> None:
        print(
            f"Current state: {self.name}: "
            f"{self._height}cm, {self._age} days old"
        )


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-12.0)
    rose.set_age(-12)
    print()
    rose.show()


if __name__ == "__main__":
    main()
