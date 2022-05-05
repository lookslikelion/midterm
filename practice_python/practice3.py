from googletrans import Translator

translator = Translator()

sentence = input("책을 읽으며 인상 깊었던 구절을 적어주세요: ")

result_en = translator.translate(sentence,'en')
result_de = translator.translate(sentence,'de')

detected = translator.detect(sentence)

print("===========번 역 결 과===========")
print("입력어-",detected.lang,":",sentence)
print("번역어1-",result_en.dest,":",result_en.text)
print("번역어2-",result_de.dest,":",result_de.text)
print("=================================")