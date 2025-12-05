Currently, there are a total of 16 different instructions present in Py4B. This is (at the moment) the maximum available (see [limitations](/limitations/) for further details).

this list is:
` add` - add two numbers
` sub` - subtract two number
` mul` - multiply two numbers
` div` - divide two numbers
` shl` - shift to the left by one bit
` shr` - shift to the right by one bit
` idl` - do nothing until user input
` cop` - copy value at one address to the other
` nop` - nothing- no operation
` brk` - branch to provided address (index of lines of code, starting at 0)
` bif` - brk only when a2 != "0000"
` sac` - inserts the 4bits of a1 to a2
` and` - bitwise and
` orx` - bitwise or
` out` - output to terminal with various formatting codes
` xor` - bitwise xor

Typically the input for all instructions follows the formatting of:
    `inst a1 a2 > a2`

This means that the instruction will run using the data at the two provided address, writting output to the second. major exceptions to this are:
- SL,SR, BR. Only requires one address
- IDLE, NOP. No required address
