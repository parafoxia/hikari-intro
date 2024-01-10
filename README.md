# An intro to hikari

This repo provides some simple examples to get you started with [hikari](https://github.com/hikari-py/hikari). Contained in this repo are bots designed with both the [hikari-lightbulb](https://github.com/tandemdude/hikari-lightbulb), [hikari-tanjun](https://github.com/FasterSpeeding/Tanjun), [hikari-crescent](https://github.com/hikari-crescent/hikari-crescent/) and [hikari-arc](https://github.com/hypergonial/hikari-arc) command handlers.

This repo only provides examples for slash commands at the moment.

## Installing requirements

You can install the necessary requirements by doing:

```sh
pip install -r requirements.txt
```

## Setup

There is a little bit of setup you need to do before testing the bots.

1. Create a file called "token" in a directory called "secrets", and put your bot's token in there.

## Testing the bots

## hikari-arc

This library was designed from the ground up with modern Python features in mind. It has intuitive functional syntax for declaring commands, and an easy to understand [documentation](https://arc.hypergonial.com/), and support for both Gateway & REST bots. `arc` only supports application commands.

To run the hikari-arc bot:
```sh
python -OO -m arc_bot
```

### hikari-crescent

This library is built to keep your project neat and tidy. Commands are created like dataclasses, so the syntax should be familiar. Crescent only supports application commands.

To run the hikari-crescent bot:
```sh
python -OO -m crescent_bot
```

### hikari-lightbulb

This library sports a very discord.py-like syntax (when making message commands), making for an easier time migrating for those wishing to switch.

To run the hikari-lightbulb bot:
```sh
python -OO -m lightbulb_bot
```

### hikari-tanjun

This library has a syntax far more similar to [click](https://github.com/pallets/click/), a CLI app builder that relies almost entirely on the usage of decorators. It is more powerful than hikari-lightbulb with better support for slash commands and interactions.

To run the hikari-tanjun bot:
```sh
python -OO -m tanjun_bot
```

## License

This repo is provided under the [BSD 3-Clause License](https://github.com/parafoxia/hikari-intro/blob/main/LICENSE). This means you can take anything you want from this repo to use in your own bots, though redistributions must retain the license.
