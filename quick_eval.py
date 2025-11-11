# quick_eval.py
import pandas as pd
from sklearn.metrics import classification_report
from features.url_features import extract_url_features
import joblib

df = pd.read_csv('data/sample_urls.csv')
bundle = joblib.load('models/url_model.pkl')
v, clf = bundle['vec'], bundle['clf']

X = [extract_url_features(u) for u in df['url'].astype(str)]
Xv = v.transform(X)
preds = clf.predict(Xv)
print(classification_report(df['label'].astype(int), preds))
