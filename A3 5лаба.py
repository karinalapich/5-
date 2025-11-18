text = input().split()
abbr = ''

for word in text:
    if len(word) >= 3:
        abbr += word[0].upper()

print(abbr)