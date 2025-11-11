##parser/email_parser.py
import email
from email import policy
from bs4 import BeautifulSoup
from typing import Dict, List
import re

URL_REGEX = r"(https?://[\w\-\./?%&=+#~:;@,]+)"
def parse_email_from_string(raw_eml: str) -> Dict:
"""Parse an RFC822 raw email and return headers, plain text body, html body, and urls."""
msg = email.message_from_string(raw_eml, policy=policy.default)
headers = dict(msg.items())

plain_parts: List[str] = []
html_parts: List[str] = []

for part in msg.walk():
ctype = part.get_content_type()
if ctype == 'text/plain':
plain_parts.append(part.get_content())
elif ctype == 'text/html':
html = part.get_content()
html_parts.append(html)

plain_body = "\n".join(plain_parts).strip()
html_body = "\n".join(html_parts).strip()

# fallback: if no plain text, try stripping html
if not plain_body and html_body:
soup = BeautifulSoup(html_body, 'html.parser')
plain_body = soup.get_text(separator='\n')

urls = extract_urls(plain_body + "\n" + html_body)

return {
'headers': headers,
'plain_body': plain_body,
'html_body': html_body,
'urls': urls
}

def extract_urls(text: str) -> List[str]:
found = re.findall(URL_REGEX, text, flags=re.IGNORECASE)
# dedupe preserving order
seen = set()
out = []
for u in found:
if u not in seen:
seen.add(u)
out.append(u)
return out
