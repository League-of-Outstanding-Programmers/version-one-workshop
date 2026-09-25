# Python Cheat Sheet - Activity 1: Variables, I/O & Calculations

Everything you need for Activity 1 (reading input, doing math, and printing formatted output).

---

## 1. Reading Input from the Console

`input()` always returns a **string**, even if the user types a number.

```python
name = input()          # reads one line as text
raw = input()           # e.g. "42" -> the string "42", not the number 42
```

If you call `input()` several times in a row, each call reads the *next* line the user types (or the next line piped into the program).

**Docs:** [W3Schools Python User Input](https://www.w3schools.com/python/python_user_input.asp)

---

## 2. Converting Text to Numbers

Since `input()` gives you text, convert it before doing math:

```python
whole = int("42")        # 42          (whole numbers)
decimal = float("3.14")  # 3.14        (numbers with a decimal point)
```

Calling `int()` on something like `"3.5"` will crash. Use `float()` for anything that might have a decimal point.

**Docs:** [W3Schools Python User Input](https://www.w3schools.com/python/python_user_input.asp) · [W3Schools Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)

---

## 3. Built-in Types You'll Use

| Type    | What it is     | Example |
| ------- | -------------- | ------- |
| `int`   | Whole number   | `42`    |
| `float` | Decimal number | `3.14`  |
| `str`   | Text           | `"hi"`  |

```python
price = 9.99      # float
quantity = 3      # int
```

**Docs:** [W3Schools Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)

---

## 4. Operators

```python
a + b    # addition
a - b    # subtraction
a * b    # multiplication
a / b    # division, always gives a float
a // b   # floor division, drops the fractional part
a % b    # remainder / modulo
```

**Docs:** [W3Schools Python Arithmetic Operators](https://www.w3schools.com/python/python_operators_arithmetic.asp)

---

## 5. Printing Formatted Output

An f-string lets you drop variables straight into text with `f"...{var}..."`.

To round a number to a fixed number of decimal places, use `:.2f` inside the braces. The `2` means two decimal places.

```python
value = 7

print(f"Value: {value}")              # Value: 7

amount = 12.3

print(f"Amount: {amount:.2f}")        # Amount: 12.30
```

Each `print(...)` call outputs one line and automatically adds a newline at the end. So if a task asks for **exactly N lines**, you generally want N separate `print()` calls (or one f-string per line).

**Docs:** [W3Schools Python String Formatting](https://www.w3schools.com/python/python_strings_format.asp)

---

## 6. Putting It Together

This example is deliberately a *different* problem from your activity. Use it to see the pattern, not to copy the answer.

```python
length = float(input())

width = float(input())

area = length * width

perimeter = 2 * (length + width)

print(f"Area: {area:.2f}")

print(f"Perimeter: {perimeter:.2f}")
```
