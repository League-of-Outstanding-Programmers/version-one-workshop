"""
Activity 2: Movie Ticket Classifier with Student Discount
Concepts: if / elif / else, comparison operators, and basic conditions

Scenario:
Create a cinema ticket classifier based on the customer's age.
Students receive an additional 10% discount after the base ticket
price has been determined.

Ticket pricing:
    age < 13        -> "Child",   price 150
    13 <= age < 60  -> "Regular", price 250
    age >= 60       -> "Senior",  price 150

Requirements:
- Read age (int) and is_student (str, exactly "yes" or "no")
  using input(), one per line, in that order.
- Use if / elif / else to determine the ticket type and base price.
- If is_student == "yes", apply a 10% discount:
    price = price - price * 0.10
- Print exactly two lines with the price as a whole number:
    Ticket Type: <ticket_type>
    Price: <price>

Example test cases:
    Input:
        10
        yes

    Expected Output:
        Ticket Type: Child
        Price: 135

    Input:
        25
        no

    Expected Output:
        Ticket Type: Regular
        Price: 250

    Input:
        65
        yes

    Expected Output:
        Ticket Type: Senior
        Price: 135

Write the solution below this line.
"""

# TODO: read age and is_student from input()

# TODO: use if / elif / else to determine ticket_type and price

# TODO: if is_student == "yes", apply the 10% discount to price

# TODO: print the two required lines
