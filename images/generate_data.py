import os, json

BASE = os.path.abspath("cbrk")  # 🔧 images/ 폴더 안에서 실행
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
            pos_data = {}
            for pos in POSITIONS:
                sample_path = os.path.join(BASE, mode, vertical, pos, hangle)
                print("CHECKING:", sample_path)
                if os.path.exists(sample_path):
                    file_list = os.listdir(sample_path)

                    # ✅ webp 파일만 포함
                    files = sorted([
                        f for f in file_list
                        if f.lower().endswith(".webp")
                        and not f.startswith("._")
                        and not f.startswith(".DS")
                        and not f.startswith(".")
                    ])

                    if files:
                        pos_data[pos] = files

            if pos_data:
                output[mode][vertical][hangle] = pos_data
            else:
                print(f"⚠️ No valid .webp images in {mode}/{vertical}/{{1,2}}/{hangle}")

# 저장
with open("data.js", "w", encoding="utf-8") as f:
    f.write("const DATA = ")
    json.dump(output, f, indent=2)
