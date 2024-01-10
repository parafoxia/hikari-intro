# An intro to hikari

This repo provides some simple examples to get you started with [hikari](https://github.com/hikari-py/hikari). Contained in this repo are bots designed with the [hikari-arc](https://github.com/hypergonial/hikari-arc), [hikari-crescent](https://github.com/hikari-crescent/hikari-crescent/), [hikari-lightbulb](https://github.com/tandemdude/hikari-lightbulb) and [hikari-tanjun](https://github.com/FasterSpeeding/Tanjun) command handlers.

This repo only provides examples for slash commands at the moment.

## Installing requirements

You can install the necessary requirements by doing:

```sh
pip install -r requirements.txt
```

## Setup

There is a little bit of setup you need to do before testing the bots, specifically:

You **must** create a file called `token` in a directory called `secrets` in the root directory of this project, and paste your bot's token in there.

> [!TIP]
> Be sure to leave **not** add a file extension to the end of this file (e.g. `.txt`), otherwise it will not work.

## Testing the bots

> [!NOTE]
> The command handlers are sorted alphabetically with no particular preference for one or the other. It is recommended that you give all of them a try before coming to conclusions.

## hikari-arc

This library was designed from the ground up with modern Python features in mind. It has intuitive functional syntax for creating commands, and an easy to understand [documentation](https://arc.hypergonial.com/). `arc` only supports application commands.

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
