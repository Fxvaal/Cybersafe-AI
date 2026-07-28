print("=" * 50)
print("🛡️ CYBERSAFE AI - ANALYSIS REPORT")
print("Developed by: Saheed Sanusi")
print("=" * 50)

message = input("Paste a message to scan: ").lower()

high_risk_keywords = [
    "winner",
    "prize",
    "urgent",
    "password",
    "verify",
    "bank",
    "account",
    "click",
    "otp",
    "login"
]

caution_keywords = [
    "fee",
    "payment",
    "confirm",
    "enrollment",
    "internship"
]

high_found = []
caution_found = []

for word in high_risk_keywords:
    if word in message:
        high_found.append(word)

for word in caution_keywords:
    if word in message:
        caution_found.append(word)

if len(high_found) >= 4:
    risk = "HIGH"
elif len(high_found) >= 2:
    risk = "MEDIUM"
elif len(high_found) >= 1:
    risk = "LOW"
elif len(caution_found) >= 1:
    risk = "REVIEW"
else:
    risk = "SAFE"

if risk == "HIGH":
     confidence = 95
elif risk =="MEDIUM":
     confidence =75
elif risk == "LOW":
     confidence =55

else:
     confidence = 10

if high_found or caution_found:

    if high_found:
        print("\n🔴 High-Risk Indicators:")
        for word in high_found:
            print(f"✔ {word}")

    if caution_found:
        print("\n🟡 Caution Indicators:")
        for word in caution_found:
            print(f"✔ {word}")

    print(f"\n🚨 Risk Level: {risk}")
    print(f"🤖 AI Confidence: {confidence}%")

    print("\n🧠 Analysis:")
    print(f"The message contains {len(high_found) + len(caution_found)} phishing indicator(s).")
    print("These words are commonly found in phishing or scam messages.")

    print("\n💡 Recommendations:")

    if risk == "HIGH":
        print("• Do not click unknown links.")
        print("• Never share passwords or OTPs.")
        print("• Verify the sender before responding.")

    elif risk == "MEDIUM":
        print("• Verify the sender before taking action.")
        print("• Be cautious before clicking links.")

    elif risk == "LOW":
        print("• Stay alert and verify unexpected requests.")

    elif risk == "REVIEW":
        print("• Research the organization before making payments.")
        print("• Verify the sender's identity.")

else:
    print("\n✅ No suspicious indicators detected.")
    print("🟢 Risk Level: SAFE")
    print(f"🤖 AI Confidence: {confidence}%")

    print("\n🧠 Analysis:")
    print("No known phishing keywords were detected.")

    print("\n💡 Recommendations:")
    print("• Continue to stay alert.")
    print("• Be cautious with unexpected messages.")

print("\nThank you for using CyberSafe AI.")