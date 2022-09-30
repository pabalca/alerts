# alerts

#### Get a telegram bot token using Botfather
https://t.me/botfather

#### Send a message to the bot and get the chat id
```
curl https://api.telegram.org/bot<token>/getUpdates | jq . | less

```

#### Create config.yml in code directory
```
---
tg_api: https://api.telegram.org/
tg_token:
tg_chat_id:
```

### Installation
```
python3 -m virtualenv venv
source venv/bin/activate
pip install -e .
```

#### Example
```
 $ alert --help
Usage: cli.py [OPTIONS] MESSAGE

  Send telegram message to chat <tg_chat_id> using the bot <tg_token>.

Options:
  --config PATH
  --tg_api TEXT
  --tg_token TEXT
  --tg_chat_id TEXT
  --help             Show this message and exit.

 $ alert "hello world"
2022-09-30 15:34:51,687 - root - INFO - Alert hello world sent
```
