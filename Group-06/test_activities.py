"""
Self Check Script for the Activities

Run the script using:
    python test_activities.py

The script will ask which activity to test (1-4). It will run the
selected activity using the fixed test input from the instructions
and clearly show whether the output matches the expected result.

A specific activity can also be tested directly:
    python test_activities.py 1
    python test_activities.py 2
    python test_activities.py 3
    python test_activities.py 4

To test all four activities at once:
    python test_activities.py all

This script does NOT check answers.py. The answers.py file must be
completed by pulling and reviewing the work of the other group members.
"""

import subprocess
import sys
import os

TESTS = {
    "1": {
        "file": "activity1.py",
        "name": "Activity 1 - Order Total Calculator",
        "stdin": "100\n2\n15\n",
        "input_shown": ["100", "2", "15"],
        "expected": [
            "Subtotal: 200.00",
            "Tax: 24.00",
            "Delivery Fee: 15.00",
            "Grand Total: 239.00",
        ],
    },
    "2": {
        "file": "activity2.py",
        "name": "Activity 2 - Movie Ticket Classifier",
        "cases": [
            {"input_shown": ["10", "yes"], "stdin": "10\nyes\n",
             "expected": ["Ticket Type: Child", "Price: 135"]},
            {"input_shown": ["25", "no"], "stdin": "25\nno\n",
             "expected": ["Ticket Type: Regular", "Price: 250"]},
            {"input_shown": ["65", "yes"], "stdin": "65\nyes\n",
             "expected": ["Ticket Type: Senior", "Price: 135"]},
        ],
    },
    "3": {
        "file": "activity3.py",
        "name": "Activity 3 - Odd Multiples Table",
        "stdin": "5\n",
        "input_shown": ["5"],
        "expected": [
            "5 x 1 = 5", "5 x 3 = 15", "5 x 5 = 25", "5 x 7 = 35", "5 x 9 = 45",
            "Sum: 125",
        ],
    },
    "4": {
        "file": "activity4.py",
        "name": "Activity 4 - Countdown Beeper",
        "stdin": "5\n",
        "input_shown": ["5"],
        "expected": ["5", "4", "3", "2", "1", "Total beeps: 5", "Even beeps: 2"],
    },
}


def run_program(path, stdin_text, timeout=5):
    try:
        result = subprocess.run(
            [sys.executable, path],
            input=stdin_text,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        if result.returncode != 0 and result.stderr.strip():
            return None, result.stderr.strip()
        return result.stdout.strip().splitlines(), None
    except Exception as e:
        return None, str(e)


def show_diff(expected, actual):
    max_len = max(len(expected), len(actual))
    for i in range(max_len):
        exp_line = expected[i] if i < len(expected) else "(nothing)"
        act_line = actual[i] if i < len(actual) else "(nothing)"
        marker = "  " if exp_line == act_line else "->"
        print(f"   {marker} line {i + 1}: expected {exp_line!r}, got {act_line!r}")


def run_one_case(filename, case, label=""):
    if not os.path.exists(filename):
        print(f"Couldn't find {filename} in this folder.")
        return False

    actual, error = run_program(filename, case["stdin"])
    input_str = ", ".join(case["input_shown"])

    if error:
        print(f"Your program crashed with input ({input_str}):")
        print(f"   {error}")
        return False

    if actual == case["expected"]:
        print(f"PASS{(' - ' + label) if label else ''} (input: {input_str})")
        return True
    else:
        print(f"FAIL{(' - ' + label) if label else ''} (input: {input_str})")
        show_diff(case["expected"], actual)
        return False


def test_activity(key):
    test = TESTS[key]
    print(f"\nTesting {test['name']} ({test['file']})")
    print("-" * 50)

    if "cases" in test:
        results = [run_one_case(test["file"], case) for case in test["cases"]]
        passed = all(results)
    else:
        passed = run_one_case(test["file"], test)

    print("-" * 50)
    if passed:
        print("All good! You're ready to commit and push this file.\n")
    else:
        print("Not quite there yet - check the lines marked with -> above,\n"
              "fix your code, and run this again.\n")
    return passed


def ask_which_activity():
    print("Which activity are you testing?")
    print("  1 - Order Total Calculator")
    print("  2 - Movie Ticket Classifier")
    print("  3 - Odd Multiples Table")
    print("  4 - Countdown Beeper")
    print("  all - test all four")
    choice = input("Enter 1, 2, 3, 4, or 'all': ").strip().lower()
    return choice


def main():
    if len(sys.argv) > 1:
        choice = sys.argv[1].strip().lower()
    else:
        choice = ask_which_activity()

    if choice == "all":
        results = [test_activity(k) for k in ("1", "2", "3", "4")]
        passed = sum(results)
        print(f"{passed}/4 activities passed.")
    elif choice in TESTS:
        test_activity(choice)
    else:
        print(f"'{choice}' isn't a valid option. Use 1, 2, 3, 4, or 'all'.")


if __name__ == "__main__":
    main()
