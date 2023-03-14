# autogit
Automatically pushes code into remote repo quickly, in case of emergency or lazy.

If you want to edit the code and build into a exe (once built finish, exe can be found in dist folder):
```
pip install pyinstaller
python -m PyInstaller --onefile --windowed --icon=image.ico autogit.py
```

Place the exe file in a folder that is in PATH, (or add the location of the autogit.exe file to PATH).

Example usage:
```
autogit
autogit "updated readme"
```
