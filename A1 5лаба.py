def shorten_text(text):
    while '(' in text and text.find(')') > text.find('('):
        left, right = text.find('('), text.find(')')
        text = text.replace(text[left:right + 1], '')
    return ' '.join(text.split())

text = "Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) (! (!))."
print(shorten_text(text))