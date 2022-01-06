# To do list with Flask framework

## Description

This repository contains a to-do list project for a website. It was made in Python using the Flask framework and uses the sqlite database.

## Creating a virtual environment

Open a terminal in your project directory and type the following command:

```bash
python -m venv venv
```
This will create a virtual environment named **venv**. To activate the virtual environment type the following command in your terminal:

```bash
"venv/scripts/activate.bat"
```

Next you have to install all required packages.

## Packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all required packages, which are listed in the **requirements.txt** file. You can use the command below.

```bash
pip install -r requirements.txt
```

## Launch

To run the application, use the **run.py** file found in the repository. You can use a terminal by typing the following command or run it from the IDE.

```bash
python run.py
```

This will start the local server. Then, in a web browser, enter the address given in the terminal, adding the endpoint **/tasks**. Example:

```
127.0.0.1:5000/tasks
```

At this URL you will find the homepage of this application.
