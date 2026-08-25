# AI Workflow Comparison: Round 1 vs Round 2

## 1. Prompt Breakdown

* **Round 1 (Vague Prompt):** "Build a simple form with validation"
  * **Result:** Generated basic HTML/Flask code with minimal error handling, generic fields, and standard page-reload behavior.
* **Round 2 (Precise Prompt):** Explicitly specified file targets (`app.py`, `templates/index.html`), regex validation, boundary constraints (age 18–120), JSON response status codes (`400`/`200`), and asynchronous `fetch` requests with inline error containers.
  * **Result:** Produced production-ready, modular code with clear error handling and zero full-page reloads.

## 2. Metrics & Comparison

| Metric | Round 1 (Vague) | Round 2 (Precise) |
| :--- | :--- | :--- |
| **Initial Prompt Effort** | Very Low (~10 words) | High (~150 words) |
| **Code Correctness & Completeness** | Basic / Partial | Complete & Robust |
| **Manual Editing / Fixes Needed** | High (needed manually added validation) | Minimal (worked out of the box) |
| **UI/UX Quality** | Default browser submit | Modern async fetch with inline errors |

## 3. Key Takeaways & Learned Rules

1. **Explicit Constraints Reduce Refactoring:** Detailing input parameters, boundary limits, and response structures upfront prevents iterative fixing cycles later.
2. **Context & File Scope Matter:** Target-specific file references ensure AI models edit precise modules without altering unrelated structures.
3. **Async & UX Guidance:** Explicitly requesting client-side `fetch` and JSON HTTP statuses avoids default HTML page reloads.
4.