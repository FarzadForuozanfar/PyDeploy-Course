import time
import random


def marriage(name):
    r = random.randint(0, 10)
    time.sleep(r)
    print(f"{name} married after {r} years.")


def main():
    for child in ["Ali", "Mammad", "Reza", "Tina"]:
        marriage(child)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f"Executed in {run_time} seconds.")
    