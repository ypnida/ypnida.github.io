import os, json

# ✅ 현재 스크립트가 images/ 안에 있을 때의 BASE 경로
BASE = os.path.abspath("cbrk")
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
                    print("📂 Found in folder:", file_list)
                    files = sorted([
                        f for f in file_list
                        if f.lower().strip().endswith((".jpg", ".jpeg", ".png", ".webp")) and not f.startswith("._")
                    ])
                    if files:
                        output[mode][vertical][hangle] = files
                        found = True
                        break
            if not found:
                print(f"⚠️ No images found in {mode}/{vertical}/{{1,2}}/{hangle}")

# 저장
with open("data.js", "w", encoding="utf-8") as f:
    f.write("const DATA = ")
    json.dump(output, f, indent=2)
