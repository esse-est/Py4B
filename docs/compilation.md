the provided compiler is incredibly simple, effectively it just does the following operations: <br>
- translate instructions into opcode <br>
- fill deadspace with empty addresses to prevent underflow <br>
- allow for the use of standard intergers with built in conversion <br>
- translate variable names into addresses in memory <br>
- pushes this to a properly formated ".pyb4c" file <br>

currently it provides the `scriptloader()` function which requires an input file, and an output location.