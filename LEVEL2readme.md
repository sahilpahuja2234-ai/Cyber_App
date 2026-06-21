# 📧 Level 2 — Email Inspection

## Objective

Review emails and decide whether to:

### Keep

or

### Report

---

## What Players Learn

### Phishing Detection

* Suspicious senders
* Fake domains
* Social engineering
* Malicious attachments
* Scam links

---

## Current Features

### Simulated Inbox

9 realistic emails.

Contains:

* Safe emails
* Internal company emails
* Phishing attempts
* Fake IT alerts
* Social engineering attacks

---

### Email Analysis

Players inspect:

* Sender
* Recipient
* Subject
* Body
* Attachments
* Links

---

### Decision System

| Action         | Result |
| -------------- | ------ |
| Correct Report | +20    |
| Correct Keep   | +20    |
| Wrong Report   | -10    |
| Wrong Keep     | -10    |

---

## Suspicious Indicators

### Attachments

```text
.exe
.scr
.bat
```

### Social Engineering

```text
Act Fast!
Urgent!
Open Immediately!
```

### Suspicious Links

```text
dataexpose-secure.ru
```

### External Domains

```text
gmail.com
protonmail.com
unknown domains
```

---

## Old Version

### Problems

* Static inbox
* Limited feedback
* Less polished presentation

---

## Up comming Version

* Animated inbox loading

* Better email rendering and clickable (inbox, junk, sent box)

* More realistic phishing examples

* Scrollable Mails

---

## Level 2 Cyber Concepts

* Phishing
* Credential Theft
* Malicious Attachments
* Social Engineering
* Email Spoofing
* Threat Awareness

---

# 🏆 Scoring System

| Level   | Correct | Incorrect |
| ------- | ------- | --------- |
| Level 2 | +20     | -10       |

High scores are stored locally.

```text
score.txt
```

---

# 🛠 Technical Features

* Python 3.8+
* Pygame
* Animated UI
* Shared BaseLevel System
* Scrollable Instruction Engine
* Persistent High Score Storage
* Transition Animation System
* Modular Level Architecture

---
