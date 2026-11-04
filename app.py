from tts_player import play_korean_tts

if __name__ == "__main__":
    print("=" * 60)
    print("  고성능 로컬 AI 음성 출력 프로그램 (Intel i9 & RTX 4070 최적화)")
    print("=" * 60)
    
    # PowerShell 콘솔창에서 직접 텍스트 입력받기
    user_text = input("변환하실 문장을 입력해주세요: ").strip()
    
    if user_text:
        print("\n[알림] 입력된 텍스트로 음성 출력을 시작합니다...")
        play_korean_tts(user_text)
    else:
        print("[알림] 입력된 텍스트가 없습니다.")