# CPSC335 Project 2
## Exhaustive Optimized Search vs Dynamic Programming

**Contributors:**
- Nathanel Gries (nathanelgries@csu.fullerton.edu)
- Nevan Nguyen (Nevanem@csu.fullerton.edu)
- Patrick Valera (patrickv@csu.fullerton.edu)


**To execute both DP and exhaustive:**
```bash
chmod +x run.sh
./run.sh
```
**Alternatively, to individually execute:**
```bash
clang++ dp.cpp -o dp
./dp < test.txt
python3 exhaustive.py < test.txt
