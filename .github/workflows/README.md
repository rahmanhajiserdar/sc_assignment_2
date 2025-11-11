# Issues and Fixes

## Prettier Markdown Formatting

The linter reported that the README.md did not match the required formatting style.  
This was fixed by adding proper spacing, consistent line width, and correct indentation  
to follow Markdown style guidelines.

## ZIZMOR

Needed to add the SHA instead of the actual version number for the GitHub Actions workflow  
to satisfy security requirements.

## Python Black

Extra lines were added between code blocks, and single quotes were replaced with double quotes  
to maintain consistent formatting across the codebase.

## Pylint Resource Management Issues

The linter recommended using `with` for resource-allocating operations:

- The database connection was changed from a manual open/close to a `try/finally` block  
  to ensure proper cleanup.
- The `urlopen(url)` call was wrapped inside a `with` statement to safely manage network resources.

## Do these results match what you found in your previous assignment?

No I felt like these results didn't match too much from the previous assignment. I think using the 
linter and bandit looked for more smaller issues than the bigger coding errors. A lot more focus on
things like spacing, indentation, best practices, as well as more effective and secure ways to write
your code. Hinting at a better way to code making it more safe while still readable.

## Do you think they caught all the vulnerabilities present in the code?

I would like to say so. It caught way more issues than I would've noticed as well as issues that
I didn't even know existed. As far as my knowledge goes with code and what I was able to see I think 
it definitely caught more than what I would've noticed and then some.

## Why is using multiple code scanners better than using one?

I mean simply having more safety measures will always be better. You can't have "too much" security.
Also from my understanding the two code scanners had some specialties of their own. Bandit focuses on 
Python security issues like unsafe function calls, hardcoded passwords while Pylint focuses more on code
quality, style and maintainability like syntax errors.
