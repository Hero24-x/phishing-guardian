# models/detect.py
import joblib
from features.url_features import extract_url_features
import os


MODEL_PATH = os.path.join('models', 'url_model.pkl')




class URLScorer:
def __init__(self, model_path: str = MODEL_PATH):
if not os.path.exists(model_path):
raise FileNotFoundError(f"Model not found at {model_path}. Train a model first.")
bundle = joblib.load(model_path)
self.vec = bundle['vec']
self.clf = bundle['clf']


def score(self, url: str) -> dict:
feats = extract_url_features(url)
Xv = self.vec.transform([feats])
prob = float(self.clf.predict_proba(Xv)[0, 1])
pred = int(self.clf.predict(Xv)[0])
return { 'url': url, 'phish_prob': prob, 'predicted_label': pred, 'features': feats }




if __name__ == '__main__':
s = URLScorer()
print(s.score('http://example.com/login'))
