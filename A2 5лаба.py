import re

text = "He jests at scars. That never felt a wound! Hello, friend! Are you OK?"
sentences = re.split(r'(?<=[.!?])\s+', text.strip())

print('\n'.join(sentences))
print(f"Предложений в тексте: {len(sentences)}")