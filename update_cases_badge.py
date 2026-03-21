import os
import glob

files = glob.glob('/Users/boolsa/Desktop/Projects/12_GoCustom_Comprehensive/microve-ai/cases*.html') + glob.glob('/Users/boolsa/Desktop/Projects/12_GoCustom_Comprehensive/microve-ai/cases/*.html')

old_html = '<div class="nav-brand">\n        <a href="index.html" class="nav-logo">microve<span class="nav-logo-tld">.ai</span></a>\n      </div>'
old_html2 = '<a href="../index.html" class="nav-logo">microve<span class="nav-logo-tld">.ai</span></a>'

new_html = '''<div class="nav-brand flex items-center">
        <a href="index.html" class="nav-logo">microve<span class="nav-logo-tld">.ai</span></a>
        <div class="hidden lg:flex items-center gap-1.5 ml-1.5 opacity-80 hover:opacity-100 transition-opacity" title="Microve = Micro + Improvement">
          <span class="font-mono text-[0.6rem] font-semibold tracking-[0.1em] text-[#1F4E79] bg-[#1F4E79]/5 border border-[#1F4E79]/20 px-2 py-0.5 rounded uppercase shadow-sm">Micro</span>
          <svg class="w-3 h-3 text-stone/40" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"/></svg>
          <span class="font-mono text-[0.6rem] font-semibold tracking-[0.1em] text-[#C96B3B] bg-[#C96B3B]/5 border border-[#C96B3B]/20 px-2 py-0.5 rounded uppercase shadow-sm">Improvement</span>
        </div>
      </div>'''

new_html2 = '''<div class="flex items-center">
        <a href="../index.html" class="nav-logo">microve<span class="nav-logo-tld">.ai</span></a>
        <div class="hidden lg:flex items-center gap-1.5 ml-1.5 opacity-80 hover:opacity-100 transition-opacity" title="Microve = Micro + Improvement">
          <span class="font-mono text-[0.6rem] font-semibold tracking-[0.1em] text-[#1F4E79] bg-[#1F4E79]/5 border border-[#1F4E79]/20 px-2 py-0.5 rounded uppercase shadow-sm">Micro</span>
          <svg class="w-3 h-3 text-stone/40" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"/></svg>
          <span class="font-mono text-[0.6rem] font-semibold tracking-[0.1em] text-[#C96B3B] bg-[#C96B3B]/5 border border-[#C96B3B]/20 px-2 py-0.5 rounded uppercase shadow-sm">Improvement</span>
        </div>
      </div>'''

for file_path in files:
    with open(file_path, 'r') as f:
        content = f.read()
    
    if file_path.endswith('cases.html'):
        if '<div class="nav-brand">' in content and 'Microve = Micro' not in content:
            content = content.replace(old_html, new_html)
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Updated {file_path}")
    else:
        if '<a href="../index.html"' in content and 'Microve = Micro' not in content:
            content = content.replace(old_html2, new_html2)
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Updated {file_path}")
