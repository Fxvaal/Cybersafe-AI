# 🛡️ CyberSafe AI

## Overview
CyberSafe AI is a Python-based phishing message detection tool that helps users identify suspicious messages by scanning for common phishing keywords.


## Features
- Detects phishing-related keywords
- Displays detected keywords
- Assigns a risk level (SAFE, LOW, MEDIUM, HIGH)
- Provides cybersecurity recommendations
- Simple command-line interface

## Technologies Used
- Python 3
- Visual Studio Code

## How to Run

```bash
python main.py
```

## Example

Input:

```
URGENT! Verify your bank account to claim your prize.
```

Output:

```
Risk Level: HIGH
Detected Keywords:
- urgent
- verify
- bank
- account
- prize
```
## How It Works

CyberSafe AI analyzes text messages by searching for common phishing keywords such as:

- winner
- urgent
- verify
- password
- bank
- account
- click
- prize

The application counts the detected indicators, assigns a risk level, estimates a confidence score, and provides security recommendations.

## Future Improvements

- Machine learning phishing detection
- URL analysis
- Email attachment scanning
- Web interface

## Developer

Saheed Sanusi
