import random 
from words import words
import string

def get_valid_words(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:#kelime listemiz içerisinde - işareti içeren kelimeler de var.onlar yerine başka kelime seçtik.
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase) #alfabenin tüm harflerini büyük harf olarak atadık.
    used_letters = set()

    lives = 6

    print(" Adam asmaca oyununa hoş geldiniz. Oyunu bitirmek için 'exit' yazabilirsiniz.")
    while len(word_letters) > 0 and lives > 0:
        print(f'Kalan can sayınız: {lives} ve daha öncesinde şu Harfleri kullandınız: ', ' '.join(used_letters))
        

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Doğru kelime :',''.join(word_list))

        user_letter = input('Bir harf yazın lütfen: ').upper()
        if user_letter == 'exit':
            print('çıkılıyor..')
            quit(hangman())
            break
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Girmiş olduğunuz harf bulunamadı.')
        elif user_letter in used_letters:
            print('O harfi daha öncesinde kullanmıştınız. Lütfen o harften başka bir harf giriniz')

        else:
            print('Lütfen klavyede bulunan harflerden tahmin ediniz')  
       
    if lives == 0:
         print(f'Kaybettiniz ama pes etmeyiniz, Doğru cevap: {word} ')        
    else:
         print(f'Kazandınız, tebrik ederiz ve doğru cevap sizlerin dediği şekilde: {word}!! ')  
               
hangman()