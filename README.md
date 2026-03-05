# Clinical Risk CLI — Test-Driven Development with Copilot Agent

**Course:** MS in Health Informatics  
**Tools:** Python 3, `unittest`, GitHub Codespaces, GitHub Copilot Agent Mode  
**Application Type:** Command-Line Interface (CLI)

---

## Purpose of This Exercise

This in-class exercise is designed to help you practice **Test-Driven Development (TDD)** while working with **GitHub Copilot Agent Mode** in GitHub Codespaces.

You will:
- Write **tests first** using Python’s built-in `unittest` framework
- Use **Copilot Agent** to implement code that satisfies your tests
- Apply the **red → green → refactor** development cycle
- Build a small, testable **command-line Python application**
- Work with **healthcare-themed scoring logic**

> ⚠️ **Important disclaimer**  
> All healthcare examples in this exercise are **educational only** and **must not** be used for real clinical decision-making.

---

## Learning Objectives

By the end of this exercise, you should be able to:

1. Explain and apply **Test-Driven Development**
2. Write effective **unit tests that define software behavior**
3. Use **Copilot Agent Mode responsibly** as an implementation assistant
4. Separate **business logic** from **CLI parsing logic**
5. Reason about **edge cases, boundary conditions, and invalid input**
6. Maintain confidence when refactoring code because tests protect behavior

---

## What You Are Building

You will build a Python CLI tool called:

```
clinical-risk
```

The tool calculates **point-based clinical risk scores** and prints results as JSON.

### Example usage

```bash
python -m clinical_risk risk qsofa --rr 24 --sbp 95 --ams true
```

Output:
```json
{"name": "qSOFA", "score": 3}
```

---

## Project Structure (Provided)

You are given **scaffolding only**. All implementation is intentionally incomplete.

```
clinical-risk-cli/
  clinical_risk/
    __init__.py
    cli.py
    risk_scores.py
  tests/
    test_qsofa.py
    test_chadsvasc.py
  README.md
```

---

## Rules of Engagement

To preserve the learning goals of this exercise:

✅ **You must write all tests yourself**  
✅ **Tests define the required behavior**  
✅ **Copilot Agent may implement production code only**  
❌ **Copilot Agent may not modify test files**

If your tests are weak, your software will be weak—especially when using AI.

---

## How to Work Through the Exercise

You will complete the exercise in **three development cycles**.

Each cycle follows the **TDD loop**:

> **Red → Green → Refactor**

---

## Cycle 1: qSOFA Score

### Step 1: Write Tests (RED)

Open `tests/test_qsofa.py` for editing.

Write unit tests that define:
- Expected scoring behavior
- Boundary conditions
- Invalid input handling

Run tests from the TERMINAL:

```bash
cd clinical-risk-cli
python -m unittest tests/test_qsofa.py
```

✅ Tests should **fail** at this stage.

---

### Step 2: Implement with Copilot Agent (GREEN)

Use **Copilot Agent Mode** in VS Code.

Suggested prompt:

> Implement `qsofa_score` in `risk_scores.py` so that all tests in `test_qsofa.py` pass.  
> Do not modify tests.  
> Validate inputs and raise `ValueError` for invalid values.

What you must do:
- Review the agent’s plan
- Inspect the generated code
- Run tests locally (`python -m unittest`)
- Fix issues if needed

✅ Tests should now pass.

---

### Step 3: Refactor Safely (REFACTOR)

Suggested prompt:

> Refactor `qsofa_score` to improve readability and reduce duplication while keeping all tests passing.

Your tests now protect you from breaking behavior.

---

## Cycle 2: CHA₂DS₂‑VASc Score

Repeat the same process using `tests/test_chadsvasc.py`.

Your tests should include:
- Age-based scoring rules
- Multiple risk factor combinations
- Edge cases (e.g., invalid age)
- Logical consistency (adding risk factors should not reduce score)

Again:
1. Write tests
2. Confirm failure
3. Use Copilot Agent to implement
4. Refactor confidently

---

## How to Run All Tests

From the project root:

```bash
python -m unittest
```

All tests must pass.

---

## Validate the Applicaton
```bash
python -m clinical_risk risk qsofa --rr 24 --sbp 95 --ams yes
python -m clinical_risk risk chadsvasc --age 75 --female yes --chf yes --htn yes --dm yes --stroke yes --vascular yes
```

## Using Copilot Agent Effectively (and Safely)

Copilot Agent is powerful—but **tests are your guardrails**.

Best practices:
- Treat the agent as a **junior developer**
- Never accept code you don’t understand
- Ask the agent to explain decisions after implementation
- Add a new test to confirm behavior if you are unsure

Reflection questions you should be able to answer:
- Which test forced this branch of logic?
- What happens if this test is removed?
- What edge case might still be missing?

---

## Reinforcing the Core Concepts

### Why Test-Driven Development?

- Tests clarify requirements **before** coding
- Code becomes easier to design and refactor
- Bugs are caught earlier
- Confidence increases as the codebase grows

### Why Copilot Agent + TDD?

- AI accelerates implementation
- Tests preserve correctness
- You stay in control of design decisions
- Mirrors real-world AI-assisted development workflows

---

## Final Reminder

> **The tests are the specification.**  
> If the tests are wrong or incomplete, the software will be too—no matter how good the AI is.

Good luck, and write the tests first.
