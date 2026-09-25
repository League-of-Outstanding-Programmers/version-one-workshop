# Python Cheat Sheet - Activity 2: Decision Structures

Everything you need for Activity 2 (classifying something based on conditions, then adjusting a value).

---

## 1. Comparison Operators

```python
a == b    # equal to
a != b    # not equal to
a > b     # greater than
a < b     # less than
a >= b    # greater than or equal to
a <= b    # less than or equal to
```

Each of these produces a `bool`: `True` or `False`.

**Docs:** [W3Schools Python Comparison Operators](https://www.w3schools.com/python/python_operators_comparison.asp)

---

## 2. if / elif / else

Python checks conditions **top to bottom** and runs the first branch that matches. It skips the rest once one matches.

```python
if condition_a:
    # runs only if condition_a is True
    pass

elif condition_b:
    # runs if condition_a was False AND condition_b is True
    pass

else:
    # runs if none of the above were True
    pass
```

Order matters when ranges could overlap. Think about which condition should be checked first.

**Docs:** [W3Schools Python If...Else](https://www.w3schools.com/python/python_conditions.asp)

---

## 3. Comparing Strings

String comparisons with `==` are case-sensitive:

```python
answer = input()

if answer == "yes":
    # "Yes" or "YES" would NOT match this
    ...
```

If a task says the input will exactly match a given form (e.g. `"yes"` or `"no"`), you can compare directly without worrying about case.

**Docs:** [W3Schools Python String Methods](https://www.w3schools.com/python/python_strings_methods.asp)

---

## 4. Combining Conditions

```python
a and b    # True only if both are True
a or b     # True if at least one is True
not a      # flips True/False
```

These are useful when a single `if` needs to check more than one thing at once.

For example:

```python
if age >= 13 and age < 60:
    ...
```

**Docs:** [W3Schools Python Boolean Operations](https://www.w3schools.com/python/python_booleans.asp)

---

## 5. Adjusting a Value After Classifying It

A common pattern is to figure out a base value first, **then** apply an adjustment in a separate step.

```python
base = 100       # some to-be-determined base value

apply_bonus = True

if apply_bonus:
    base = base + base * 0.05    # base is now increased by 5%
```

Notice that the adjustment happens **after** the base value is already set. You don't need to redo the entire `if/elif/else` chain to apply it.

---

## 6. Putting It Together

```python
score = int(input())

if score >= 90:
    grade = "A"

elif score >= 75:
    grade = "B"

else:
    grade = "C"

print(f"Grade: {grade}")
```

---

## References

* [W3Schools Python Control Flow (if/elif/else)](https://www.w3schools.com/python/python_conditions.asp)
* [W3Schools Python Comparison Operators](https://www.w3schools.com/python/python_operators_comparison.asp)
* [W3Schools Python Boolean Operations](https://www.w3schools.com/python/python_booleans.asp)
