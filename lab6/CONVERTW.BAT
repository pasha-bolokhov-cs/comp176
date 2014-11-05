@echo off
:loop
  choice /n /c 0123456789ABCDEFQ /m "Enter a hexadecimal digit (0-F or Q to end):"
  if ERRORLEVEL 1 set guess=0   0000    0       0
  if ERRORLEVEL 2 set guess=1   0001    1       1
  if ERRORLEVEL 3 set guess=2   0010    2       2
  if ERRORLEVEL 4 set guess=3   0011    3       3
  if ERRORLEVEL 5 set guess=4   0100    4       4
  if ERRORLEVEL 6 set guess=5   0101    5       5
  if ERRORLEVEL 7 set guess=6   0110    6       6
  if ERRORLEVEL 8 set guess=7   0111    7       7
  if ERRORLEVEL 9 set guess=8   1000    10      8
  if ERRORLEVEL 10 set guess=9  1001    11      9
  if ERRORLEVEL 11 set guess=10 1010    12      A
  if ERRORLEVEL 12 set guess=11 1011    13      B
  if ERRORLEVEL 13 set guess=12 1100    14      C
  if ERRORLEVEL 14 set guess=13 1101    15      D
  if ERRORLEVEL 15 set guess=14 1110    16      E
  if ERRORLEVEL 16 set guess=15 1111    17      F
  if ERRORLEVEL 17 goto stop
  echo The decimal, binary, octal, and hex values are %guess%.
goto loop

:stop
echo Thanks for playing.
