import os
import glob

html_files = glob.glob('/Users/boolsa/Desktop/Projects/12_GoCustom_Comprehensive/microve-ai/**/*.html', recursive=True)

old_html = '<span class="nav-badge">Micro automation</span>'
new_html = '''<div class="hidden lg:flex items-center gap-1.5 ml-1.5 opacity-80 hover:opacity-100 transition-opacity" title="Microve = Micro + Improvement">
          <span class="font-mono text-[0.6rem] font-semibold tracking-[0.1em] text-[#1F4E79] bg-[#1F4E79]/5 border border-[#1F4E79]/20 px-2 py-0.5 rounded uppercase shadow-sm">Micro</span>
          <svg class="w-3 h-3 text-stone/40" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"/></svg>
          <span class="font-mono text-[0.6rem] font-semibold tracking-[0.1em] text-[#C96B3B] bg-[#C96B3B]/5 border border-[#C96B3B]/20 px-2 py-0.5 rounded uppercase shadow-sm">Improvement</span>
        </div>'''

for file_path in html_files:
    with open(file_path, 'r') as f:
        content = f.read()
        
    if old_html in content:
        new_content = content.replace(old_html, new_html)
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
