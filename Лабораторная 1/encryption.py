class Ceasar():
    def __init__(self, key_word, key_word_high_reg, shift):
        self.key_word = key_word
        self.shift = shift
        self.key_word_high_reg = key_word_high_reg
        self.dict = {}

    def gen_dict(self):
        alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                    'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        alphabet_high_reg = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж' , 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
                             'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
        alphabet_upd = alphabet.copy()
        alphabet_high_reg_upd = alphabet_high_reg.copy()
        for i in self.key_word:
            alphabet_upd.remove(i)

        for i in self.key_word_high_reg:
            alphabet_high_reg_upd.remove(i)

        new_alph = [i for i in self.key_word]
        new_alph = new_alph + alphabet_upd

        new_alph_high_reg = [i for i in self.key_word_high_reg]
        new_alph_high_reg = new_alph_high_reg + alphabet_high_reg_upd

        shifted_alph = new_alph[-self.shift:] + new_alph[:-self.shift]
        shifted_alph_high_reg = new_alph_high_reg[-self.shift:] + new_alph_high_reg[:-self.shift]

        self.dict = {i : j for i, j in zip(alphabet+alphabet_high_reg, shifted_alph+shifted_alph_high_reg)}