import glob, re

for f in glob.glob('*.html'):
    content = open(f, 'r', encoding='utf-8').read()
    # Update year
    content = content.replace('© 2025', '© 2026')
    # Remove social links block
    content = re.sub(r'\s*<div class="social-links">.*?</div>', '', content, flags=re.DOTALL)
    open(f, 'w', encoding='utf-8').write(content)
    print(f'Updated: {f}')
