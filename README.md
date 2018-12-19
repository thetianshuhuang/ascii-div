# Sublime Text ASCII Divider Plugin

Adds easy insertion for dividers and large ASCII text:

```c
// ----------------------------------------------------------------------------
//
//                              Divider Caption
//
// ----------------------------------------------------------------------------
```

```python
# -- Divider Caption ----------------------------------------------------------
```

```python
#  ___  _     _    _            ___           _   _
# |   \(_)_ _(_)__| |___ _ _   / __|__ _ _ __| |_(_)___ _ _
# | |) | \ V / / _` / -_) '_| | (__/ _` | '_ \  _| / _ \ ' \
# |___/|_|\_/|_\__,_\___|_|    \___\__,_| .__/\__|_\___/_||_|
#                                       |_|
```

Dividers automatically center and conform to an 79-column width. Comments are determined by language detection. All pyfiglet fonts are supported.


## Install
Copy the entire ```asci-div``` directory to Sublime's packages folder.

Windows:
```shell
C:\Users\<your username>\AppData\Roaming\Sublime Text 3\Packages
```
or
```shell
%appdata%\Sublime Text 3\Packages
```

Linux:
```shell
~/.config/sublime-text-3/Packages
```

## Commands

The command can be called with
```python
window.run_command("insertasciiart", {"divtype": "large"})
```
replacing ```"large"``` with ```"small"```, as desired. By default, ```Command Palette -> ASCII Art: Add large/small divider``` (```CTRL```+```shift```+```p``` or ```M-x``` with emacs bindings) calls the insertion command.

In order to run a figlet command, add ```figlet_``` before the font name. For example, a command for inserting the ```slant``` fount would have type ```divtype = figlet_slant```.
