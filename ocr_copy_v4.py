import time
from PIL import ImageGrab, Image
import pytesseract
import pyperclip
import hashlib
import io

# Tesseract 경로는 본인 PC 환경에 맞게 수정
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print("🟢 OCR 감시 시작 (클립보드에 이미지 복사 시 자동 텍스트 추출)")

last_hash = None

while True:
    img = ImageGrab.grabclipboard()

    if img:
        # 이미지 중복 방지
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()
        img_hash = hashlib.md5(img_bytes).hexdigest()

        if img_hash != last_hash:
            print("📸 새 이미지 감지 → OCR 처리 중...")

            # 전처리(선택) - 필요 없으면 바로 img 사용
            # img = img.convert('L')  # (선택) 그레이스케일

            # Tesseract로 OCR
            text = pytesseract.image_to_string(
                img, lang='kor+eng',
                config='--psm 6 --oem 3'  # 표준 코드/SQL에 가장 잘 맞는 모드
            )

            # 텍스트를 클립보드에 복사
            pyperclip.copy(text)
            print("✅ 텍스트가 클립보드에 복사되었습니다:\n", text.strip())
            last_hash = img_hash
    else:
        last_hash = None

    time.sleep(1)  # 1초마다 감시 (CPU 낭비 방지)
