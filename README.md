# 🧠 Phishing-guardian Guardian  
**AI-Powered Phishing Detection Framework — catching threats before they click.**
---
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![Security](https://img.shields.io/badge/Security-BlueTeam%20Project-red.svg)]()
---

## 🛡️ Overview

**Phish Guardian** is an **AI-driven phishing detection system** built for blue-teamers and SOC analysts.  
It inspects every layer of an email — **links, headers, IPs, content, and behavior** — using **machine learning**, **NLP**, and **threat-intel correlation** to detect malicious patterns, even zero-day campaigns.

No static rules, no guesswork — this firewall for your inbox *learns, adapts, and explains*.
---

## ✨ Key Features

| Layer | Detection Focus |
|:------|:----------------|
| 🔗 **URL Analyzer** | Lexical + entropy + domain age features detect fake or obfuscated links. |
| 📬 **Header Inspector** | SPF/DKIM/DMARC failures, sender mismatch, relay anomalies. |
| 🧠 **AI Content Model** | NLP + transformers classify tone & intent (“urgent”, “account verify”, etc.). |
| 🌐 **IP / Domain Intel** | Checks local threat feeds, WHOIS, passive DNS, and IP reputation. |
| ⚔️ **Zero-Day Engine** | Autoencoder-based anomaly detection finds unseen phishing patterns. |
| 📊 **Behavioral Analytics** | Monitors sender timing, volume, impersonation attempts. |
| 🧾 **Explainable Results** | Every alert lists top reasons + confidence score. |
| 🧱 **SOC Integration** | REST API + dashboard for incident automation. |

---

## ⚙️ Architecture
```text
[ Email / API Input ]
          ↓
 ┌───────────────────────┐
 │  Parser & Feature Extractor │
 └───────────────────────┘
          ↓
 ┌────────────────────────────┐
 │  ML / NLP Models Ensemble  │
 └────────────────────────────┘
          ↓
 ┌───────────────────────┐
 │  Threat Intel & Sandbox │
 └───────────────────────┘
          ↓
 ┌───────────────────────┐
 │  Policy Engine + API   │
 └───────────────────────┘
          ↓
 [ Analyst Dashboard / SIEM ]
```

## 🚀 Quick Start
# 1. Clone repository
git clone https://github.com/Hero24-x/phishing-guardian.git
cd phishing-guardian
---
# 2. Setup environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
---
# 3. Run API server
python api/server.py
---
# 4. Test with a sample email
curl -X POST -F "file=@tests/sample_email.eml" http://127.0.0.1:5000/analyze
---
📂 Folder Structure
phish-guardian/
├─ ingest/          # Email ingestion
├─ parser/          # Header + body parser
├─ features/        # URL & header features
├─ models/          # ML models (train + detect)
├─ sandbox/         # Optional safe browser analyzer
├─ api/             # REST API + response engine
├─ ui/              # Simple SOC dashboard
├─ intel/           # Local threat feed cache
└─ tests/           # Unit tests + samples
---

⚖️ Safety & Privacy Notes🔹
---
🔹Do not open or sandbox live malicious samples on production machines.
🔹Dynamic analysis runs only inside isolated containers or VMs.
🔹Redact or hash sensitive data before storing for training.
---

🤝 Contributing
Pull requests welcome!
Fork the repo, create a branch (feature/new-detector), commit, and open a PR.
---
🪪 License
Released under the MIT License — free for learning, research, and SOC integration.
---
💬 Author’s Note
Phishing-Guardian isn’t just a filter — it’s a sentinel that listens, learns, and protects.
Built for defenders who believe prevention beats reaction 🧩
---
📛 Author / Maintainer

Shibnath Hansda 
GitHub: @Hero24-x 
---
