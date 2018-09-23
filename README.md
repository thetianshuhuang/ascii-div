# Sublime Text ASCII Divider Plugin

Adds easy insertion for dividers:

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

Dividers automatically center and conform to an 79-column width. Comments are determined by language detection.

## Commands

The command can be called with
```python
window.run_command("insertasciiart", {"type": "large"})
```
replacing ```"large"``` with ```"small"```, as desired. By default, ```Command Palette -> ASCII Art: Add large/small divider``` (```CTRL```+```shift```+```p``` or ```M-x``` with emacs bindings) calls the insertion command.
