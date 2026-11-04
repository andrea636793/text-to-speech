import os
import tempfile
import torch
from TTS.api import TTS
import sounddevice as sd
import scipy.io.wavfile as wavfile

def play_korean_tts(text: str):
    # 1. 하드웨어 가속 확인 (RTX 4070 GPU 활용)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[시스템 정보] 하드웨어 가속 장치: {device.upper()} (GPU 성능 극대화 중)")

    if device == "cpu":
        print("[경고] CUDA가 감지되지 않았습니다. CPU로 동작하여 속도가 저하될 수 있습니다.")

    # 2. 고품질 다국어 및 한국어 지원 모델 로드 (XTTS-v2)
    model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
    print(f"[시스템 정보] TTS 모델('{model_name}') 로딩 중... 잠시만 기다려주세요.")
    
    try:
        tts = TTS(model_name=model_name).to(device)
    except Exception as e:
        print(f"[오류] 모델 로드 실패: {e}")
        return

    # 3. 임시 오디오 파일 경로 생성
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        temp_path = temp_audio.name

    try:
        # 모델에 내장된 화자 목록 중 첫 번째 화자를 자동으로 안전하게 선택
        speaker_name = tts.speakers[0] if tts.speakers else None
        print(f"[진행 중] 선택된 화자(Speaker): {speaker_name}")
        print(f"[진행 중] 입력된 텍스트를 한국어 음성으로 변환 중...")
        
        # 음성 합성 수행 및 파일 저장
        tts.tts_to_file(
            text=text,
            file_path=temp_path,
            speaker=speaker_name,
            language="ko"
        )
        print("[진행 중] 음성 변환 완료. 스피커로 출력합니다.")

        # 4. 변환된 음성 소리 출력 (SoundDevice 활용)
        sample_rate, audio_data = wavfile.read(temp_path)
        sd.play(audio_data, sample_rate)
        sd.wait() # 재생이 완전히 끝날 때까지 대기
        print("[완료] 음성 출력이 완료되었습니다.")

    except Exception as e:
        print(f"[오류] 음성 합성 또는 출력 중 문제가 발생했습니다: {e}")

    finally:
        # 5. 임시 파일 정리
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    print("=" * 60)
    print("  고성능 로컬 AI 음성 출력 프로그램 (Intel i9 & RTX 4070 최적화)")
    print("=" * 60)
    
    user_text = input("변환할 한국어 텍스트를 입력하세요: ").strip()
    
    if user_text:
        play_korean_tts(user_text)
    else:
        print("[알림] 입력된 텍스트가 없습니다.")