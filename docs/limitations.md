Shockingly, working with 4 bit address for... everything causes several limitations. <br>

this includes: <br>
 - only supporting numbers 0-15 per register <br>
 - maximum register amount of 16 <br>
 - maximum instruction amount of 16 <br>

As a semi-bandaid solution to at least the register quanitity, memory cells are impelemented. Using `MSH` you can shift your memory cell to the given 4b address. each MSHC(memory shift cell) has 16 registers, resulting in a total of 256 registers. this is still on the low end, but signicantly more usable then the MSHC-less 16.