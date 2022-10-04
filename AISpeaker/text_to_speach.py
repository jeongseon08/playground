#TTS (Text To Speech)
from gtts import gTTS
from playsound import playsound

#영어 텍스트 
text='Hello This is sample english sound.'
file_name='sample.mp3'
tts_en = gTTS(text=text, lang='en')
tts_en.save(f"C:/code/playground/AISpeaker/{file_name}")
playsound(f"C:/code/playground/AISpeaker/{file_name}")

#한글 텍스트
text='저는 기계입니다. 더 자연스러워지고싶습니다.'
file2_name='sample2.mp3'
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(f"C:/code/playground/AISpeaker/{file2_name}")
playsound(f"C:/code/playground/AISpeaker/{file2_name}")

#긴 문장(파일 불러와서 처리하기)
with open("C:/code/playground/AISpeaker/sample.txt",'r',encoding='utf8') as f:
    text =f.read()
file3_name='sample3.mp3'
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(f"C:/code/playground/AISpeaker/{file3_name}")
playsound(f"C:/code/playground/AISpeaker/{file3_name}")
    
