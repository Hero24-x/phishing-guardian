# models/train_url_model.py
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
from features.url_features import extract_url_features




def train_from_csv(csv_path: str, out_model_path: str = 'models/url_model.pkl'):
"""Expect CSV with columns: url,label (label: 0 benign, 1 phishing)"""
df = pd.read_csv(csv_path)
X_dicts = []
for u in df['url'].astype(str):
X_dicts.append(extract_url_features(u))


v = DictVectorizer(sparse=False)
X = v.fit_transform(X_dicts)
y = df['label'].astype(int).values


clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X, y)


joblib.dump({'vec': v, 'clf': clf}, out_model_path)
print(f"Model saved to {out_model_path}")




if __name__ == '__main__':
import sys
if len(sys.argv) < 2:
print('Usage: python train_url_model.py data.csv [out_model.pkl]')
sys.exit(1)
csv = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else 'models/url_model.pkl'
train_from_csv(csv, out)
