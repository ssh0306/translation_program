import googletrans #구글번역 라이브러리 가져오기

translator = googletrans.Translator() #번역기 객체 생성

inStr = input("번역이 필요한 문장을 입력하시오.: ") #번역이 필요한 문장 넣기

destLang = input("번역할 언어를 선택하세요. 영어(en), 일본어(ja), 한국어(ko)").strip() #번역될 언어 선택 .strip():앞뒤 공백 제거

outStr = translator.translate(inStr, dest = destLang) # 라이브러리를 이용하여 번역

print(f"{inStr} => {outStr.text}") #결과 출력

