import emoji
import sys

if len(sys.argv) < 2:
    sys.exit()
'''
input = input("Input: ")
emojized = emoji.emojize(input, language = 'alias')
for arg in sys.argv[1:]:
    print(arg, end=" ")

print(f"{emojized}")
'''

emojized = emoji.emojize(sys.argv[1], language = 'alias')
input = input("Input: ")
print(f"{input} {emojized}")
