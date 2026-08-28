# acronyms
 
 A collection of acronyms from business, technology, security, and engineering.
 I am documenting the acronyms that I encounter while working, studying, and researching.

 ## Scope

 Reminders on what not to include:
 1. No common government agencies (e.g. IRS, FBI, CIA, etc.)
 1. No common acronyms that have become integrated into modern English language (e.g. SCUBA, PIN, etc.) 
 
 ## Contributing

 `acronyms.csv` is checked for duplicate (Acronym, Meaning) rows before every
 commit via a `.git/hooks/pre-commit` script that runs `check_duplicates.py`
 (an acronym may still appear more than once as long as its Meaning differs,
 e.g. `IP` = Intellectual Property vs. Internet Protocol). The same check
 also runs in CI as a backstop.

 The git hook itself only needs Python 3 and is already active in this repo.
 If you clone a fresh copy, either use the
 [pre-commit](https://pre-commit.com) framework:

 ```
 pip install pre-commit
 pre-commit install
 ```

 or just run `python3 check_duplicates.py acronyms.csv` by hand before
 committing.

 ## Future Plans

 I _might_ use this data to create an API.
 
