# Python Cheat Sheet - Activity 4: While Loops & Counting

Everything you need for Activity 4 (looping until a condition becomes false, decrementing, and tallying as you go).

## 1. `while` Loops

A `while` loop keeps running **as long as its condition is `True`**. Unlike a `for` loop, you don't know in advance how many times it will run. It depends on what happens inside the loop.

```python
n = 5

while n > 0:
    print(n)
    n = n - 1    # or: n -= 1
```

**Docs:** [W3Schools Python `while` Loops](https://www.w3schools.com/python/python_while_loops.asp)

## 2. Decrementing (and Avoiding Infinite Loops)

Every `while` loop needs something inside it that eventually makes the condition `False`. Otherwise, it never stops.

```python
n -= 1    # shorthand for n = n - 1
```

If you forget this line, or put it in the wrong place, the loop will run forever. If your program seems to hang when you test it, this is the first thing to check.

## 3. Counting / Tallying Inside a Loop

Just like the accumulator pattern for sums, a tally counter starts at `0` **before** the loop and gets increased **inside** the loop whenever a condition is met.

```python
even_count = 0    # starts at 0, before the loop

n = 5

while n > 0:
    if n % 2 == 0:
        even_count += 1    # only increases when n is even

    n -= 1

print(even_count)
```

You can track more than one tally at once, such as a total count **and** a filtered count. Just give each its own variable, both initialized before the loop.

## 4. Modulo for Even/Odd (Reminder)

```python
n % 2 == 0    # True when n is even
```

## 5. `for` vs `while` Which to Use

Use `for` + `range()` when you know exactly how many times to loop.

Use `while` when the loop should continue "until some condition is no longer true", like counting down until a value reaches zero.

## 6. Putting It Together

```python
n = int(input())

total_count = 0
multiples_of_three = 0

while n > 0:
    print(n)

    total_count += 1

    if n % 3 == 0:
        multiples_of_three += 1

    n -= 1

print(f"Total printed: {total_count}")
print(f"Multiples of 3: {multiples_of_three}")
```

---

## References

* [`while` Loops](https://www.w3schools.com/python/python_while_loops.asp)
* [Augmented Assignment (`+=`, `-=`)](https://www.w3schools.com/python/gloss_python_assignment_operators.asp)
