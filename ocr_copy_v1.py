import time
from PIL import ImageGrab
import pytesseract
import pyperclip
import hashlib
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print("🟢 OCR 감시 시작 (클립보드에 이미지 복사 시 자동 텍스트 추출)")

last_hash = None

while True:
    img = ImageGrab.grabclipboard()

    if img:
        # 이미지 바이트 해시값 비교 (중복 처리 방지)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()
        img_hash = hashlib.md5(img_bytes).hexdigest()

        if img_hash != last_hash:
            print("📸 새 이미지 감지 → OCR 처리 중...")
            text = pytesseract.image_to_string(img, lang='kor+eng')
            pyperclip.copy(text)
            print("✅ 텍스트가 클립보드에 복사되었습니다:\n", text.strip())
            last_hash = img_hash
    else:
        last_hash = None  # 클립보드가 이미지가 아닐 때는 리셋

    time.sleep(1)  # CPU 점유 줄이기 위해 1초 대기
