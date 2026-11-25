from pathlib import Path

Path('/output').mkdir(exist_ok=True)
Path('/output/entry.txt').write_text('Reusable tote bag, c. 2025. Commemorative replica of the bag left at home.', encoding='utf-8')
