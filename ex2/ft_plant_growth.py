class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.old = age

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.old += 1


def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    initial_height: float = rose.height
    print("=== Garden Plant Growth ===")
    print(f"{rose.name}: {rose.height}cm, {rose.old} days old")
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.age()
        rose.grow()
        print(f"{rose.name}: {round(rose.height, 1)}cm, {rose.old} days old")
    print(f"Growth this week: {round(rose.height - initial_height, 1)}cm")


if __name__ == "__main__":
    main()
