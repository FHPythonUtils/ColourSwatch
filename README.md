[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/ColourSwatch.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/[codacy-proj-id].svg?style=for-the-badge)](https://www.codacy.com/gh/FHPythonUtils/ColourSwatch)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/ColourSwatch.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/ColourSwatch.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/ColourSwatch.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/ColourSwatch.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/ColourSwatch.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/colourswatch.svg?style=for-the-badge)](https://pypi.org/project/colourswatch/)
[![PyPI Version](https://img.shields.io/pypi/v/colourswatch.svg?style=for-the-badge)](https://pypi.org/project/colourswatch/)

<!-- omit in TOC -->
# ColourSwatch

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Use this module to read, and write to a number of colour palette file formats

- [Compatibility](#compatibility)
	- [*](#ul-lili-ul)
	- [&](#)
	- [$](#-1)
- [Docs](#docs)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Download](#download)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
- [How to run](#how-to-run)
	- [With VSCode](#with-vscode)
	- [From the Terminal](#from-the-terminal)
- [How to update, build and publish](#how-to-update-build-and-publish)
- [Download](#download-1)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)

## Compatibility

Bear in mind that the tables below may not be completely accurate. If that is
the case, please open an issue and I will fix the tables.

|Application|Extension|Read|Write|
|---|---|---|---|
|Gimp|.gpl|:heavy_check_mark:|:heavy_check_mark:|
|KOffice|.colors|:heavy_check_mark:|:heavy_check_mark:|
|Skencil|.spl|:heavy_check_mark:|:heavy_check_mark:|
|sK1|.skp|:heavy_check_mark:|:heavy_check_mark:|
|LibreOffice|.soc|:heavy_check_mark:|:heavy_check_mark:|
|Paint.net|.txt|:heavy_check_mark:|:heavy_check_mark:|
|Adobe Color Book Legacy|.acbl|:heavy_check_mark:|:x:|
|Scribus|.xml|:heavy_check_mark:|:heavy_check_mark:|
|PaintShopPro|.pal|:heavy_check_mark:|:heavy_check_mark:|
|CorelDraw|.pal|:heavy_check_mark:|:heavy_check_mark:|
|ColdFusion|.hpl|:heavy_check_mark:|:heavy_check_mark:|
|*|.yaml|:heavy_check_mark:|:heavy_check_mark:|
|*|.toml|:heavy_check_mark:|:heavy_check_mark:|
|*|.json|:heavy_check_mark:|:heavy_check_mark:|
|&|.png|:heavy_check_mark:|:heavy_check_mark:|
|&|.svg|:heavy_check_mark:|:heavy_check_mark:|
|$|.jpg|:heavy_check_mark:|:heavy_check_mark:|
|$|.webp|:heavy_check_mark:|:heavy_check_mark:|
|Adobe Swatch Exchange|.ase|:heavy_check_mark:|:x:|

### *
Files require a name (`name` or `scheme`) and an author is optional (`author`)

### &
Support for any PNG and any SVG when reading

### $
Colours should be 16x16 px on a canvas with size 256x(16*ceil(colours/16)
e.g.

<img src="test/colours.jpg" width="256">

## Docs
See the [Docs](/DOCS.md) for more information.

## Install With PIP

```python
pip install colourswatch
```

Head to https://pypi.org/project/colourswatch/ for more info


## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.8.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.8
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.8 interpreter is selected (Ctrl+Shift+P > Python:Select
Interpreter > Python 3.8)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```

## How to update, build and publish

1. Ensure you have installed the following dependencies
	Linux
	```bash
	wget dephell.org/install | python3.8
	wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.8
	```
	Windows
	```powershell
	(wget dephell.org/install -UseBasicParsing).Content | python
	(wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
	```
2. Use poetry for the heavy lifting and dephell to generate requirements
	```bash
	poetry update
	dephell deps convert
	```
3. Build/ Publish
	```bash
	poetry build
	poetry publish
	```
	or
	```bash
	poetry publish --build
	```


## Download
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/FHPythonUtils/ColourSwatch
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files
### Licence
MIT License
Copyright (c) FredHappyface
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct
In the interest of fostering an open and welcoming environment, we
as contributors and maintainers pledge to make participation in our
project and our community a harassment-free experience for everyone.
Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md) for more information.

### Contributing
Contributions are welcome, please see the [Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md) for more information.

### Security
Thank you for improving the security of the project, please see the [Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md) for more information.
