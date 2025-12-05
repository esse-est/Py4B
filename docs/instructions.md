Currently, there are a total of 16 different instructions present in Py4B. This is (at the moment) the maximum available (see [limitations](/limitations/) for further details).

this list is: <br>
` add` - add two numbers <br>
` sub` - subtract two number <br>
` mul` - multiply two numbers <br>
` div` - divide two numbers <br>
` shl` - shift to the left by one bit <br>
` shr` - shift to the right by one bit <br>
` idl` - do nothing until user input <br>
` cop` - copy value at one address to the other <br>
` nop` - nothing- no operation <br>
` brk` - branch to provided address (index of lines of code, starting at 0) <br>
` bif` - brk only when a2 != "0000" <br>
` sac` - inserts the 4bits of a1 to a2 <br>
` and` - bitwise and <br>
` orx` - bitwise or <br>
` out` - output to terminal with various formatting codes <br>
` xor` - bitwise xor <br>

Typically the input for all instructions follows the formatting of:
    `inst a1 a2 > a2`

This means that the instruction will run using the data at the two provided address, writting output to the second. major exceptions to this are: <br>
- SL,SR, BR. Only requires one address <br>
- IDLE, NOP. No required address <br>
