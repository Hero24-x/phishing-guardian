from urllib.parse import urlparse
import math
import tldextract




def url_entropy(s: str) -> float:
if not s:
return 0.0
probs = [s.count(c) / len(s) for c in set(s)]
return -sum(p * math.log2(p) for p in probs)




def extract_url_features(url: str) -> dict:
parsed = urlparse(url)
domain = parsed.netloc or ''
path = parsed.path or ''
query = parsed.query or ''
ext = tldextract.extract(domain)


features = {
'url_length': len(url),
'domain_length': len(domain),
'path_length': len(path),
'has_query': 1 if query else 0,
'num_dots': domain.count('.'),
'subdomain_count': 0 if not ext.subdomain else len(ext.subdomain.split('.')),
'tld': ext.suffix or '',
'entropy': url_entropy(url),
'has_at': 1 if '@' in url else 0,
'uses_ip': 1 if is_ip(domain) else 0
}
return features




def is_ip(host: str) -> bool:
# crude check for IPv4
parts = host.split(':')[0].split('.')
if len(parts) != 4:
return False
try:
return all(0 <= int(p) <= 255 for p in parts)
except ValueError:
return False
