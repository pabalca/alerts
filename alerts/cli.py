import sys
import os
from alerts.utils import load_config
import click
import json
import requests
import os
import logging


@click.command()
@click.option(
    "--config",
    default="config.yml",
    type=click.Path(),
    callback=load_config,
    is_eager=True,
    expose_value=False,
)
@click.argument("message")
@click.option("--tg_api")
@click.option("--tg_token")
@click.option("--tg_chat_id")
def cli(message, tg_api, tg_token, tg_chat_id):
    """
    Send telegram message to chat <tg_chat_id> using the bot <tg_token>.
    """

    # Check that configuration is valid.
    if tg_api is None or tg_token is None or tg_chat_id is None:
        logging.error("Configuration is not valid.")
        sys.exit()

    # Send message.
    try:
        r = requests.post(
            tg_api + tg_token + "/sendMessage",
            params={"chat_id": tg_chat_id, "text": message},
        )
    except Exception as e:
        logging.error(f"Exception {e}")
        sys.exit()

    # Check result.
    res = r.json()
    if res["ok"]:
        logging.info(f"Alert {message} sent")
    else:
        logging.error(f"Failed to send alert {message}")


if __name__ == "__main__":
    cli()
