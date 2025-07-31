import os, json

BASE = os.path.abspath("cbrk")  # 🔧 images/ 폴더 안에 있는 상태에서 실행해야 함
MODES = ["colored", "mono"]
VERTICALS = ["1", "2", "3"]
HANGLES = ["1", "2", "3", "4", "5"]
POSITIONS = ["1", "2"]

output = {}

for mode in MODES:
    output[mode] = {}
    for vertical in VERTICALS:
        output[mode][vertical] = {}
        for hangle in HANGLES:
            found = False
            for pos in POSITIONS:
                sample_path = os.path.join(BASE, mode, vertical, pos, hangle)
                print("CHECKING:", sample_path)
                if os.path.exists(sample_path):
                    file_list = os.listdir(sample_path)

                    # ✅ 유효한 이미지 파일만 필터링
                    files = sorted([
                        f for f in file_list
                        if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
                        and not f.startswith("._")  # 맥에서 생긴 임시파일 제거
                        and not f.startswith(".DS")  # DS_Store 제거
                        and not f.startswith(".")    # 다른 숨김파일 제거
                    ])

                    if files:
                        output[mode][vertical][hangle] = files
                        found = True
                        break

            if not found:
                print(f"⚠️ No valid images in {mode}/{vertical}/{{1,2}}/{hangle}")

# 저장
with open("data.js", "w", encoding="utf-8") as f:
    f.write("const DATA = ")
    json.dump(output, f, indent=2)
