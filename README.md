# An intro to hikari

This repo is designed to provide some simple examples to get you started with hikari. Contained in this repo are bots designed with both the [hikari-lightbulb](https://github.com/tandemdude/hikari-lightbulb) and [hikari-tanjun](https://github.com/FasterSpeeding/Tanjun) command handlers. This repo is designed with extra stability in mind, but if you want newer features, [check out this experimental repo](https://github.com/Carberra/hikari-testing).

## Installing requirements

When installing the requirements, make sure you install the correct requirements for your operating system.

Windows:
```sh
pip install -r requirements-nt.txt
```

Anything else:
```sh
pip install -r requirements-unix.txt
```

## Running the bots

### hikari-lightbulb

This library sports a very discord.py-like syntax, making for an easier time migrating for those wishing to switch. It is less powerful than hikari-tanjun, but is the more stable of the two options at present.

To run the hikari-lightbulb bot:
```sh
python -OO -m lightbulb_bot
```

### hikari-tanjun

This library has a syntax far more similar to [click](https://github.com/pallets/click/), a CLI app builder that relies almost entirely on the usage of decorators. It is more powerful than hikari-lightbulb with better support for slash commands and interactions, but does not currently have a stable version. The version this repo currently uses is the unreleased v2.0.0a1 version.

To run the hikari-tanjun bot:
```sh
python -OO -m tanjun_bot
```

## License

This repo is provided under the [BSD 3-Clause License](https://github.com/parafoxia/hikari-intro/blob/main/LICENSE). This means you can take anything you want from this repo to use in your own bots, though redistributions must retain the license.
