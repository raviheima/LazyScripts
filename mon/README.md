# mon (python auto run)

This is a Bash script I created to automate running Python scripts. As a beginner, I wanted to make things easier instead of hitting the run button after every little change to get a preview. So, I automated it instead!

The script is currently tweaked to run only Python scripts, but in the future, I might tweak it to support other languages if necessary. You can also modify it as you like to suit your needs.

## Features

- **Automatic Execution:** Watches a Python script for changes and runs it whenever it's modified.
- **Customizable:** Feel free to tweak the script to support other programming languages or adjust it to your needs.

## Installation

You can install this script on your Linux PC in two ways:

### Option 1: Copy it to `/bin`

To make it accessible from anywhere, copy the script to the `/bin` directory:

```bash
sudo cp mon /bin/mon
```

This allows you to run the script like this:

```bash
mon hello.py
```

### Option 2: Create an Alias

Alternatively, you can create an alias by editing your `~/.bashrc` or `~/.zshrc` file (depending on your shell). Add this line:

```bash
alias mon='/path/to/mon'
```

Then, run `source ~/.bashrc` (or `source ~/.zshrc`) to refresh your shell configuration.

## Usage

Once installed, run the script by passing the Python script you want to monitor as an argument:

```bash
mon hello.py
```

The script will automatically monitor the specified Python script for changes and run it whenever modified.

Enjoy! :)