import logging
import os
import sys

import click

from alerts.utils import load_config, send_message


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

    res = send_message(tg_api, tg_token, tg_chat_id, message)

    if res["ok"]:
        logging.info(f"Alert {message} sent")
    else:
        logging.error(f"Failed to send alert {message}")


if __name__ == "__main__":
    cli()
