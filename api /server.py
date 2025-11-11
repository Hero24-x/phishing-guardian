# api/server.py
from flask import Flask, request, jsonify
import os
from parser.email_parser import parse_email_from_string
from models.detect import URLScorer


app = Flask(__name__)


# lazy load scorer
SCORER = None




def get_scorer():
global SCORER
if SCORER is None:
try:
SCORER = URLScorer()
except Exception as e:
print('Warning: URL model not loaded:', e)
SCORER = None
return SCORER




@app.route('/analyze', methods=['POST'])
def analyze():
# accept file upload (eml) or raw text
if 'file' in request.files:
raw = request.files['file'].read().decode('utf-8', errors='ignore')
else:
raw = request.get_data(as_text=True)


parsed = parse_email_from_string(raw)
urls = parsed.get('urls', [])


scorer = get_scorer()
url_results = []
for u in urls:
if scorer:
try:
url_results.append(scorer.score(u))
except Exception as e:
url_results.append({'url': u, 'error': str(e)})
else:
url_results.append({'url': u, 'error': 'No model loaded'})


response = {
'headers': parsed.get('headers', {}),
'urls': url_results,
'plain_body': parsed.get('plain_body', '')[:2000]
}
return jsonify(response)




if __name__ == '__main__':
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=True)
