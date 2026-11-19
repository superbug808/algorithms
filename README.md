#Algorithms & Data Structures Practice

[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A structured, production-grade collection of algorithmic pattern solutions and data structure implementations. Designed for technical mastery, clean code architecture, and continuous problem-solving.

---

##Repository Architecture

algorithms/
|---python
|	|--- data_structures/            # Core data structures
|	|   |--- arrays_and_strings
|	|	|--- caches
|	|	|--- graphs
|	|	|--- hash_tables
|	|	|--- heaps
|	|	|--- linked_lists
|	|	|--- priority_queues
|	|	|--- stacks_and_queues
|	|	|--- trees
|	|
|	|--- patterns/					# Solutions categorized by core algorithmic patterns
|	|	|--- arrays_and_hashing
|	|	|--- binary_serach
|	|	|--- dynamic_programming
|	|	|--- graphs
|	|	|--- sliding_window
|	|	|--- stack
|	|	|--- trees_bfs_dfs
|	|	|--- two_pointers
|--- README.md


Running Tests Locally

This repository uses pytest for automated test verification.

    Navigate to the language directory:
    Bash

    cd python/

    Activate your virtual environment:
    Bash

    source venv/bin/activate  # Windows: venv\Scripts\activate

    Run the test suite:
    Bash

    pytest -v