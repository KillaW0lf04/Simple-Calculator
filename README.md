Calculate
=========

Simple script that is able to parse and solve input formulas from the command line.
This is performed by transforming the formula to postfix (Reverse-Polish) notation.

Contains support for all standard operators including:

* Multiplication
* Division
* Addition
* Subtraction
* Modulus

Ambiguous formulas are solved using standard BODMAS rules. Parentheses are also
supported to specify exact orderings.

