import glob
import re

def update_files():
    html_files = glob.glob("*.html")
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace Phone numbers
        content = content.replace('+91 XXXXX XXXXX', '9080 11 22 55')
        content = content.replace('tel:+91XXXXXXXXXX', 'tel:+919080112255')
        content = content.replace('placeholder="+91 XXXXX XXXXX"', 'placeholder="9080 11 22 55"')
        
        # Replace Email
        content = content.replace('info@udhayamconstructions.com', 'udhaymuralidharan@gmail.com')
        content = content.replace('mailto:info@udhayamconstructions.com', 'mailto:udhaymuralidharan@gmail.com')
        
        # Replace Address in footer
        content = content.replace('Chennai, Tamil Nadu, India', '#14/31, Amman Koil Street, Srinivasa Nagar, New Perungalathur, Chennai : 600 063')
        
        # Replace scroll to top button
        scroll_btn_pattern = r'<button id="scroll-top".*?>↑</button>'
        whatsapp_btn = '''<a href="https://wa.me/919080112255" id="whatsapp-btn" target="_blank" aria-label="Chat on WhatsApp" style="position: fixed; bottom: 30px; right: 30px; width: 50px; height: 50px; background: #25D366; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; z-index: 99; box-shadow: 0 4px 14px rgba(37,211,102,0.4); transition: transform 0.3s ease;">
    <svg viewBox="0 0 32 32" fill="currentColor" width="28" height="28"><path d="M16.05 2.15c-7.66 0-13.9 6.24-13.9 13.9 0 2.45.64 4.84 1.85 6.95L2 30l7.2-1.89c2.04 1.11 4.35 1.7 6.8 1.7 7.66 0 13.9-6.24 13.9-13.9S23.71 2.15 16.05 2.15zm8.39 20.08c-.35.98-2.02 1.88-2.8 1.98-.78.11-1.74.28-5.32-1.2-4.32-1.79-7.14-6.2-7.36-6.49-.21-.29-1.76-2.34-1.76-4.46 0-2.12 1.1-3.17 1.5-3.6.38-.41.83-.51 1.11-.51.28 0 .56.01.8.02.26.01.62-.1.95.7 3.51.13.56.42 1.25.48 1.4.07.15.11.33.01.52s-.17.31-.35.5c-.17.19-.36.41-.51.56-.17.17-.35.35-.15.7 1.12.35 2.5 1.13 3.69 2.2 1.18 1.07 1.97 1.82 2.25 2.3.28.49.03.75-.15.93-.17.18-.75.87-.93 1.1-.17.23-.35.19-.66.04-.32-.15-2.01-.74-3.83-2.36-1.42-1.26-2.38-2.82-2.66-3.29-.28-.47-.03-.73.15-.96.16-.2.35-.41.53-.61.18-.21.24-.35.35-.59.12-.24.06-.45-.03-.63-.08-.18-.75-1.81-1.03-2.48-.27-.65-.54-.56-.75-.57-.2-.01-.43-.01-.66-.01zm0 0"/></svg>
  </a>'''
        content = re.sub(scroll_btn_pattern, whatsapp_btn, content)
        
        # Remove scroll-top JS logic
        js_pattern = r"document\.getElementById\('scroll-top'\)\.classList\.toggle\('visible', window\.scrollY > 400\);"
        content = re.sub(js_pattern, "", content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    update_files()
