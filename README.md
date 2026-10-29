# 🏦 Accessible Banking for the Visually Impaired and Elderly
### **DEXATHON 2026 — Sathyabama Institute of Science and Technology**
* **Team Name:** INNOVEX
* **Team ID:** DEX26121
* **Theme:** FinTech & EdTech
* **PS Category:** Software

---

## 🎯 Executive Summary & Problem Addressed
In India alone (2025 data):
* Over **1.03 lakh senior citizens** reported cyber fraud losses.
* Combined financial losses reached **₹7,769.63 crore**.
* Persons with visual impairments and senior citizens face extreme barriers with conventional banking apps (tiny fonts, complex menus, lack of continuous screen-reader feedback, vulnerability to phone scammers and digital arrest fraud).

**INNOVEX Solution:**
A voice-first, high-contrast, AI fraud-shielded accessible banking platform that empowers visually impaired individuals and senior citizens to bank independently with 100% confidence.

---

## 🚀 Key Innovations Implemented in This Prototype

1. **🎙️ Voice-First Natural Interaction (Speech-to-Text & Text-to-Speech)**
   * Full bilingual voice interaction in **English** and **தமிழ் (Tamil)**.
   * Hands-free or 1-tap operation with massive touch targets (80px+ tremor-friendly buttons).
   * **Web Audio API Sound Synthesizer**: Distinct audio earcons for mic active, completion chimes, warning sirens, and tactile keypad clicks (accessible for 100% blind users).

2. **🤖 AI Cyber Fraud Detection & Senior Scam Shield**
   * Real-time anomaly detection against common cyber fraud tactics targeting senior citizens in India:
     * **Mule Account Blacklist**: Intercepts transfers to suspicious recipient UPI handles reported on the National Cyber Crime Portal (Helpline 1930).
     * **High-Amount Spending Anomaly**: Flags sudden large transfers (>₹10,000 / ₹25,000) for pensioner accounts.
     * **Scam Keyword Detection**: Detects coercion terms like *lottery, electricity disconnection, KYC update, digital arrest, APK installation*.
     * **Audible Alarm & Guidance**: Plays an alert tone and audibly warns the user in English/Tamil: *"Warning: Over 1 lakh seniors lost money to similar calls. Never transfer money under pressure."*

3. **👁️ WCAG 2.2 AAA Accessibility Suite**
   * **High-Contrast Modes**:
     * Low-Vision Gold on Black (High contrast standard)
     * Navy Blue & High-Visibility White
     * Senior Soft Light (Glare-reduction mode)
   * **Font Scaling**: 100%, 115%, 135%, 155% with automatic layout reflow.
   * **Screen-Reader Audio Assistant**: Automatically narrates every focused button and tile out loud on hover, tab navigation, or arrow keys.
   * **Privacy Masking**: Balance masking with audio narration controls to protect from shoulder-surfing.

4. **🔒 Explicit Voice Confirmation & Privacy PIN**
   * Requires clear verbal and tactile verification: *"You are sending ₹500 to Priya. Say Confirm to proceed, or Cancel to go back."*
   * Distinct tone numeric keypad where each digit produces a unique audio frequency, allowing blind users to input PINs securely without the number being spoken aloud.

5. **🚨 1-Tap Emergency SOS & Account Freeze**
   * Instantly freezes outgoing bank transactions with one touch or voice command ("Help" / "Scam alert").
   * Automatically simulates alerting emergency contacts (e.g., Daughter Priya) and the National Cyber Crime helpline 1930.

---

## 🛠️ Technical Architecture (Slide 3 Mapping)

```
[ User (Visually Impaired / Elderly) ]
         │ (Voice or Touch Input - English & Tamil)
         ▼
[ Accessible Frontend Layer (WCAG AAA) ]
   ├── High-Contrast Dynamic CSS Themes
   ├── Tremor-Tolerant 80px+ Touch Grid
   └── Web Audio API Earcon Synthesizer (Chimes / Sirens / Keypad Tones)
         │
         ▼
[ Voice & Accessibility Engine ]
   ├── Speech-to-Text (Web Speech API)
   ├── Text-to-Speech (window.speechSynthesis with rate tuning)
   └── Bilingual Voice Command Parser
         │
         ▼
[ Security & Safety Layer ]
   ├── AI Fraud Detection Engine (Heuristics + Keyword NLP)
   ├── Explicit Voice Confirmation ("Confirm" or "Cancel")
   ├── Privacy Scrambled Keypad
   └── Instant SOS Account Freeze Protocol
         │
         ▼
[ Python Flask Backend & Mock Banking API ]
   ├── GET /api/balance
   ├── GET /api/transactions
   ├── POST /api/transfer
   ├── POST /api/ai-fraud-check
   └── POST /api/sos-freeze
```

---

## ⚡ How to Run the Prototype

### Option 1: Instant Standalone (No setup required!)
Simply open `index.html` in any modern web browser (Google Chrome, Microsoft Edge, Brave, Firefox):
```
Double click: index.html
```
* Works 100% offline.
* All voice recognition, speech synthesis, sound effects, AI fraud simulation, and transactions run instantly in the browser.

### Option 2: Full-Stack Flask Backend
1. Double-click `run_demo.bat` (or execute `python app.py`).
2. The server will start at:
   ```
   http://localhost:5000
   ```
3. The browser will automatically open to the live banking app.

---

## 🎤 3-Minute Hackathon Pitch & Live Demo Script

When presenting to the judges:

1. **Introduction (30s):**
   * *"Good day judges! We are Team INNOVEX representing Sathyabama Institute. In 2025 alone, over 1.03 lakh Indian senior citizens lost ₹7,769 crore to cyber fraud. Today, we present **Drishti Bank** — an accessible, voice-guided, AI-protected banking system for the elderly and visually impaired."*

2. **Live Voice Balance Check (45s):**
   * Press `Spacebar` (or tap the Giant Yellow Button) and say:
     > **"What is my balance?"**
   * The system responds with audio: *"Your current bank balance is 48,250 rupees."*
   * Switch language to Tamil (`தமிழ் / English` button) to demonstrate regional language inclusivity:
     > **"எனது கணக்கு இருப்பு என்ன?"**

3. **Demonstrating AI Fraud Detection in Action (60s):**
   * Tap **Send Money** -> Select the flagged recipient **"Unknown Caller / Prize Claim"** (or click the test button `"Send ₹25,000 to Prize Scam"`).
   * **Judge Impact Moment:** The siren sound triggers, a high-contrast warning flashes, and the voice warns:
     > *"Warning! High fraud risk detected. This recipient was flagged on National Cyber Crime Helpline 1930 for senior lottery fraud."*
   * Explain how this directly prevents the ₹7,769 crore fraud crisis highlighted in Slide 2.

4. **Demonstrating Safe Transfer & Audio Confirmation (30s):**
   * Select **Priya (Daughter)** -> Choose ₹500.
   * System reads explicit audio confirmation: *"Please confirm: You are sending 500 rupees to Priya."*
   * Enter PIN `1 2 3 4` -> Success chime plays, transaction receipt is spoken aloud, balance updates dynamically!

5. **Emergency SOS (15s):**
   * Say `"Help scam emergency"` or tap **Anti-Scam & SOS**.
   * Account instantly freezes, blocking all unauthorized withdrawals and notifying the guardian.

---

## 📚 References & Compliance
* **Web Content Accessibility Guidelines (WCAG 2.2 AAA)**
* **National Cyber Crime Reporting Portal (Helpline 1930)**
* **Tata Consultancy Services (TCS) Accessibility Research**
* **Union Bank of India & Bank of Baroda Inclusive Digital Banking Initiatives**
* **Journal of Medical Internet Research (JMIR) Elder Accessibility Findings**
