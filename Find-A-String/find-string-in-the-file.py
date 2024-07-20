import os 

text = input("Input Text: ")
path = input("Path : ")


def getfiles(path):
    f_found = False
    os.chdir(path)
    files = os.listdir()
    #print(files)
    for file_name in files:
        abs_path = os.path.abspath(file_name)
        if os.path.isdir(abs_path):
            getfiles(abs_path)
        if os.path.isfile(abs_path):
            try:
                f = open(file_name, "r", encoding='utf-8', errors='ignore')
                if text in f.read():
                    f_found = True
                    print(f"{text} found in ")
                    final_path = os.path.abspath(file_name)
                    print(final_path)
            except Exception as e:
                print(f"Error readin")
    return f_found

if not getfiles(path):
    print(f"{text} not found")
