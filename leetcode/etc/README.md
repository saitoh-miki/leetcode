## How to start.

### Write code

- Sign in https://leetcode.com/ .
- Select problem and open URL (ex. https://leetcode.com/problems/two-sum/ ).
- Open code.py by Visual Studio Code.
    - if code.py is not exist, execute below for sample.

        `cp sample_code.py code.py`
- Write code as below.

```py
# %% [Number. Title](URL)
...
```

### Convert code

- You can convert code from code.py to each file.

```
poetry run leetcode convert
```

or

```
pip install .
leetcode convert
```

## etc.

- [imported](imported.py)
    - You can use NumPy and SciPy, but not imported.
- [ListNode](list_node.py)
- [TreeNode](tree_node.py)
