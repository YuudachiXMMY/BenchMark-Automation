pyinstaller --distpath="./builds" --workpath="./builds" --specpath="./builds" -p C:/Users/Navi/AppData/Local/Programs/Python/Python39/Lib -p ../main/crawler.py -F -w ../main/main.py

pyInstaller --distpath="./builds" --workpath="./builds" --specpath="./builds" -w program_name.spec

pyinstaller --distpath="./builds" --workpath="./builds" --specpath="./builds" -p C:/Users/Navi/AppData/Local/Programs/Python/Python39/Lib -p ./main/crawler.py -F -w main/main.py


pyinstaller --distpath="./monitoring" --workpath="./monitoring" --specpath="./monitoring" -F tests/winMemoryDetect.py