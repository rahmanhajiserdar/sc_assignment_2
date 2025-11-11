# Issues and Fixes

## Prettier Markdown Formatting

The linter would report that the README.md did not 
match the required formatting style. Fixed this 
adding the proper spacing, line width, and indentation
to follow markdown file style guidelines.

## ZIZMOR

Needed to add the SHA instead of the actual version number.

## Python Black

Had to add extra lines between each block of code as well 
as changing single quotes to double quotes. Consistent 
use of double quotes instead of single.

## Pylint Resource Management Issues

THe linter told me to use 'with' for resource-allocating
operations. So I changed the manual connection to a 
try-finally block. Also wrapped urlopen(url) inside 
a with statement.
