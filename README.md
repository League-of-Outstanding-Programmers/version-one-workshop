# Version One: A Beginner's Workshop on Git

## Group Collaboration Activity

**Time:** 30 minutes (9:05 AM – 9:35 AM)

### Your Group Folder

Find your group's folder (`Group-01` ... `Group-10`). Inside it:

```text
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

Each `activityN.py` file already contains the full scenario, requirements, and a fixed test case in its docstring. Just fill in the `# TODO` sections.

### Cheat Sheets

Stuck on the Python syntax rather than the logic? Check the `cheat-sheets/` folder in the root of this repository.

There is one cheat sheet for each activity:

* `activity1_cheatsheet.md`
* `activity2_cheatsheet.md`
* `activity3_cheatsheet.md`
* `activity4_cheatsheet.md`

Each cheat sheet explains the Python concepts, provides a different example, and includes useful documentation links.

The examples do **not** use the exact answers for the activities.

### Workflow

#### 1. Clone the repository

```bash
git clone <this-repo-url>
cd version-one-workshop
```

#### 2. Set up sparse checkout

Sparse checkout allows you to work with only your group's folder instead of checking out all ten group folders.

Initialize sparse checkout:

```bash
git sparse-checkout init --cone
```

Then select your group's folder.

**Group 1:**

```bash
git sparse-checkout set Group-01
```

**Group 2:**

```bash
git sparse-checkout set Group-02
```

Continue using your assigned group number (`Group-03`, `Group-04`, etc.).

After this, only your group's folder will appear in your working directory.

> **Important:** Replace `Group-01` with your actual group folder. Do not use another group's folder.

#### 3. Enter your group folder

```bash
cd Group-XX
```

Replace `Group-XX` with your assigned group folder.

#### 4. Complete your assigned activity

Open your assigned file and complete the `# TODO` sections.

#### 5. Test your activity

Run:

```bash
python test_activities.py
```

It will ask which activity you're testing (1-4), run it with the fixed test input, and tell you clearly whether it passed.

If it says **PASS**, you're done. If not, it shows which part needs to be fixed so you can try again.

You can also skip the prompt:

```bash
python test_activities.py 1
```

This tests Activity 1.

```bash
python test_activities.py all
```

This checks all four activities at once.

#### 6. Commit and push your work

After your activity passes the test:

```bash
git status
git add activityN.py
git commit -m "Add Activity N solution"
git push
```

Replace `N` with your activity number.

#### 7. Pull your teammates' latest changes

Once your teammates have pushed their work:

```bash
git pull
```

This gets the latest changes from the shared repository.

#### 8. Review your teammates' work

Open and **run every teammate's file** to see their output.

Review their solutions and observe how they approached the activities.

#### 9. Complete `answers.py`

Fill in all 10 blanks in `answers.py` based on what you observed from your teammates' work.

This file is **not checked by `test_activities.py`**. It is meant to be completed by actually reviewing your teammates' solutions.

#### 10. Commit and push the group review

```bash
git add answers.py
git commit -m "Add answers to collaboration activity"
git push
```
