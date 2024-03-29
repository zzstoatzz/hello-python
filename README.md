# hello, python!
this repo is meant as a kickstart to learning python (for someone who happens to be on windows :/ {not me})

## development environment

### clone this repo and cd into it
```bash
git clone https://github.com/zzstoatzz/hello-python.git # download this repo
cd hello-python # change directory into the repo
```

### install python (3.10+)
here's a tutorial on installing python on windows: https://www.digitalocean.com/community/tutorials/install-python-windows-10

### pick an editor
editors are controversial in software but in my opinion, the easiest to get started with is [VSCode](https://code.visualstudio.com/). it's free, open source, and has a ton of extensions that make it easy to get started with python.

**tip**
> add `code` to your path so you can open files from the command line. in VSCode, open the command palette (ctrl + shift + p) and type `shell command` to find the option to install the `code` command in path. Then from anywhere in your terminal, you can type `code <filename>` to open it in VSCode. Open the current directory with `code .`

### virtual environments
most things you want to do in python, someone has already written a package for. you can install these packages with `pip` like `pip install some-package-name`. but its a good idea to only have packages around that you need for the thing you're currently working on - this is where virtual environments come in.

so if you're starting something new:
- create a directory for your project
```bash
mkdir my-project # make a new directory
cd my-project
```
- create a virtual environment named my-project
```bash
python -m venv my-project
```
you can also use micromamba like me, but you'd have to install it first, see [here](
https://mamba.readthedocs.io/en/latest/micromamba-installation.html#linux-and-macos)

- activate the virtual environment
```bash
source my-project/bin/activate
```

- edit your `pyproject.toml` file to include the packages you need
```toml
[project]
dependencies = [
    "httpx",
    "pydantic",
    "ruff",
]
```
the above is the current `pyproject.toml` file for this repo. it includes the packages `httpx`, `pydantic`, and `ruff` used in this repo. You shouldn't need to edit this file unless you'd like to play around with the packages used in this repo.
- install the packages
```bash
pip install .
```
- to deactivate the virtual environment, run
```bash
deactivate
```

## now let's learn some python!