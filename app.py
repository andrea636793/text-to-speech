from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3", lang="ko"):
	"""
	텍스트를 입력받아 음성 파일로 저장하는 함수
	"""
	try:
		# gTTS 객체 생성 (언어: 한국어 'ko')
		tts = gTTS(text=text, lang=lang, slow=False)
		
		# mp3 파일로 저장하는
		tts.save(filename)
		print(f"음성 파일이 성공적으로 생성되었습니다: {filename}")
		
	except Exception as e:
		print(f"오류가 발생했습니다: {e}")
        
if __name__ == "__main__":
    print("--- 텍스트 음성 변환 프로그램 ---")
    user_input = input("음성으로 변환할 텍스트를 입력하세요: ")
    
    if user_input.strip():
        text_to_speech(user_input, filename="my_voice.mp3")
    else:
        print("텍스트가 입력되지 않았습니다.")