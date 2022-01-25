def freq_method(text):
    freq_rating = ['о', 'е', 'а', 'и', 'н', 'т', 'с', 'р', 'в', 'л', 'к', 'м', 'д', 'п', 'у', 'я', 'ы', 'ь', 'г',
                   'з', 'б', 'ч', 'й', 'х', 'ж', 'ш', 'ю', 'ц', 'щ', 'э', 'ф', 'ё', 'ъ']
    freq_rating_high_reg = ['О', 'Е', 'А', 'И', 'Н', 'Т', 'С', 'Р', 'В', 'Л', 'К', 'М', 'Д', 'П', 'У', 'Я', 'Ы', 'Ь', 'Г',
     'З', 'Б', 'Ч', 'Й', 'Х', 'Ж', 'Ш', 'Ю', 'Ц', 'Щ', 'Э', 'Ф', 'Ё', 'Ъ']
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    alphabet_high_reg = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
                         'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    freq = []
    for i in alphabet + alphabet_high_reg:
        freq.append(text.count(i))

    dict_1 = {i: j for i, j in zip(alphabet+alphabet_high_reg, freq)}
    dict_1 = dict(sorted(dict_1.items(), key=lambda item: item[1], reverse=True))
    dict_2 = {i:j for i, j in zip(dict_1.keys(), freq_rating+freq_rating_high_reg)}

    text = list(text)

    for i, ii in enumerate(text):
        if ii in dict_2:
            text[i] = dict_2[ii]

    a = ''
    for i in text:
        a = a + i
    return a





