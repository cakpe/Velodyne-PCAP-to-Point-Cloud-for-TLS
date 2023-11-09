# At the creation of this README, open3d for python did not work on python 3.11 (whih is what i had on my system)

To work around this without completely disrupting your system, install multiple versions of python and then alias whichever version you
installed in your shell configuration file (.zshrc in my case). So in my case, I installed python3.10 using homebrew and then aliased it to
python310 in my .zshrc file.

I then create a python virtual environment tied to that new version of python (python3.10 in my case) and work within said environment.