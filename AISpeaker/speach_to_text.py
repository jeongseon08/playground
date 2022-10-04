#STT (Speech To Text)
import speech_recognition as sr

#  마이크로부터 음성 듣기
r = sr.Recognizer()
with sr.Microphone() as source:
    print('듣고 있어요')
    audio = r.listen(source) #마이크로부터 음성 듣기

# 파일로부터 음성 불러오기: mp3파일은 불가능
#r= sr.Recognizer()
#with sr.AudioFile('sample.wav') as source:
#    audio = r.record(source)

#try:
    #구글 API 사용, 하루 50회로 제한
#    text=r.recognize_google(audio,language='en-US')
#    print(text)

#except sr.UnknownValueError:
#    print('인식 실패') #음성인식 실패한 경우
#except sr.RequestError as e:
#    print('요청 실패:{0}'.format(e)) #API key오류, 네트워크 단절 등

try:
    #구글 API 사용, 하루 50회로 제한
    text=r.recognize_google(audio,language='ko')
    print(text)

except sr.UnknownValueError:
    print('인식 실패') #음성인식 실패한 경우
except sr.RequestError as e:
    print('요청 실패:{0}'.format(e)) #API key오류, 네트워크 단절 등
