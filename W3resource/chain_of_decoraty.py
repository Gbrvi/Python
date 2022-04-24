# Write a Python program to make a chain of function decorators (bold, italic, underline etc.).

def make_bold(frase):

    def inner():
        return f'<b> {frase()} </b>'
    return inner

def make_italic(frase):

    def inner():
        return f'<i> {frase()} </i>'
    return inner

def make_under(frase):

    def inner():
        return f'<u> {frase()} </u>'
    return inner

@make_under
@make_italic
@make_bold
def sentenca():
    return 'Noc linda'

print(sentenca())