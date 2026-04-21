print("--- Example 1: Using Built-in Modules ---")

import math
import random
import datetime

print("\n--- math module ---")
print("Pi:           ", math.pi)
print("Square root 25:", math.sqrt(25))
print("2 to the power 8:", math.pow(2, 8))

print("\n--- random module ---")
print("Random number 1-100:", random.randint(1, 100))
colors = ["red", "green", "blue", "yellow"]
print("Random color:       ", random.choice(colors))

print("\n--- datetime module ---")
now = datetime.datetime.now()
print("Today's date:", now.date())
print("Current time:", now.time())
print("Year:        ", now.year)
