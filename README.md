# ReqLint

Quickly lint your python files to detect if you're using requests library without specifying a timeout value

## Why?
- [Nearly all production code should use this parameter in nearly all requests. Failure to do so can cause your program to hang indefinitely](https://docs.python-requests.org/en/latest/user/quickstart/#timeouts)

## Quick Start

### Installation
* `pip install py-reqlint`

### CLI usage
```bash
# Show help text
python -m reqlint --help

# recusively lint all python files in specified directory
python -m reqlint path/to/your/repo -r

# lint only specific files
python -m reqlint somefile.py someotherfile.py
```

### Library usage
```python
from reqlint import ReqLint

with open('your_file.py', 'r') as f:
    code = f.read()

for issue in ReqLint.lint(code):
    print(issue)
```
