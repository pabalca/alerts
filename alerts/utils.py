import os
import sys
import logging
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def load_config(ctx, param, value):
    if os.path.exists(value):
        # read and parse
        with open(value, "r") as f:
            config = load(f.read(), Loader=Loader)

        # validate
        required_params = ["tg_api", "tg_token", "tg_chat_id"]
        for param in required_params:
            if param not in config.keys() or config[param] is None:
                logging.error(f"missing mandatory '{param}' in the config file")
                sys.exit()
        ctx.default_map = config
    return value
