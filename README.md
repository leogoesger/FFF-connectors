# FFF Connectors

[![Build Status](https://travis-ci.org/leogoesger/FFF-connectors.svg?branch=master)](https://travis-ci.org/leogoesger/FFF-connectors)

## About

This project uses [Python3](https://www.python.org/), [NPM](https://www.npmjs.com/get-npm)(optional) and [Docker](https://docs.docker.com/install/)

## Setup

Docker is the preferred way of setting up the project. It will resolve most cross OS compatibility issues.

### I. Using Docker (Recommended Way)

Docker provides an easy installation process to get the project running in your local machine with near zero-configuration.

1.  Install [Docker](https://docs.docker.com/install/)

2.  Clone your project in [Terminal](http://www.informit.com/blogs/blog.aspx?uk=The-10-Most-Important-Linux-Commands) or download the entire repo from [Github](https://github.com/leogoesger/FFF-connectors)

    ```
    git clone https://github.com/leogoesger/FFF-connectors
    cd FFF-connectors/
    ```

3.  `cd` into the path of `FFF-connections` directory, then run `shell` script

    ```
    cd path/to/FFF-connectors
    ./build.sh
    ```

### II. Using [Anaconda Spyder](https://anaconda.org/anaconda/spyder) (Mac OS and Windows)

1.  Clone your project in [Terminal](http://www.informit.com/blogs/blog.aspx?uk=The-10-Most-Important-Linux-Commands) or download the entire repo from [Github](https://github.com/leogoesger/FFF-connectors)

    ```
    git clone https://github.com/leogoesger/FFF-connectors
    cd FFF-connectors/
    ```

2.  Open the folder from [Spyder](https://anaconda.org/anaconda/spyder)

3.  You may need to install these packages if you do not already have them locally

    ```
    six==1.11.0
    inquirer==2.2.0
    rasterio==0.36.0
    ```

4.  Click on `main.py` and `run`

### III. With Mac OS

1.  Install [Python3](https://www.python.org/downloads/), [Git](https://git-scm.com/download/) and a [text editor](https://www.sublimetext.com/3) of your choice.
2.  Clone your project in [Terminal](http://www.informit.com/blogs/blog.aspx?uk=The-10-Most-Important-Linux-Commands)

    ```
    git clone https://github.com/leogoesger/FFF-connectors
    cd FFF-connectors/
    ```

3.  Create and activate virtualenv

    ```
    npm setup
    source my-virtualenv/bin/activate
    ```

4.  Install dependencies

    ```
    npm install
    ```

    If you chose not to install npm, use `pip` as following:

    ```
    pip install -r requirement.txt
    ```

### IV. With Windows

1.  Install [Python3](https://www.python.org/downloads/), [Git](https://git-scm.com/download/win) and a [text editor](https://www.sublimetext.com/3) of your choice.
2.  Add Python to [System Path](https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/)

    -   Locate `Python3` from your local computer. Usually located in the following folder:

        ```
        C:\python3
        ```

        or

        ```
        C:\Users\your-namprojectData\Local\Programs\Python\Python36-32
        ```

    -   Follow this [link](https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/) from step 2 to the end.
    -   Go into Command Prompt by typing `cmd` in search bar, and type `python`. You should see the following:

        ```
        Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28)
        [GCC 4.2.1projectle Inc. build 5666) (dot 3)] on darwin
        Type "help", "copyright", "credits" or "license" for more information.
        >>>
        ```

    -   Type `exit()` to exit the python shell.

3.  Clone your project in [Command Prompt](http://www.informit.com/blogs/blog.aspx?uk=The-10-Most-Important-Linux-Commands)

    ```
    git clone https://github.com/leogoesger/FFF-connectors
    cd FFF-connectors
    ```

4.  Create and activate virtualenv

    ```
    python -m venv my-virtualenv
    my-virtualenv\Scripts\activate
    ```

5.  Install dependencies

    ```
    pip install -r requirements.txt
    ```

## Run Script

1.  With [Docker](https://docs.docker.com/install/)

    ```
    ./run.sh
    ```

2.  With Spyder, click on main.py and `run`

3.  All others, navigate to project directory, use `npm` with

    ```
    npm start
    ```

    or using `python` direcly as following:

    ```
    python main.py
    ```

## Test

First enter `virtualenv` with previously discussed steps in project directory.

```
npm test
```

or using `python` directly as following:

```
python -m unittest discover -v
```

## Error and Bug

Use [JIRA](http://watermgmt.ucdavis.edu/) to keep upload error message, a screen shot, and raw data file used

## Options

[iTerm](https://www.iterm2.com/): iTerm2 is a replacement for Terminal in MacOS

## License

Copyright (c) 2018

Licensed under the [MIT license](https://opensource.org/licenses/MIT).
