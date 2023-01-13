import os

import pexpect
import tomlkit


def create_config(config_path: str) -> dict:
    """
    Function to create the config file

    Parameters
    ----------
    config_path : str
        Path to the config file.

    Returns
    -------
    config : dict
        Dictionary containing the configuration.
    """
    path, _ = os.path.split(config_path)
    os.makedirs(path, exist_ok=True)

    data = {}
    data["path"] = input("What is the path to the environments?\n")
    data["shell"] = input("What is your favorite shell?\n")
    outstring = tomlkit.dumps(data)

    with open(config_path, "w") as f:
        f.write(outstring)

    return data


def read_config(config_path: str) -> dict:
    """
    Function to read the configuration.

    Parameters
    ----------
    config_path : str
        Path to the config file.

    Returns
    -------
    config : dict
        Dictionary containing the configuration.
    """
    with open(config_path, "r") as f:
        file_content = f.read()
    data = tomlkit.parse(file_content)
    return data


def get_venv(config: dict) -> str:
    """
    Function to get the users choice of environment.

    Parameters
    ----------
    config : dict
        Dictionary containing the configuration.

    Returns
    -------
    env_path : str
        Path to the virtual environment.
    """
    dir_content = os.listdir(config["path"])

    # filtering contents of directory to only include subdirectories that have a bin subdirectory
    dirs = []
    for content in dir_content:
        print(content)
        print(config["path"])
        full_path = os.path.join(config["path"], content)
        if os.path.isdir(full_path) and "bin" in os.listdir(full_path):
            dirs.append(content)

    # listing possible environments
    os.system("clear")
    for i, directory in enumerate(dirs):
        print(f"[{i}] {directory}")

    # adding the quit option
    print("\n[q] quit application\n")

    choice = input("Which environment do you want to activate?\n")

    if choice == "q":
        exit()

    # verifying choice
    try:
        choice_int = int(choice)
        if choice_int > len(dirs):
            os.system("clear")
            print(f"Error: choice has to be between 0 and {len(dirs)-1}.")
            get_venv(config)
    except ValueError:
        os.system("clear")
        print(f"Error: input has to be an integer.")
        get_venv(config)

    return os.path.join(config["path"], dirs[choice_int])


def activate_venv(env_path: str, config: dict):
    """
    Function to activate virtual environment.

    Parameters
    ----------
    env_path : str
        Path to the virtual environment.
    config : dict
        Dictionary containing the configuration.
    """
    if "args" in config:
        args = config["args"]
        args.append("-i")
    else:
        args = ["-i"]

    c = pexpect.spawn(
        config["shell"],
        args,
    )
    c.sendline(f"source {env_path}/bin/activate")
    c.interact(escape_character=None)
    c.close()


def select_pyenv():
    """
    Main function
    """
    config_path = os.path.expanduser("~/.config/select_pyenv/config.toml")

    if os.path.exists(config_path):
        config = read_config(config_path)
    else:
        config = create_config(config_path)

    venv = get_venv(config)
    activate_venv(venv, config)


if __name__ == "__main__":
    select_pyenv()
