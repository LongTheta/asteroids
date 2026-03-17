# Asteroids Game

bootdev run 7228cde1-e519-4ee4-920e-1c50011197bb

## Using WSL

Run the project from WSL so pygame can use VcXsrv (start XLaunch on Windows first):

```bash
# From a WSL terminal in the project directory:
uv run python main.py
```

If `uv` isn't in your WSL PATH, install it in WSL or run from Windows with:  
`wsl -e bash -c "cd '/mnt/c/Users/Cathy/OneDrive/Documents/Coding Exercises/Learning_Path/boot_astroids' && uv run python main.py"`  
(ensure Windows `uv` is on your WSL PATH, e.g. add it to `~/.bashrc`).
