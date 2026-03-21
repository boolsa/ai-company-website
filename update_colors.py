import os
import glob
import re

directory = 'microve-ai'
html_files = glob.glob(os.path.join(directory, '*.html'))

replacements = [
    (re.compile(r'#FAF9F7', re.IGNORECASE), '#F4F1E8'),
    (re.compile(r'#1E3A5F', re.IGNORECASE), '#1F4E79'),
    (re.compile(r'#E07A5F', re.IGNORECASE), '#C96B3B'),
    (re.compile(r'#C96A4F', re.IGNORECASE), '#A6552B'),
    (re.compile(r'#7A9E7E', re.IGNORECASE), '#6C8261'),
    (re.compile(r'#2D3436', re.IGNORECASE), '#17212B'),
    
    (re.compile(r'rgba\(\s*30\s*,\s*58\s*,\s*95\s*,', re.IGNORECASE), 'rgba(31, 78, 121,'),
    (re.compile(r'rgba\(\s*224\s*,\s*122\s*,\s*95\s*,', re.IGNORECASE), 'rgba(201, 107, 59,'),
    (re.compile(r'rgba\(\s*201\s*,\s*106\s*,\s*79\s*,', re.IGNORECASE), 'rgba(166, 85, 43,')
]

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for pattern, replacement in replacements:
        new_content = pattern.sub(replacement, new_content)
        
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {file_path}")

print(f"Total files updated: {count}")
