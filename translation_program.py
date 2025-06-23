import googletrans #구글번역 라이브러리 가져오기

translator = googletrans.Translator() #번역기 객체 생성

inStr = '안녕하세요' #번역이 필요한 문장 넣기

outStr = translator.translate(inStr, dest = 'en', src = 'ko') #라이브러리를 이용해서 번역하기 dest=번역될 언어 src=번역이 필요한 언어

print(f"{inStr} => {outStr.text}") #결과 출력

