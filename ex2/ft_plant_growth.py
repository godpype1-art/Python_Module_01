class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> float:
        self.height += 0.8
        return 0.8

    def ages(self) -> int:
        self.age += 1
        return 1


def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    growth: float = 0.0
    print("=== Garden Plant Growth ===")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.ages()
        growth += rose.grow()
        print(f"{rose.name}: {round(rose.height, 1)}cm, {rose.age} days old")
    print(f"Growth this week: {round(growth, 1)}cm")


if __name__ == "__main__":
    main()
