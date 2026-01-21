# codificador de mensagem (zenit polar)

def zenit_polar_replace(text):
    #entrada da frase e aplicação da codificação
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
    for old, new in replacements:
        text - text.replace(old, new)
        return text

def main():
    #entrada da frase
    frase = "The quick brown fox jumps over the lazy dog"
    frase = frase.title()

    words = frase.split