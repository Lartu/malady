# Malady ![Spyder PetPet](http://images.neopets.com/template_images/spyder_black_dance.gif)
**Malady** is a string-substitution based [esolang](https://en.wikipedia.org/wiki/Esoteric_programming_language). The premise
lies in defining rules within the code that are then used to alter the remaining code until no code is left. A Turing Machine
can be easily implemented in Malady, thus rendering Malady turing-complete.

## How to Install
You can grab a copy of Malady by cloning this repository. Malady requires **Python 3** to run. You may also compile
Malady by running `make && sudo make install`, provided you have **Cython3** and a C compiler installed on your system.

## How to Use
 - A **source file** in Malady is a sequence of lines of text (a textfile).
 - There are two types of lines in Malady: **Rule** lines and **Text** lines.
 - Lines that don't begin with `>` are considered plain **text**.
 - **Rule** lines begin with the character `>`, and follow the format `>conditions|replacements`.
   - Each rule occupies one entire line of code.
   - Conditions are comma separated values that must be matched in any non-rule line (or lines) of the source code
     in order to trigger the rule.
   - If all the condition tokens are found in the source, the replacements are executed.
     - If a condition is preceded by `~`, that token will trigger if it ISN'T found in the source.
   - Replacements are comma sepparated `oldvalue->newvalue` statements.
     - An oldvalue of `*` matches any character.
 - Execution halts when there are no characters left in the source.
 
## Example
Add the values of A and B together in C:
```
>A:I|A:I->A:,C:->C:I
>B:I|B:I->B:,C:->C:I
>~A:I,~B:I|*->
A:IIIII
B:III
C:
```


## License

This Malady interpreter is distributed under the GNU General Public License 3.0. That dancing spider is a Spyder and belongs to Neopets.
