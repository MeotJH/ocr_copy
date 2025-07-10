# OCR Clipboard Watcher (Python + pytesseract)

Windows 환경에서 `클립보드에 복사된 이미지`를 자동으로 OCR(문자 인식)하여  
텍스트로 변환, 곧바로 복사(Ctrl+V)할 수 있도록 해주는 실전 스크립트입니다.

---

## ✅ 주요 특징

- Windows에서 스크린샷(`Win+Shift+S` 등)이나 이미지 복사 시 자동 인식
- 한글/영문 모두 지원 (`kor+eng`)
- 줄 맞춤/줄 바꿈 최대한 원본에 가깝게 복원 (코드/SQL에 강함)
- OCR 결과 텍스트가 바로 클립보드에 복사됨 (즉시 붙여넣기 가능)

---

## 🚩 설치 방법

### 1. Python 패키지 설치

아래 명령어를 **터미널(cmd, PowerShell, 또는 Anaconda Prompt)**에 입력

```bash
pip install pillow pytesseract pyperclip
2. Tesseract OCR 엔진 설치
공식 사이트:
https://github.com/tesseract-ocr/tesseract

Windows용 설치 파일 (추천):
https://github.com/UB-Mannheim/tesseract/wiki
