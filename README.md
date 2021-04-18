# Anki Reference Version

[Anki](https://apps.ankiweb.net/) is a free and open-source flashcard program that uses [spaced repetition](https://en.wikipedia.org/wiki/Spaced_repetition). This repository contains a reference version of Anki based on [**Anki v2.1.16**](https://github.com/ankitects/anki/tree/2.1.16). The purpose of this reference version is to be able to install and run the same version of Anki in different environments with a stable set of settings and features. It was primarily created for [`ArnaudLasnier/computer_science_flashcards`](https://github.com/ArnaudLasnier/computer_science_flashcards).

## Installation

For macOS, with [Homebrew](https://brew.sh):

```sh
brew install python mpv mplayer lame portaudio sqlite git
git clone https://github.com/ArnaudLasnier/ankiref
cd ankiref
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
deactivate
```

Note that this version of Anki requires **Python 3.6** or newer. If you cannot download a compatible version of Python with Homebrew, you can build Python 3.6 directly [from source](https://www.python.org/downloads/release/python-3613/).

## Running Anki

Once everything is properly installed, you can run Anki with:

```sh
source .venv/bin/activate
./runanki --base <base> --profile <profile> --lang <lang>
deactivate
```

The `base` argument corresponds to the [base folder](https://docs.ankiweb.net/#/files?id=file-locations) used by Anki. The `profile` argument corresponds to the [profile](https://docs.ankiweb.net/#/profiles) used (i.e. the user) and defaults to "User 1". The `lang` argument corresponds to the language used in the user interface and defaults to "en_US".

## Notes

This reference version is based on [Anki v2.1.16](https://github.com/ankitects/anki/tree/2.1.16) (released on December 12, 2019) because it was the first release to [remove](https://changes.ankiweb.net/#/?id=changes-in-2116) the "experimental" label from the new scheduler<sup>1</sup> and also the last to be solely written in Python<sup>2</sup>. Also, the differences between this reference version and the original Anki v2.1.16 are well explained in the [commit log](https://github.com/ArnaudLasnier/ankiref/commits/reference) of this branch.

---

<small>
    <p><sup>1</sup> Anki 2.1 introduced a <a href="https://changes.ankiweb.net/#/?id=experimental-scheduler">new optional scheduler</a>. It was considered experimental until Anki v2.1.16.</p>
    <p><sup>2</sup> Some parts of Anki were indeed rewritten in Rust in <a href="https://github.com/ankitects/anki/tree/2.1.17">Anki v2.1.17</a> (released on January 11, 2020).</p>
</small>
