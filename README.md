# 🤖 TeleFlow

> **An Intelligent, Context-Aware Telegram AI Userbot powered by Google Gemini**
>
> *Reply naturally, preserve conversation context, and communicate in your own style.*

---

## 📌 Overview

**TeleFlow** is an AI-powered Telegram Userbot that connects your Telegram account with Google's Gemini models. It generates intelligent, context-aware replies by understanding the entire conversation thread, allowing you to respond naturally while maintaining your own communication style.

---

## ✨ Features

- 🧠 **Deep Context Awareness**
  - Reads the complete reply chain.
  - Understands previous messages, sender names, and timestamps.
  - Produces highly contextual responses.

- 🤖 **Powered by Gemini**
  - Uses Google's latest Gemini models.
  - Fast, natural, and intelligent responses.

- 🗣️ **Human-like Responses**
  - Casual conversational style.
  - No robotic formatting.
  - Sounds like you wrote it.

- 🎭 **Custom Persona**
  - Define your own personality and writing style.
  - Easily customize prompts.

- 👻 **Ghost Mode**
  - Deletes the `!ask` command automatically.
  - Sends the generated response directly from your account.

- ⚡ **Smart Reply Generation**
  - `!ask`
    - Automatically joins the conversation.
  - `!ask <instruction>`
    - Generate replies based on your instructions.
  - `!ask I disagree`
    - Writes a complete contextual response.

- 🔒 **Privacy First**
  - OWNER_ID protection.
  - Local session storage.
  - Errors are shown only in the terminal.

---

# 🛠 Tech Stack

- **Python**
- **Telethon**
- **Google Gemini API**
- **python-dotenv**
- **AsyncIO**

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/JoshithPotnuru/TeleFlow.git
cd TeleFlow
```

---

## Configure Environment Variables

Rename

```
.env.example
```

to

```
.env
```

and add:

```env
API_ID=YOUR_TELEGRAM_API_ID
API_HASH=YOUR_TELEGRAM_API_HASH

GEMINI_API_KEY=YOUR_GEMINI_API_KEY
GEMINI_MODEL=gemini-2.5-flash

SESSION_NAME=teleflow_session
OWNER_ID=YOUR_TELEGRAM_USER_ID
```

---

## Get Required Credentials

### Telegram API

Visit:

https://my.telegram.org

Create an application and copy:

- API_ID
- API_HASH

---

### Gemini API Key

Visit:

https://aistudio.google.com

Generate a Gemini API Key and paste it into `.env`.

---

## Run

```bash
python launcher.py
```

On first launch you'll be asked for your Telegram phone number and OTP.

---

# 💬 Usage

| Command | Description |
|----------|-------------|
| `!ask` | Generate a contextual reply to the replied message |
| `!ask <instruction>` | Generate a reply following your instruction |
| `!help` | Display help information |

---

# 📂 Project Structure

```
TeleFlow/
│
├── launcher.py
├── main.py
├── config.py
├── prompt.py
├── text.py
├── requirements.txt
├── .env.example
├── README.md
└── venv/
```

---

# 🔐 Security

- Never commit `.env`
- Never commit `.session` files
- Keep your Gemini API key private
- Restrict usage with `OWNER_ID`

---

# 📖 Example

Reply to any Telegram message:

```
!ask
```

or

```
!ask Roast him politely
```

TeleFlow understands the conversation history and generates a natural reply.

---

# 👨‍💻 Author

**Joshith Potnuru**

GitHub:
https://github.com/JoshithPotnuru

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
