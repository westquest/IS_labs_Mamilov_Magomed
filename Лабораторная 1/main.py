import encryption
import decryption


key_word = 'шифровка'
key_word_high_reg = 'ШИФРОВКА'
shift = 3

with open("text.txt", "r") as f:
    text = f.read()

text = list(text)


def submain():
    x = encryption.Ceasar(key_word, key_word_high_reg, shift)
    x.gen_dict()
    dict = x.dict
    for i, ii in enumerate(text):
        if ii in dict:
            text[i] = dict[ii]

    a = ''
    for i in text:
        a = a + i
    print(a)
    print()
    print()
    print(decryption.freq_method(a))

if __name__ == '__main__':
    submain()

