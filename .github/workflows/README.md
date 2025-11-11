# Issues and Fixes

## Prettier Markdown Formatting

The linter reported that the README.md did not match the required formatting style.  
This was fixed by adding proper spacing, consistent line width, and correct indentation to follow Markdown style guidelines.

## ZIZMOR

Needed to add the SHA instead of the actual version number for the GitHub Actions workflow to satisfy security requirements.

## Python Black

Extra lines were added between code blocks, and single quotes were replaced with double quotes to maintain consistent formatting across the codebase.

## Pylint Resource Management Issues

The linter recommended using `with` for resource-allocating operations.  
- The database connection was changed from a manual open/close to a `try/finally` block to ensure proper cleanup.  
- The `urlopen(url)` call was wrapped inside a `with` statement to safely manage network resources.
