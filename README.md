# select_pyenv

- [select\_pyenv](#select_pyenv)
  - [Introduction](#introduction)
  - [Install](#install)
  - [Usage](#usage)

## Introduction

`select_pyenv` is a command line tool to select a python virtual environment from a folder.
For me this is useful as I have environments that are used in many different folders for example a
plotting environment and I like to use a simple environment created by `python -m venv NAME` as I
prefer using `poetry` for my project management and I don't want to combine it another virtual
environment manager.

## Install

To install use the following command (it might need [`poetry`](https://python-poetry.org/docs/#installation) to be installed):

```bash
pip install pyproject.toml
```

## Usage

The usage is simple, run it by typing `select_pyenv` first time you run it a config file is created 
`$HOME/.config/select_pyenv/config.toml` in this config file there are 3 options:

| Name  | Description                                                                                                       |
| ----- | ----------------------------------------------------------------------------------------------------------------- |
| path  | Path the your virtualenvs.                                                                                        |
| shell | Your preferred shell.                                                                                             |
| args  | arguments that need to be passed when creating the shell. `-i` will always be passed to get an interactive shell. |

After this, when you run `select_pyenv` you will be shown a list of virtualenvs and be prompted to 
select one, which is then activated.