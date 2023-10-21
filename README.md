# hello, python!

## development environment

### pick an editor
editors are controversial in software but in my opinion, the easiest to get started with is [VSCode](https://code.visualstudio.com/). it's free, open source, and has a ton of extensions that make it easy to get started with python.

**tip**
> add `code` to your path so you can open files from the command line. in VSCode, open the command palette (ctrl + shift + p) and type `shell command` to find the option to install the `code` command in path. Then from anywhere in your terminal, you can type `code <filename>` to open it in VSCode. Open the current directory with `code .`

### virtual environments
most things you want to do in python, someone has already written package for. you can install these packages with `pip` like `pip install some-package-name`. but its a good idea to only have packages around that you need for the thing you're currently working on - this is where virtual environments come in.

so if you're starting something new, here's what you do:
- create a directory for your project
```bash
mkdir my-project # make a new directory
cd my-project # move your terminal into that directory, cd = change directory
```
- create a virtual environment named my-project
```bash
python -m venv my-project
```

- activate the virtual environment
```bash
source my-project/bin/activate
```

- create a file called `requirements.txt` and add the packages you need
```bash
echo "httpx" > requirements.txt # httpx is a package for making http requests
```

- install the packages
```bash
pip install -r requirements.txt # install the packages in the requirements.txt file
```

- to deactivate the virtual environment, run
```bash
deactivate
```