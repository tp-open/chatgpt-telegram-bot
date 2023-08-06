# ChatGPT Telegram Bot

## What is ChatGPT Telegram Bot?
A Telegram bot that integrates with OpenAI's official API to provide a chatbot that can talk about anything you want.

## How to use this image
### start a chatgpt-telegram-bot instance
```shell
docker run --name some-chatgpt \
  -e MONGODB_URI=XX \
  -e TELEGRAM_TOKEN=YY \
  -e OPENAT_API_KEY=ZZ \
  chatgpt-telegram-bot
```
- where `some-chatgpt` is the name you want to assign to your container, and `chatgpt-telegram-bot` is the name of the image you want to run. That's it! You can now enter the container and start using chatgpt-telegram-bot.
- XX is your mongodb uri
- YY is your telegram token
- ZZ is your openai api key
### ... via docker-compose or docker stack deploy
Example docker-compose.yml for chatgpt-telegram-bot:
```yaml
version: "3"

services:
  chatgpt_telegram_bot:
    image: thucpk/chatgpt-telegram-bot
    container_name: chatgpt_telegram_bot
    ports:
      - "8000:8000"
    restart: always
    environment:
      - MONGODB_URI=mongodb://root:example@mongo:27017/
      - TELEGRAM_TOKEN=YY
      - OPENAI_API_KEY=ZZ
      - ALLOWED_TELEGRAM_USERNAMES=["thucpk"]

  mongo:
    image: mongo:5.0.3
    container_name: mongo
    restart: always
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example

  mongo-express:
    image: mongo-express
    restart: always
    ports:
      - 8081:8081
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: root
      ME_CONFIG_MONGODB_ADMINPASSWORD: example
      ME_CONFIG_MONGODB_URL: mongodb://root:example@mongo:27017/
```

## Environment Variables
- `MONGODB_URI` - mongodb uri
- `TELEGRAM_TOKEN` - telegram token
- `OPENAI_API_KEY` - openai api key
- `ALLOWED_USERS` - list of allowed telegram users
- `LISTEN_HOST` - host to listen on (default: 0.0.0.0)
- `LISTEN_PORT` - port to listen on (default: 8000)

## License
Copyright © 2023 Thuc Phan
Licensed under the MIT License. See [LICENSE](https://github.com/thucpk/chatgpt-telegram-bot/blob/master/LICENSE)