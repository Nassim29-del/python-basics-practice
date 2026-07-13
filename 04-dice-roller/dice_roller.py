# Rolls a die a chosen number of times and shows each result plus a tally.

import random


def roll(times, sides=6):
    results = [random.randint(1, sides) for _ in range(times)]
    tally = {face: results.count(face) for face in range(1, sides + 1)}
    return results, tally


def main():
    times = int(input("How many rolls? "))
    results, tally = roll(times)
    print("Rolls:", results)
    print("Tally:")
    for face, count in tally.items():
        print(f"  {face}: {count}")


if __name__ == "__main__":
    main()
