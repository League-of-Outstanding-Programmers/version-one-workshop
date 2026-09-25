# VERSION ONE: A Beginner's Workshop on Git
## Group Collaboration Activity

**Time:** 30 minutes (9:05 AM – 9:35 AM)

### Your Group Folder
Find your group's folder (`Group-01` ... `Group-10`). Inside it:

```
cheat-sheets/
├── activity1_cheatsheet.md  -> syntax help for Activity 1
├── activity2_cheatsheet.md  -> syntax help for Activity 2
├── activity3_cheatsheet.md  -> syntax help for Activity 3
└── activity4_cheatsheet.md  -> syntax help for Activity 4

Group-XX/
├── activity1.py       -> Simple Python Basics (3 inputs)
├── activity2.py       -> Decision Structures (age + student discount)
├── activity3.py       -> Repetition, for loop (odd multipliers only)
├── activity4.py       -> Repetition, while loop (even-number tally)
├── answers.py         -> Group review (fill in after pulling teammates' work)
└── test_activities.py -> Run this and pick your activity to test it (1-4, or 'all')
```

Each `activityN.py` file already contains the full scenario, requirements,
and a fixed test case in its docstring — just fill in the `# TODO` sections.

### Cheat Sheets

Stuck on the Python syntax rather than the logic? Check the `cheat-sheets/`
folder in the root of this repository.

There is one cheat sheet for each activity:

- `activity1_cheatsheet.md`
- `activity2_cheatsheet.md`
- `activity3_cheatsheet.md`
- `activity4_cheatsheet.md`

Each cheat sheet explains the Python concepts, provides a different example,
and includes useful documentation links.

The examples do **not** use the exact answers for the activities.

### Workflow
1. `git clone <this-repo-url>`
2. `cd Group-XX`
3. Open your assigned file, complete the TODOs
4. Run `python test_activities.py` — it will ask which activity you're testing (1-4), run it with the fixed test input, and tell you clearly whether it passed. If it says PASS, you're done; if not, it shows exactly which line is wrong so you can fix it and try again.
   (You can also skip the prompt: `python test_activities.py 1` tests just Activity 1, etc. `python test_activities.py all` checks all four at once.)
5. `git status` → `git add activityN.py` → `git commit -m "Add Activity N solution"` → `git push`
6. Once teammates have pushed: `git pull`
7. Open and RUN every teammate's file to see their output
8. Fill in all 10 blanks in `answers.py` using what you observed (this is NOT checked by `test_activities.py` — it's meant to be filled in by actually reviewing your teammates' work)
9. `git add answers.py` → `git commit -m "Add answers to collaboration activity"` → `git push`
