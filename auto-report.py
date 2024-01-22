import requests
from io import BytesIO
from PIL import Image
import os
from email.mime.text import MIMEText

urls = ['https://example.com', 'https://example2.com']
images = []

for url in urls:
    # Disable SSL verification
    response = requests.get(url, verify=False)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    images.append(img)

# Save images to files
for i, img in enumerate(images):
    img.save(f'screenshot_{i}.png')

html_content = '<html><body><h1>Screenshots Report</h1><ul>'
for i, img in enumerate(images):
    img_filename = f'screenshot_{i}.png'
    img_url = f'file://{os.path.abspath(img_filename)}'
    html_content += f'<li><img src="{img_url}" alt="Screenshot {i}"></li>'
html_content += '</ul></body></html>'

html_report = MIMEText(html_content, 'html')
with open('screenshots_report.html', 'w') as f:
    f.write(html_report.as_string())
