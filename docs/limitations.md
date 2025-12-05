Shockingly, working with 4 bit address for... everything causes several limitations. <br>

this includes: <br>
 - only supporting numbers 0-15 per register <br>
 - maximum register amount of 16 <br>
 - maximum instruction amount of 16 <br>

currently in the works is a multiple 4b address system to fix this problem. this would drastically scale capabilities, effectively giving each bit 2 more states. <br>

a hypothetical 4bx2 array would have 256 items, 4bx3 1296, 4bx4 4096, etc etc. exponential scaling, and large numbers? in my 4b fake cpu?