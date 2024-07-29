import re

# Sample text containing email addresses
email_addresses = '''
singye.doe@gmail.com
john09.doe@example.com
jane_smith@companydomainp.private.com
support@service-provider.com
'''

# Regular expression pattern to match email addresses
pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

# Start of Sentence
match = re.match(pattern, email_addresses)
if match:
    print(f"First found email address: {match.group()}")
else:
    print("No email addresses found.")

# Using re.search to find the first occurrence
search = re.search(pattern, email_addresses)
if search:
    print(f"First found email address: {search.group()}")
else:
    print("No email addresses found.")

# Using re.findall to find all occurrences
findall = re.findall(pattern, email_addresses)

print(f'Find all : {findall}')

# Using re.finditer to find all occurrences with match objects
print("All found email addresses with details:")
for match in re.finditer(pattern, email_addresses):
    # print(match.span())
    print(f"Email address: {match.group()} at position {match.start()}-{match.end()}")
