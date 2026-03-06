# Working Across Files in Python: Importing From Another Module

In this short guide, you’ll learn how to **call a function defined in one Python file from another file**, how to structure simple projects, when to use `-m`, and how to fix common import errors.

> **You should read/follow this before the first assignment.** It will save you time debugging `ModuleNotFoundError` issues.

---

## 👀 What you’ll learn

- Importing from a **file in the same folder**
- Importing from a **subfolder (package)**
- **Absolute vs. relative** imports (and when to use them)
- Running code **as a module** with `python -m`
- Fixing common errors (`ModuleNotFoundError`, `ImportError`, name shadowing)
- How to run in **VS Code**, **terminal**, and **Jupyter**

---

## 1) Import from a file in the **same folder**

**Layout**
```
project/
├── utils.py
└── main.py
```

**`utils.py`**
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

**`main.py`**
```python
from utils import greet

if __name__ == "__main__":
    print(greet("Coding Enthusiast!"))
```

**Run from `project/`:**
```bash
python main.py
```

---

## 2) Import from a **subfolder (package)**

Add an `__init__.py` so Python treats the folder as a package.

**Layout**
```
project/
├── main.py
└── helpers/
    ├── __init__.py
    └── text_utils.py
```

**`text_utils.py`**
```python
def title_case(s: str) -> str:
    return s.title()
```

**`main.py`**
```python
from helpers.text_utils import title_case

if __name__ == "__main__":
    print(title_case("hello world"))
```

---

## 3) **Relative imports** (inside a package)

Relative imports (with leading dots) are only valid **inside packages**.

**Layout**
```
project/
└── mypkg/
    ├── __init__.py
    ├── main.py
    └── utils.py
```

**`main.py`**
```python
from .utils import greet

if __name__ == "__main__":
    print(greet("team"))
```

Run from the folder *above* `mypkg/`:
```bash
python -m mypkg.main
```

---

## 4) When to use `python -m`

Use `-m` when:
- You have **relative imports** like `from .utils import ...`
- You’re running code **inside a package directory**
- You want the module’s package context set correctly

**Pattern:**
```bash
python -m package_name.module_name
```

---

## 5) Common errors & how to fix them

### ❌ `ModuleNotFoundError`
- Run from the **project root**
- Ensure folders have `__init__.py`
- Check VS Code/IDE working directory

### ❌ `ImportError: attempted relative import with no known parent package`
Run with:
```bash
python -m mypkg.main
```

### ❌ Name shadowing
Avoid naming files after standard libraries (`random.py`, `json.py`, etc.)

---

## 6) Recommended project layouts

**Simple:**
```
project/
├── main.py
└── utils.py
```

**Package:**
```
project/
└── mypkg/
    ├── __init__.py
    ├── main.py
    ├── utils.py
    └── io/
        ├── __init__.py
        └── files.py
```

---

## 7) Environment notes

### VS Code
- Open project root
- Use integrated terminal

### Terminal
- `cd` into project root
- Prefer `python -m`

### Jupyter
```python
import sys, os
sys.path.append(os.path.abspath(".."))
```

---

## 8) Practice

```
demo/
├── main.py
└── tools/
    ├── __init__.py
    └── math_ops.py
```

---

## 9) Troubleshooting checklist
- [ ] Running from root
- [ ] Import path correct
- [ ] `__init__.py` exists
- [ ] Using `python -m` when needed
- [ ] No shadowing of stdlib names
