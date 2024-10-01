import os, sys, time, json
from data.modules import bjson, conversions, JOAAThash, updateDatabase
modifiedCodePath = f'{os.path.dirname(__file__)}\\codebin\\modified_code.bin'
codePath = f'{os.path.dirname(__file__)}\\codebin\\code.bin'

def helpFunction():
    print(f"""
    python "{os.path.basename(__file__)}" [flag]
        Flags:
            -c2s | --csplash-to-splash
            -s2c | --splash-to-code

    Example Usage:
        python "{os.path.basename(__file__)}" -c2s
    """)
    input("Press The 'Enter' to Exit Application.")
    sys.exit(1)

try:
    flag = sys.argv[1]
    if flag == '--help' or flag == '-h':
        helpFunction()

except IndexError:
    helpFunction()

if os.path.exists(codePath):
    if os.path.exists(modifiedCodePath):
        os.remove(modifiedCodePath)
else:
    print(f"\nNo code.bin File Provided.\nPlease place your 'code.bin' file into '{os.path.dirname(__file__)}\\codebin'\n")
    input("Press The 'Enter' to Exit Application.")
    sys.exit(1)

def copyCodeToModifiedFile():
    with open(codePath, 'rb') as codeFile:
        actualCodeOfCodeFile = codeFile.read()
        with open(modifiedCodePath, 'wb') as modifiedCodeFile:
            modifiedCodeFile.write(actualCodeOfCodeFile)
            modifiedCodeFile.close()
        codeFile.close()

def csplashtosplash():
    jsonString = bjson.convertBjsonToJson(f".\\data\\splashes.bjson")
    with open(".\\data\\splashes.json", 'w') as jsonFile0:
        jsonFile0.write(jsonString)
        with open('.\\splashes.json', 'w') as jsonFile1:
            jsonFile1.write(jsonString)
            jsonFile1.close()
        jsonFile0.close()

    print(f"\nConversion From Compiled '{os.path.dirname(__file__)}\\data\\splashes.bjson'\nTo a Decompiled '{os.path.dirname(__file__)}\\splashes.json' File.\n")
    time.sleep(5)
    sys.exit(1)

def splashIntoCode():
    json_file = ".\\data\\splashes.json"
    bin_file = modifiedCodePath
    replacement_json_file = '.\\splashes.json'
    with open(json_file, 'r') as jf:
        original_data = json.load(jf)
        splash_strings = original_data['splashes']

    with open(replacement_json_file, 'r') as rjf:
        replacement_data = json.load(rjf)
        replacement_strings = replacement_data['splashes']

    with open(bin_file, 'rb+') as bf:
        content = bf.read()

        for original_string, replacement_string in zip(splash_strings, replacement_strings):
            original_string_bytes = original_string.encode('utf-8')
            original_length = len(original_string_bytes)
            position = content.find(original_string_bytes)
            
            if position != -1:
                if len(replacement_string) > original_length:
                    print(f"Error: The replacement string '{replacement_string}' exceeds {original_length} characters. Skipping.")
                    continue
                elif len(replacement_string) < original_length:
                    replacement_string = replacement_string.ljust(original_length)
                
                replacement_string_bytes = replacement_string.encode('utf-8')
                bf.seek(position)
                bf.write(replacement_string_bytes)
            else:
                print(f"Error: String '{original_string}' not found in The code.bin File.")
    
    print("\nGenerating Game Patch... (This Can Take A While)")
    with open(codePath, 'rb') as f1:
        data1 = f1.read()
        with open(modifiedCodePath, 'rb') as f2:
            data2 = f2.read()
            f2.close()
        f1.close()
    
    if data1 != data2:
        os.system(f"{os.path.dirname(__file__)}\\data\\gc.exe create {codePath} {modifiedCodePath} {os.path.dirname(__file__)}\\code.ips > nul 2>&1")
        print(f"Successfully Generated '{os.path.dirname(__file__)}\\code.ips' Game Patch.\n")
    else:
        print("Error: File was not Changed, cannot create Game Patch.\n")
    
    sys.exit(1)

if os.path.basename(__file__) == 'main.py':
    copyCodeToModifiedFile()
    if flag == '--csplash-to-splash' or flag == '-c2s':
        csplashtosplash()
    if flag == '--splash-to-code' or flag == '-s2c':
        splashIntoCode()
    else:
        helpFunction()
