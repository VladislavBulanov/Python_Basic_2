def decrypt_string(string):
    decrypted_string = ''

    for symbol in string:
        if symbol in letters:
            index = letters.index(symbol)
            decrypted_string += letters[index - 1]
        else:
            decrypted_string += symbol

    return decrypted_string


def shift_string(input_string, key):
    shift = key % len(input_string)
    shifted_string = input_string[-shift:] + input_string[:-shift]
    return shifted_string


source_text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm ' \
              'fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj ' \
              'uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj ' \
              'vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ' \
              'ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm ' \
              'omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ' \
              'ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof ' \
              'pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ' \
              'ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu ' \
              'cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( ' \
              'b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe ' \
              'jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

words_list = source_text.split()
decrypted_words_list = []
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
decryption_key = 3

for word in words_list:
    decrypted_word = decrypt_string(word)
    shifted_word = shift_string(decrypted_word, decryption_key)

    if shifted_word.endswith("/"):
        decryption_key += 1
        decrypted_words_list.append(shifted_word)
    else:
        decrypted_words_list.append(shifted_word)

decrypted_text = ' '.join(decrypted_words_list)
decrypted_text = decrypted_text.replace("/ ", ".\n")
decrypted_text = decrypted_text.replace("+", "*")
decrypted_text = decrypted_text.replace("-", ",")
decrypted_text = decrypted_text.replace("(", "'")
decrypted_text = decrypted_text.replace("..", "--")
decrypted_text = decrypted_text.replace('"', "!")

print(decrypted_text)
