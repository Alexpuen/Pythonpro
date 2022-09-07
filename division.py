def make_division_by(n):
    def divisor(number: int) -> float:
        assert type(number) == int, "Solo puedes usar numeros"
        return number / n
    return divisor


def run():
    
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))

if __name__ == "__main__":
    run()