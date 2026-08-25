# Prompt Engineering Ablation Study: Prompt Ladder

## 1. Baseline Run (Vague Prompt)
* **Prompt:** `Write backend code`
* **Output Excerpt:** Claude asked clarifying questions and generated generic Flask boilerplate code without application context.
* **4-Point Notes:**
  1. **Prompt Change:** None (Weak Baseline).
  2. **Output Change (Result):** Generates generic, uncontextualized code and prompts for clarification.
  3. **What Still Failed:** Lacks specific business logic, database integration, validation rules, and error handling.
  4. **Next Layer to Try:** Clearer Goal.

---

## 2. Version 1 (Layer: Clearer Goal)
* **Prompt:** `Build a Python Flask REST API backend endpoint for user profile settings update.`
* **Output Excerpt:** Generated a multi-file project template (`config.py`, `extensions.py`, routes) with generic CRUD placeholders.
* **4-Point Notes:**
  1. **Prompt Change:** Added a defined end goal (Flask REST API endpoint for user profile updates).
  2. **Output Change (Result):** Shifted from interactive clarifying menus to generating concrete REST API project files.
  3. **What Still Failed:** Uses generic resource names (`/api/items`) rather than real project fields.
  4. **Next Layer to Try:** Real Context.

---

## 3. Version 2 (Layer: Real Context)
* **Prompt:** `Build a Python Flask REST API backend endpoint for user profile settings update. The payload comes from a MySQL database with fields username, email, and age.`
* **Output Excerpt:** Updated the user model and route handler to explicitly read and process `username`, `email`, and `age`.
* **4-Point Notes:**
  1. **Prompt Change:** Specified backend payload context (`username`, `email`, `age` stored in MySQL).
  2. **Output Change (Result):** Replaced generic `item` placeholders with user profile attributes mapped directly to database models.
  3. **What Still Failed:** Accepts invalid payload values (such as non-numeric ages or malformed emails) without error handling.
  4. **Next Layer to Try:** Constraints.

---

## 4. Version 3 (Layer: Constraints)
* **Prompt:** `Great! Now update that endpoint by adding strict backend validation: username must be alphanumeric, email must match regex standard, age must be an integer between 18 and 120, and return HTTP status 400 with descriptive error messages on failure.`
* **Output Excerpt:** Added regex email checks, string type validation, age bound checking (`18 <= age <= 120`), and HTTP `400` JSON responses.
* **4-Point Notes:**
  1. **Prompt Change:** Enforced strict validation rules and HTTP status code standards.
  2. **Output Change (Result):** Stopped allowing invalid payloads and added structured JSON error messages with standard HTTP status codes.
  3. **What Still Failed:** Plain code outputs are functional, but custom output formatting constraints have not been evaluated.
  4. **Next Layer to Try:** Specified Output Format.

---

## 5. Version 4 (Layer: Specified Output Format — Misstep Evaluation)
* **Prompt:** `Now format the entire output response strictly as a single JSON object containing separate string fields for imports, app_setup, route_handler, and database_query rather than standard code blocks.`
* **Output Excerpt:** `{"imports": "from flask import...", "app_setup": "app = Flask...", "route_handler": "..."}`
* **4-Point Notes:**
  1. **Prompt Change:** Forced strict JSON schema output formatting.
  2. **Output Change (Result):** Programmatically structured the output into individual string key-value pairs.
  3. **What Still Failed (Honest Misstep):** The JSON encapsulation inserted escaped newlines (`\n`), broke syntax highlighting, and made code uncopyable directly into VS Code without manual cleanup.
  4. **Next Layer to Try:** Verification Requirements.

---

## 6. Version 5 (Layer: Verification Requirements)
* **Prompt:** `Revert to standard Python code block formatting, and add a full unittest test suite covering valid submissions, missing fields, invalid email format, and age out-of-bounds errors.`
* **Output Excerpt:** Restored standard Python code formatting and included `tests/test_users.py` with 4 complete `unittest` test cases.
* **4-Point Notes:**
  1. **Prompt Change:** Reverted code formatting constraints and requested explicit unit testing suites.
  2. **Output Change (Result):** Added runnable test assertions covering edge cases, missing payload keys, and invalid formats.
  3. **What Still Failed:** None. The output produces fully tested, production-ready backend code.
  4. **Next Layer to Try:** Final reusable prompt finalized.

---

## 7. Final Reusable Production Prompt

```markdown
Role: Senior Python Backend Engineer

Context: You are building a production-ready Flask REST API endpoint that handles user profile setting updates backed by a MySQL database.

Task:
Write a modular Flask endpoint accepting POST requests containing username, email, and age.

Constraints & Business Logic:
1. Input Validation:
   - username: Required, alphanumeric string.
   - email: Required, must match regex email formatting.
   - age: Required, integer between 18 and 120.
2. Error Handling:
   - If any validation fails, return jsonify({"error": "Descriptive error message"}) with HTTP 400.
3. Success Handling:
   - Return jsonify({"message": "Profile updated successfully"}) with HTTP 200.

Verification Deliverable:
Provide standard runnable Python code blocks including:
1. The Flask API route implementation (app.py).
2. A full unittest test suite covering valid payload submission, missing required keys, invalid email formats, and age boundary conditions (<18 or >120).