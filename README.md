# ChatGPT Telegram Bot: minimal configuration for self-host.
[![Release](https://github.com/tp-open/chatgpt-telegram-bot/actions/workflows/release.yml/badge.svg)](https://github.com/tp-open/chatgpt-telegram-bot/actions/workflows/release.yml)

[Project](https://github.com/tp-open/chatgpt-telegram-bot) fork from [karfly/ChatGPT](https://github.com/karfly/chatgpt_telegram_bot) and customized to minimal configuration for self-host.

## Get started
1. Get your [OpenAI API](https://openai.com/api/) key

2. Get your Telegram bot token from [@BotFather](https://t.me/BotFather)

3. Get MongoDB from [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or [MongoDB](https://www.mongodb.com/try/download/community)
4. Setup [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/)
5. Edit environment [.env](sample.env) file:
```bash
mv sample.env .env
```
6. And now **run**, see [docker-docs](docs/docker-readme.md) for more details
```bash
```bash
docker-compose up --build
```


## Features
- Support health check 
- Low latency replies (it usually takes about 3-5 seconds)
- No request limits
- Message streaming (watch demo)
- GPT-4 support
- Group Chat support (/help_group_chat to get instructions)
- DALLE 2 (choose 👩‍🎨 Artist mode to generate images)
- Voice message recognition
- Code highlighting
- Support chat modes
- Support of [ChatGPT API](https://platform.openai.com/docs/guides/chat/introduction)
- List of allowed Telegram users
- Track $ balance spent on OpenAI API

## News
- *06 Aug 2023*: Added support health check
- *21 Apr 2023*:
    - DALLE 2 support
    - Group Chat support (/help_group_chat to get instructions)
    - 10 new hot chat modes and updated chat mode menu with pagination: 🇬🇧 English Tutor, 🧠 Psychologist, 🚀 Elon Musk, 📊 SQL Assistant and other.
- *24 Mar 2023*: GPT-4 support. Run `/settings` command to choose model
- *15 Mar 2023*: Added message streaming. Now you don't have to wait until the whole message is ready, it's streamed to Telegram part-by-part (watch demo)
- *9 Mar 2023*: Now you can easily create your own Chat Modes by editing `config/chat_modes.yml`
- *8 Mar 2023*: Added voice message recognition with [OpenAI Whisper API](https://openai.com/blog/introducing-chatgpt-and-whisper-apis). Record a voice message and ChatGPT will answer you!
- *2 Mar 2023*: Added support of [ChatGPT API](https://platform.openai.com/docs/guides/chat/introduction).

## Bot commands
- `/retry` – Regenerate last bot answer
- `/new` – Start new dialog
- `/mode` – Select chat mode
- `/balance` – Show balance
- `/settings` – Show settings
- `/help` – Show help

## LICENSE
Copyright © 2023 Thuc Phan
Licensed under the MIT License. See [LICENSE](LICENSE) for details.