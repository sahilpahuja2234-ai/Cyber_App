# 🛡️ CyberApp — Email Phishing Detection Game

> A cybersecurity awareness game built with Python & Pygame, where you act as an employee navigating a simulated inbox and deciding which emails are safe or suspicious.

---

## 🎮 About The Project

**CyberApp** is an interactive educational game designed to teach players how to identify phishing emails, social engineering attacks, and suspicious digital communications. Players open emails in a simulated inbox, inspect sender details, attachments, and content, then decide to **keep** or **report** each one.

Built entirely in Python using [Pygame](https://www.pygame.org/), the game features a sleek dark cyberpunk UI theme with animated neon borders and custom fonts.

> 🚧 **This project is actively under development. More levels covering broader cybersecurity threats are coming soon!**

---
## 📸 Screenshots
<img width="320" height="180" alt="Video Project" src="https://github.com/user-attachments/assets/4fe8ff22-1fb0-4999-b7f2-625fbc878f14" />

<img width="480" height="282" alt="image" src="https://github.com/user-attachments/assets/53f6e456-65d6-4715-bb72-917dd1300aa5" />

<img width="480" height="282" alt="image" src="https://github.com/user-attachments/assets/f0d590ac-2a45-4c9b-bed9-716529fe1b36" />

---
## 🕹️ Gameplay

### Level 1 — Email Inspection ✅ Available Now
<img width="480" height="282" alt="image" src="https://github.com/user-attachments/assets/5fd6f298-8b5a-458e-824e-4b9c2d7d2ffa" />

<img width="480" height="282" alt="image" src="https://github.com/user-attachments/assets/ed9b4863-ebe3-453e-86c2-3e15a927a902" />


- You are presented with **9 emails** in a simulated Gmail-style inbox.
- Open each email and analyze:
  - **Sender address** (internal vs external domain)
  - **Email body** content and urgency cues
  - **Suspicious attachments** (e.g., `.exe` files)
  - **External links** or threats
- Take action:
  - ✅ **Back** — Safe email, dismiss it
  - 🚩 **Report** — Flag it as suspicious

### Scoring
| Action | Points |
|--------|--------|
| Correctly reporting a phishing email | **+20** |
| Correctly dismissing a safe email | **+20** |
| Wrong report on a legitimate email | **-10** |
| Missing a suspicious email | **-10** |

High scores are saved locally in `score.txt`.

---

## 🗺️ Roadmap

CyberApp is a growing project. Here's what's currently available and what's planned:

| Level | Title | Status |
|-------|-------|--------|
| Level 1 | Email Inspection | ✅ Available |
| Level 2 | Suspicious Links & URLs | 🔜 Coming Soon |
| Level 3 | Social Engineering Scenarios | 🔜 Coming Soon |
| Level 4 | Malware & Download Traps | 🔜 Coming Soon |
| Level 5 | Password Security & Data Leaks | 🔜 Coming Soon |

> 💡 Have a level idea? Feel free to open an [Issue](../../issues) or submit a Pull Request!

---

## 📂 Project Structure

```
CyberApp/
│
├── Cyber_APP.py          # Main entry point — game loop & state manager
├── menu.py               # Main menu screen with animated neon border
├── level_1.py            # Level 1 logic, email data, scoring & rendering
├── Score.py              # Score class — tracks current & high score
│
├── Font/
│   ├── Main_menu_font/   # Rajdhani-Bold.ttf
│   └── Level_1_font/     # OpenSans variants
│
├── Graphic/
│   └── Level_1_graphics/ # All PNG assets (frames, buttons, email view)
│
└── score.txt             # Auto-generated high score file
```

---

## ⚙️ Requirements

- Python 3.8+
- Pygame

Install dependencies:

```bash
pip install pygame
```

---

## 🚀 How to Run

```bash
git clone https://github.com/sahilpahuja2234-ai/Cyber_App.git
cd Cyber_App
python Cyber_APP.py
```

---

## 🖥️ Technical Details

- **Resolution:** 1280 × 720 (fixed window)
- **FPS:** 60 (capped via `clock.tick(60)`)
- **Font:** Rajdhani Bold (menu), Open Sans (gameplay)
- **Rendering:** Pygame surface blitting with custom animated border drawing
- **State management:** `game_active` flag switches between menu and level

### Key Modules

| File | Responsibility |
|------|---------------|
| `Cyber_APP.py` | Game loop, event routing, screen state |
| `menu.py` | Animated border, Start/Exit buttons, color constants |
| `level_1.py` | `LevelOne` class — email data, open/inspect/report logic |
| `Score.py` | `SCORE` class — add, deduct, save high score to file |

---

## 🔒 Cybersecurity Concepts Covered

### Currently Taught (Level 1)
- **Phishing email identification**
- **Suspicious sender domain detection**
- **Social engineering red flags** (urgency, threats, unknown senders)
- **Malicious attachment recognition** (`.exe` files in emails)
- **External link danger awareness**

### Coming in Future Levels
- URL spoofing and lookalike domains
- Credential harvesting page detection
- Ransomware delivery mechanisms
- Safe password practices and breach response

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add a new level, improve UI, or suggest new cybersecurity scenarios:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/level-2`)
3. Commit your changes (`git commit -m 'Add Level 2: Suspicious Links'`)
4. Push to the branch (`git push origin feature/level-2`)
5. Open a Pull Request

---

## 📄 License

Fonts used under the [SIL Open Font License (OFL)](OFL.txt).

Project code is open for educational use.

---

## 🙌 Acknowledgements

- Built with [Pygame](https://www.pygame.org/)
- Fonts: [Rajdhani](https://fonts.google.com/specimen/Rajdhani), [Open Sans](https://fonts.google.com/specimen/Open+Sans) via Google Fonts
- Inspired by real-world cybersecurity awareness training platforms

---

<p align="center">
  <i>🔐 Stay cyber-aware. More levels coming soon!</i>
</p>
