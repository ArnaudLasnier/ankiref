# Anki Reference Version

[Anki](https://apps.ankiweb.net/) is a free and open-source flashcard program that uses [spaced repetition](https://en.wikipedia.org/wiki/Spaced_repetition). This repository contains a reference version of Anki based on [**Anki v2.1.16**](https://github.com/ankitects/anki/tree/2.1.16) (released on December 12, 2019).

[Anki v2.1.16](https://github.com/ankitects/anki/tree/2.1.16) was the first release to [remove](https://changes.ankiweb.net/changes/2.1.10-19.html#changes-in-2116) the "experimental" label from the new [v2 scheduler](https://faqs.ankiweb.net/the-anki-2.1-scheduler.html#v2-scheduler) introduced in Anki v2.1.0 and also the last to be solely written in Python (some parts of Anki were indeed rewritten in Rust in [Anki v2.1.17](https://github.com/ankitects/anki/tree/2.1.17), released on January 11, 2020).


## System Dependencies

On macOS:

```sh
brew install mpv mplayer lame portaudio sqlite git
```

On Ubuntu:

```sh
sudo apt install mpv mplayer lame portaudio19-dev sqlite3 libxcb-xinerama0 qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools qtwebengine5-dev
```

## Python Setup

This version of Anki requires a version of Python in the **v3.6.x – v3.9.x** range. The simplest way to acquire such a version of Python is to use [`uv`](https://docs.astral.sh/uv):

```sh
uv python install
```

Then you can setup a virtual environment with:

```sh
uv venv
uv pip install -r requirements.txt
```

## Running Anki

Once everything is properly installed, you can run Anki with:

```sh
uv run python runanki --base <base>
```

The `--base` argument is required and corresponds to the [base folder](https://docs.ankiweb.net/files.html#file-locations) used by Anki. There are also two other optional arguments:

- `--profile` corresponds to the [profile](https://docs.ankiweb.net/profiles.html) used (i.e. the user) and defaults to "User 1"
- `--lang` corresponds to the language used in the user interface and defaults to "en_US".

On Debian, Ubuntu and other Debian-based distributions, you will need to run Anki by disabling the Qt WebEngine sandboxing:

```sh
QTWEBENGINE_DISABLE_SANDBOX=1 uv run python runanki --base <base>
```

The reason is explained [here](https://doc.qt.io/qt-5/qtwebengine-platform-notes.html#sandboxing-support).
