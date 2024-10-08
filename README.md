# MC3DS-SplashReplacer
- Creates Game Patches to Replace Splashes in Minecraft New Nintendo 3DS Edition inside of the `code.bin`.

## Requirement(s):
- Python 3.9+
- The `code.bin` file itself.
- Add the `C-Drive` to PATH for Python to See Modules/Files needed.
- Windows Vista/7/8/10/11 (Does not work in VM's or on ARM Hardware Emulating Windows).

## Download:
- Click [Here](https://github.com/Cracko298/MC3DS-SplashReplacer/releases/download/v1.1/SplashReplacer.zip) to Download.

## Usage:
- Place `code.bin` rom Code File inside of `.\SplashReplacer\codebin\` sub-directory.
- Start Powershell in the `.\SplashReplacer\` directory.
- Run the Following Command: `python "main.py" --csplash-to-splash`.
- Modify the Splash file that was generated here: `.\SplashReplacer\splashes.json`.
- Then run the Following Command: `python "main.py" --splash-to-code`.
- This will create a new Modified `code.bin` file and Create a Patch (`code.ips`) for the splashes in Code File (this may take a  while depending on how much you modified).
### Help Message:
```
    python "main.py" [flag]
        Flags:
            -c2s | --csplash-to-splash
            -s2c | --splash-to-code

    Example Usage:
        python "main.py" -c2s
        python "main.py" --csplash-to-splash
```

### Notice(s):
- If you get an error that says something like: "Python was not found", you may need to add it to PATH, or use `py` instead of `python` in your Commands.
- If you get any errors saying the text was not found, this means that the Original Text is not Stored inside of the `code.bin` Code File.
- `.\SplashReplacer` is the Directory you extracted the `*.zip` File too, plus the Application Directory. Example: `C:\Users\batch_t2amk73\Downloads\SplashReplacer\`.
- After Completing/making your `code.ips` Game-Patch, you will need to put it into the Following Directory on 3DS: `sdmc:\luma\titles\[mc3dsTitleID]\`.
