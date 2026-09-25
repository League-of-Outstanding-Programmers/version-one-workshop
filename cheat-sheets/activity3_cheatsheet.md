# Python Cheat Sheet - Activity 3: For Loops & Accumulation

Everything you need for Activity 3 (looping a fixed number of times, filtering with a condition, and keeping a running total).

---

## 1. `range()` and `for` Loops

`range(start, stop)` produces numbers from `start` up to, **but not including**, `stop`.

```python
for i in range(1, 11):
    print(i)    # prints 1, 2, 3, ... 10 (11 is NOT included)
```

If a task says "loop from 1 to 10," you generally want `range(1, 11)`.

**Docs:** [W3Schools Python `range()`](https://www.w3schools.com/python/ref_func_range.asp) · [W3Schools Python `for` Loops](https://www.w3schools.com/python/python_for_loops.asp)

---

## 2. The Modulo Operator for Even/Odd

`%` gives you the remainder of a division. This is the standard way to test whether a number is even or odd:

```python
n % 2 == 0    # True when n is even
n % 2 == 1    # True when n is odd (for non-negative n)
```

**Docs:** [W3Schools Python Arithmetic Operators](https://www.w3schools.com/python/python_operators_arithmetic.asp)

---

## 3. Filtering Inside a Loop with `if`

You can skip iterations that don't meet a condition by wrapping the loop body in an `if`:

```python
for i in range(1, 6):
    if i % 2 == 0:
        print(i)    # only even i values get printed
```

Only the code **inside** the `if` block is conditional. Anything outside it, such as the next iteration of the loop, still happens normally.

---

## 4. The Accumulator Pattern

To keep a running total across loop iterations, create the variable **before** the loop starts, then update it **inside** the loop:

```python
total = 0                 # starts at 0, before the loop

for i in range(1, 6):
    total = total + i     # or: total += i

print(total)              # the final sum after all iterations
```

A common mistake is putting `total = 0` **inside** the loop. That resets it every iteration instead of accumulating.

---

## 5. Putting It Together

```python
n = int(input())

total = 0

for i in range(1, 6):
    if i % 2 == 0:
        square = i * i
        print(f"{i} squared = {square}")
        total = total + square

print(f"Sum of even squares: {total}")
```

---

## References

* [`range()`](https://www.w3schools.com/python/ref_func_range.asp)
* [`for` Loops](https://www.w3schools.com/python/python_for_loops.asp)
* [Arithmetic & Modulo](https://www.w3schools.com/python/python_operators_arithmetic.asp)
