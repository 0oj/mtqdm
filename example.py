from mtqdm import mtqdm
import time
import random

def main():
    """Example usage of mtqdm."""
    # Use mtqdm as a drop-in replacement for tqdm
    for _ in mtqdm(range(100), display_mode=mtqdm.DisplayMode.BAR):
        # Simulate some work
        time.sleep(random.uniform(0.1, 0.2))

if __name__ == "__main__":
    main()
