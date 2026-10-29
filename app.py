"""
INNOVEX - DEXATHON 2026 (Team ID: DEX26121)
Sathyabama Institute of Science and Technology
Accessible Banking for the Visually Impaired and Elderly
Backend REST API & AI Fraud Detection Service
"""

from flask import Flask, jsonify, request, send_from_directory
import os
import re
import datetime

app = Flask(__name__, static_folder=".")

# Mock Banking Data (Elderly Pensioner Account)
BANK_ACCOUNT = {
    "account_number": "SB-48210992348",
    "masked_account": "•••• •••• 2348",
    "account_holder": "Thiru. S. Ramanathan",
    "category": "Senior Citizen / Pensioner Account",
    "bank_name": "Canara Bank / Union Bank of India",
    "balance": 48250.00,
    "currency": "INR",
    "currency_symbol": "₹",
    "is_frozen": False,
    "guardian_contact": "+91 98401 23456 (Daughter - Priya)",
    "last_updated": datetime.datetime.now().strftime("%d %b %Y, %I:%M %p")
}

BENEFICIARIES = [
    {
        "id": "ben_1",
        "name": "Priya (Daughter)",
        "tamil_name": "பிரியா (மகள்)",
        "account": "•••• 9812",
        "upi_id": "priya.ram@okhdfc",
        "trusted": True,
        "category": "Family",
        "risk_score": 0.02
    },
    {
        "id": "ben_2",
        "name": "Apollo Pharmacy (Medicines)",
        "tamil_name": "அப்பல்லோ மருந்தகம்",
        "account": "•••• 5521",
        "upi_id": "apollo.meds@icici",
        "trusted": True,
        "category": "Healthcare",
        "risk_score": 0.05
    },
    {
        "id": "ben_3",
        "name": "TNEB Electricity Bill",
        "tamil_name": "மின் கட்டணம் (TNEB)",
        "account": "•••• 1102",
        "upi_id": "tneb.chennai@sbi",
        "trusted": True,
        "category": "Utilities",
        "risk_score": 0.01
    },
    {
        "id": "ben_4",
        "name": "Unknown Caller / Prize Claim (Mule Account)",
        "tamil_name": "தெரியாத நபர் / பரிசு கூற்று (மோசடி)",
        "account": "•••• 7731",
        "upi_id": "luckywinner2026@paytm",
        "trusted": False,
        "category": "High Risk",
        "risk_score": 0.94,
        "flag_reason": "Reported to National Cyber Crime Portal (1930) for KYC / Senior Lottery fraud."
    }
]

TRANSACTIONS = [
    {
        "id": "TXN90211",
        "date": "Today, 10:15 AM",
        "title": "Pension Credit (Central Govt)",
        "title_ta": "ஓய்வூதிய வரவு (மத்திய அரசு)",
        "type": "credit",
        "amount": 28500.00,
        "status": "Success",
        "spoken_summary": "Twenty-eight thousand five hundred rupees received as pension credit."
    },
    {
        "id": "TXN89104",
        "date": "Yesterday, 04:30 PM",
        "title": "Apollo Pharmacy (Monthly Meds)",
        "title_ta": "அப்பல்லோ மருந்தகம்",
        "type": "debit",
        "amount": 1450.00,
        "status": "Success",
        "spoken_summary": "One thousand four hundred and fifty rupees paid to Apollo Pharmacy."
    },
    {
        "id": "TXN87321",
        "date": "24 Oct 2026",
        "title": "TNEB Electricity Bill Paid",
        "title_ta": "மின் கட்டணம் செலுத்தியது",
        "type": "debit",
        "amount": 820.00,
        "status": "Success",
        "spoken_summary": "Eight hundred and twenty rupees paid for electricity bill."
    },
    {
        "id": "TXN86440",
        "date": "20 Oct 2026",
        "title": "Transfer from Priya (Daughter)",
        "title_ta": "பிரியாவிடமிருந்து வரவு",
        "type": "credit",
        "amount": 5000.00,
        "status": "Success",
        "spoken_summary": "Five thousand rupees received from Priya."
    }
]

FRAUD_PATTERNS = [
    "lottery", "prize", "gift", "kyc update", "electricity cut", "power disconnect",
    "cbi officer", "police verification", "digital arrest", "urgent transfer", "block account",
    "apk file", "anydesk", "teamviewer", "otp", "pin share"
]


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/api/account", methods=["GET"])
def get_account():
    """Returns current account details and status"""
    return jsonify({
        "status": "success",
        "account": BANK_ACCOUNT,
        "beneficiaries": BENEFICIARIES
    })


@app.route("/api/balance", methods=["GET"])
def get_balance():
    """Returns current balance with audio-ready spoken text"""
    bal = BANK_ACCOUNT["balance"]
    spoken_en = f"Your current bank balance is {int(bal):,} rupees."
    spoken_ta = f"உங்கள் கணக்கு இருப்பு {int(bal):,} ரூபாய் ஆகும்."
    return jsonify({
        "status": "success",
        "balance": bal,
        "currency": "₹",
        "spoken_en": spoken_en,
        "spoken_ta": spoken_ta,
        "is_frozen": BANK_ACCOUNT["is_frozen"]
    })


@app.route("/api/transactions", methods=["GET"])
def get_transactions():
    """Returns recent transactions with spoken summaries"""
    return jsonify({
        "status": "success",
        "transactions": TRANSACTIONS
    })


@app.route("/api/ai-fraud-check", methods=["POST"])
def check_fraud():
    """
    AI Fraud Detection Engine:
    Specifically targets senior citizen cyber fraud patterns highlighted in Problem Statement:
    - Over 1.03 lakh senior citizens reported losses of ₹7,769.63 crore
    - Flags high-risk beneficiary UPIs, extortion keywords (digital arrest, electricity cut, prize money)
    - Detects unusually high amounts (>₹10,000 for elderly profile)
    """
    data = request.json or {}
    recipient = data.get("recipient", "").strip().lower()
    amount = float(data.get("amount", 0))
    note = data.get("note", "").strip().lower()

    risk_score = 0.05
    flags = []

    # 1. Beneficiary Check
    if "winner" in recipient or "lucky" in recipient or "unknown" in recipient or "scam" in recipient:
        risk_score += 0.85
        flags.append("Recipient account flagged on National Cyber Crime Registry (1930).")

    # 2. Senior Citizen High-Amount Anomaly
    if amount > 25000:
        risk_score += 0.40
        flags.append(f"Amount (₹{amount:,.0f}) is unusually high for pensioner spending profile.")
    elif amount > 10000:
        risk_score += 0.25
        flags.append("High-value transaction requires secondary guardian notification.")

    # 3. Known Cyber Fraud Trigger Keywords (Targeting Elderly in India)
    for kw in FRAUD_PATTERNS:
        if kw in note or kw in recipient:
            risk_score += 0.50
            flags.append(f"Contains high-risk scam trigger phrase: '{kw.title()}'.")
            break

    is_high_risk = risk_score >= 0.50

    spoken_warning_en = ""
    spoken_warning_ta = ""
    if is_high_risk:
        spoken_warning_en = "Warning! High fraud risk detected. This transaction matches common cyber scam patterns targeting seniors. We strongly recommend canceling this transfer."
        spoken_warning_ta = "எச்சரிக்கை! அதிக மோசடி ஆபத்து கண்டறியப்பட்டது. இந்த பரிவர்த்தனை மூத்த குடிமக்களை குறிவைக்கும் மோசடியுடன் பொருந்துகிறது. இதை ரத்து செய்ய பரிந்துரைக்கிறோம்."

    return jsonify({
        "status": "success",
        "risk_score": round(min(risk_score, 0.99), 2),
        "is_high_risk": is_high_risk,
        "flags": flags,
        "spoken_warning_en": spoken_warning_en,
        "spoken_warning_ta": spoken_warning_ta,
        "safe_to_proceed": not is_high_risk
    })


@app.route("/api/transfer", methods=["POST"])
def process_transfer():
    """Processes simulated secure transaction with explicit verification"""
    if BANK_ACCOUNT["is_frozen"]:
        return jsonify({
            "status": "error",
            "message": "Account is temporarily frozen for security. Please unfreeze via Guardian SOS."
        }), 403

    data = request.json or {}
    recipient_name = data.get("recipient_name", "Beneficiary")
    amount = float(data.get("amount", 0))
    pin = data.get("pin", "")

    if pin != "1234":
        return jsonify({
            "status": "error",
            "message": "Invalid Security PIN. Transaction declined.",
            "spoken_en": "Incorrect PIN. For your protection, the transaction was canceled.",
            "spoken_ta": "தவறான ரகசிய எண். பாதுகாப்புக்காக பரிவர்த்தனை ரத்து செய்யப்பட்டது."
        }), 401

    if amount <= 0:
        return jsonify({"status": "error", "message": "Invalid transfer amount."}), 400

    if amount > BANK_ACCOUNT["balance"]:
        return jsonify({
            "status": "error",
            "message": "Insufficient account balance.",
            "spoken_en": "You have insufficient funds in your account for this transfer.",
            "spoken_ta": "உங்கள் கணக்கில் போதிய இருப்பு இல்லை."
        }), 400

    # Deduct balance
    BANK_ACCOUNT["balance"] -= amount
    txn_id = f"TXN{datetime.datetime.now().strftime('%M%S%f')[:7]}"
    now_str = datetime.datetime.now().strftime("Today, %I:%M %p")

    new_txn = {
        "id": txn_id,
        "date": now_str,
        "title": f"Transfer to {recipient_name}",
        "title_ta": f"{recipient_name}-க்கு அனுப்பப்பட்டது",
        "type": "debit",
        "amount": amount,
        "status": "Success",
        "spoken_summary": f"{int(amount):,} rupees successfully transferred to {recipient_name}."
    }
    TRANSACTIONS.insert(0, new_txn)

    return jsonify({
        "status": "success",
        "transaction": new_txn,
        "new_balance": BANK_ACCOUNT["balance"],
        "spoken_en": f"Payment successful! {int(amount):,} rupees transferred to {recipient_name}. Your new balance is {int(BANK_ACCOUNT['balance']):,} rupees.",
        "spoken_ta": f"பரிவர்த்தனை வெற்றி! {int(amount):,} ரூபாய் {recipient_name}-க்கு அனுப்பப்பட்டது. உங்கள் புதிய இருப்பு {int(BANK_ACCOUNT['balance']):,} ரூபாய்."
    })


@app.route("/api/sos-freeze", methods=["POST"])
def sos_freeze():
    """Emergency SOS: Freezes account instantly and triggers guardian alert"""
    data = request.json or {}
    freeze_state = data.get("freeze", True)
    BANK_ACCOUNT["is_frozen"] = freeze_state

    status_word = "FROZEN" if freeze_state else "ACTIVE"
    spoken_en = "Emergency SOS Activated. Your bank account is immediately frozen. Cyber fraud protection has notified your guardian Priya." if freeze_state else "Account has been un-frozen and restored to normal operation."
    spoken_ta = "அவசர உதவி செயல்படுத்தப்பட்டது. உங்கள் கணக்கு முடக்கப்பட்டுள்ளது. உங்கள் பாதுகாவலர் பிரியாவுக்கு தகவல் அனுப்பப்பட்டது." if freeze_state else "கணக்கு மீண்டும் இயல்பு நிலைக்கு மீட்டமைக்கப்பட்டது."

    return jsonify({
        "status": "success",
        "is_frozen": BANK_ACCOUNT["is_frozen"],
        "account_state": status_word,
        "guardian_alerted": True,
        "guardian_contact": BANK_ACCOUNT["guardian_contact"],
        "spoken_en": spoken_en,
        "spoken_ta": spoken_ta
    })


@app.route("/api/voice-command", methods=["POST"])
def parse_voice_command():
    """
    Intelligent NLP Command Parser:
    Maps natural English or Tamil phrases to actions:
    - 'What is my balance?' / 'check balance' / 'இருப்பு'
    - 'Send 500 to Priya' / 'பணம் அனுப்பு'
    - 'Read passbook' / 'recent transactions' / 'பரிவர்த்தனைகள்'
    - 'Help' / 'Emergency' / 'SOS' / 'மோசடி'
    """
    data = request.json or {}
    raw_text = data.get("text", "").strip().lower()
    lang = data.get("lang", "en")

    action = "UNKNOWN"
    details = {}

    # Balance queries
    if any(k in raw_text for k in ["balance", "money do i have", "how much", "account balance", "இருப்பு", "பணம் எவ்வளவு"]):
        action = "CHECK_BALANCE"

    # Transfer queries
    elif any(k in raw_text for k in ["send", "pay", "transfer", "அனுப்பு", "பணம் செலுத்த"]):
        action = "TRANSFER"
        # Extract amount if present
        nums = re.findall(r"\d+", raw_text)
        if nums:
            details["amount"] = float(nums[0])
        # Check beneficiary
        if "priya" in raw_text or "மகள்" in raw_text or "daughter" in raw_text:
            details["recipient"] = "Priya (Daughter)"
        elif "apollo" in raw_text or "pharmacy" in raw_text or "மருந்தகம்" in raw_text:
            details["recipient"] = "Apollo Pharmacy (Medicines)"
        elif "electricity" in raw_text or "tneb" in raw_text or "மின்" in raw_text:
            details["recipient"] = "TNEB Electricity Bill"
        elif "prize" in raw_text or "unknown" in raw_text or "lucky" in raw_text:
            details["recipient"] = "Unknown Caller / Prize Claim (Mule Account)"

    # Passbook / statement
    elif any(k in raw_text for k in ["passbook", "transaction", "statement", "history", "recent", "விவரங்கள்", "அறிக்கை"]):
        action = "PASSBOOK"

    # SOS / Fraud / Help
    elif any(k in raw_text for k in ["help", "fraud", "scam", "freeze", "emergency", "sos", "மோசடி", "அவசரம்", "உதவி"]):
        action = "SOS_FREEZE"

    # Confirm / Cancel
    elif any(k in raw_text for k in ["confirm", "proceed", "yes", "சரி", "ஆம்"]):
        action = "CONFIRM"
    elif any(k in raw_text for k in ["cancel", "stop", "no", "ரத்து", "வேண்டாம்"]):
        action = "CANCEL"

    return jsonify({
        "status": "success",
        "action": action,
        "details": details,
        "input_text": raw_text
    })


if __name__ == "__main__":
    print("=" * 60)
    print("Accessible Banking for Visually Impaired and Elderly")
    print("Team INNOVEX - DEXATHON 2026 (Team ID: DEX26121)")
    print("Server running at: http://localhost:5000")
    print("=" * 60)
    app.run(host="0.0.0.0", port=5000, debug=True)
