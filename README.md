# Caesar Cipher

This project lets users encode or decode messages by shifting each letter by a user-defined number of positions in the alphabet. Non-alphabet characters remain unchanged, and the program ensures the shift wraps around the alphabet correctly.

**Technologies Used**

+ ```Python```
+ List and string manipulation
+ User input validation with exception handling

**Features**

+ Encrypt (```encode```) and decrypt (```decode```) messages
+ Supports custom shift values
+ Preserves non-alphabet characters (spaces, punctuation)
+ Handles shifts that exceed the alphabet length (wrap-around)
+ Input validation for direction and shift number

**What Users Can Do**

+ Choose to encode or decode a message
+ Enter the message to process
+ Specify the shift amount for the cipher
+ Receive the transformed message printed to the console

**The Process / How It’s Built**

+ The program prompts the user to select encoding or decoding.
+ It accepts the message and desired shift amount, with validation for numeric input.
+ The caesar function processes each letter:
  + Finds its index in the alphabet list.
  + Adds or subtracts the shift value depending on the direction.
  + Wraps around the alphabet if the shift goes past 'z'.
  + Leaves non-alphabet characters unchanged.
+ The result is joined back into a string and printed. 

**What I Learned**

+ How to implement the Caesar cipher logic with wrap-around shifts.
+ Using ```enumerate()``` to modify list elements by index.
+ Validating user input and handling exceptions.
+ Working with lists and strings for character-level operations.

