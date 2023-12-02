A=dp
B=test
C=exhaustive
clang++ $A.cpp -o $A
./$A < $B.txt
python3 $C.py < $B.txt