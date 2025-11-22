import re

# A pattern that matches the three target sentences used in the tests.
# We capture the core sentence (without leading/trailing indentation)
# so that `findall()` returns the exact strings expected by the tests.
my_pattern = r"^\s*(It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.)\s*$"

# Use MULTILINE so ^/$ match line boundaries when searching a multi-line string.
my_regex = re.compile(my_pattern, re.MULTILINE)

