# An intro to hikari

This repo is designed to provide some simple examples to get you started with hikari. Contained in this repo are bots designed with both the [hikari-lightbulb](https://github.com/tandemdude/hikari-lightbulb) and [hikari-tanjun](https://github.com/FasterSpeeding/Tanjun) command handlers. This repo is designed with extra stability in mind, but if you want newer features, [check out this experimental repo](https://github.com/Carberra/hikari-testing).

## Installing requirements

When installing the requirements, make sure you install the correct reqirements for your operating system.

Windows:
```sh
pip install -r requirements-nt.txt
```

Anything else:
```sh
pip install -r requirements-unix.txt
```

## Running the bots

To run the hikari-lightbulb bot:
```sh
python -m lightbulb-bot
```

To run the hikari-tanjun bot:
```sh
python -m tanjun-bot
```

**Please note**: There is no suitable stable version of hikari-tanjun, so this repo uses the unreleased version 2.0.0a1. If you want utmost stability, use hikari-lightbulb.

## License

This repo is provided under the [BSD 3-Clause License](https://github.com/parafoxia/hikari-intro). This means you can take anything you want from this repo to use in your own bots, though redistributions must retain the license.
