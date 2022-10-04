import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# 음성인식(듣기,STT)
def listen(recognizer, audio):
    try:
    #구글 API 사용, 하루 50회로 제한
        text=recognizer.recognize_google(audio,language='ko')
        print('[최정선]',text)
        answer(text)

    except sr.UnknownValueError:
        print('인식 실패') #음성인식 실패한 경우
    except sr.RequestError as e:
        print('요청 실패:{0}'.format(e)) #API key오류, 네트워크 단절 등

# 대답
def answer(input_text):
    answer_text=''
    if '안녕' in input_text:
        answer_text='저도 반가워요.'
    if '이름' in input_text:
        answer_text='제 이름은 최정선이에요.'
    elif '날씨' in input_text:
        answer_text='오늘 강원도 날씨는 비가 내리고 있어요.'
    elif '환율' in input_text:
        answer_text="원 달러 환율은 1400원입니다."
    elif '고마워' in input_text:
            answer_text="별말씀을요."
    elif '정지'  in input_text:
        answer_text="장비를 정지합니다. 감사합니다."
        #백그라운드 종료
        stop_listening(wait_for_stop=False)
    else:
        answer_text="다시 말씀해 주세요."
    speak(answer_text)


#소리내어 읽기 (TTS)
def speak(text):
    print('[인공지능]'+text)
    file_name='voice.mp3'
    tts= gTTS(text=text, lang='ko')
    tts.save(f"C:/code/playground/AISpeaker/{file_name}")
    playsound(f"C:/code/playground/AISpeaker/{file_name}")
    if os.path.exists(f"C:/code/playground/AISpeaker/{file_name}"):
        os.remove(f"C:/code/playground/AISpeaker/{file_name}")


r = sr.Recognizer()
m= sr.Microphone()

speak('안녕하세요, 무엇을 도와드릴까요?')
stop_listening= r.listen_in_background(m,listen)

#프로그램 무한 반복
while True:
    time.sleep(0.1)
