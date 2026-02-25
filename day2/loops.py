# ==========================================================
# 1. FOR LOOP
# ==========================================================

# A for loop is used to iterate over a sequence
# (such as a list, tuple, string, or range).

print("Example 1: Basic for loop")

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    # This block runs once for each element in the list
    print("Current number:", num)

print("-" * 40)


# ==========================================================
# 2. USING range() WITH FOR LOOP
# ==========================================================

# range(start, stop, step)
# start: starting number (inclusive)
# stop: ending number (exclusive)
# step: increment value

print("Example 2: for loop with range()")

for i in range(0, 10, 2):
    print("i =", i)

print("-" * 40)


# ==========================================================
# 3. WHILE LOOP
# ==========================================================

# A while loop runs as long as a condition is True.

print("Example 3: while loop")

counter = 0

while counter < 5:
    print("Counter value:", counter)
    counter += 1  # Important: update the condition variable

print("-" * 40)


# ==========================================================
# 4. BREAK STATEMENT
# ==========================================================

# break immediately stops the loop.

print("Example 4: break statement")

for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print("i =", i)

print("-" * 40)


# ==========================================================
# 5. CONTINUE STATEMENT
# ==========================================================

# continue skips the current iteration
# and moves to the next iteration.

print("Example 5: continue statement")

for i in range(5):
    if i == 2:
        print("Skipping i =", i)
        continue
    print("i =", i)

print("-" * 40)


# ==========================================================
# 6. NESTED LOOPS
# ==========================================================

# A loop inside another loop is called a nested loop.

print("Example 6: nested loops")

for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

print("-" * 40)


# ==========================================================
# 7. LOOP WITH ELSE
# ==========================================================

# The else block runs if the loop completes normally
# (without encountering a break statement).

print("Example 7: loop with else")

for i in range(3):
    print("i =", i)
else:
    print("Loop finished without break.")

print("-" * 40)


# ==========================================================
# 8. PRACTICAL EXAMPLE – FINDING A NUMBER
# ==========================================================

# This example searches for a target value in a list.

print("Example 8: searching in a list")

data = [10, 25, 30, 45, 50]
target = 30

for value in data:
    if value == target:
        print("Target found:", value)
        break
else:
    print("Target not found.")