# Binary Search Practice Problems

This repository contains a collection of Python solutions for binary-search related problems and variants (rotated arrays, frequency counts, insert position, etc.). Each file implements a `Solution` class with a method solving the described problem.

Files

- [Binary_search.py](Binary_search.py) — simple search implementation (returns index or -1)
- [find_1st_and_last_pos_sorted_arr.py](find_1st_and_last_pos_sorted_arr.py) — find first and last positions of target
- [find_minimum_rotation.py](find_minimum_rotation.py) — find minimum (rotation) in rotated sorted array
- [floor_in_sorted_arr.py](floor_in_sorted_arr.py) — floor in sorted array (commented example)
- [number_of_occurrence.py](number_of_occurrence.py) — count occurrences of a value
- [search_in_rotated_sorted_arr.py](search_in_rotated_sorted_arr.py) — search rotated sorted array (index)
- [search_in_rotated_sorted_arr2.py](search_in_rotated_sorted_arr2.py) — search rotated sorted array (bool, handles duplicates)
- [search_insert_pos.py](search_insert_pos.py) — find insert position for target

Quick Usage

- Run functions interactively from Python or a small wrapper script. Example in REPL or a script:

```python
from Binary_search import Solution
print(Solution().search([1,2,3,4], 3))  # expected output: 2
```

Notes

- Some files expect type annotations (e.g., `List`) but do not include imports; add `from typing import List` if needed when running.
- The repository is meant for study and practice; feel free to add tests, examples, or a runner script.

Next steps

- Add unit tests (pytest) and sample inputs in a `tests/` folder.
- Add a small CLI or `run_examples.py` to exercise each solution.
