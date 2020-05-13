from translate import Translator
translator= Translator(to_lang="ja")

try:
    with open('abc.txt', mode='r') as myfile:
        text=myfile.read()
        translation = translator.translate(text)
        print(translation)
        with open('abcja.txt', mode='w')as myfile1:
            myfile1.write(translation)

except FileNotFoundError as e:
    print("File not found")        


