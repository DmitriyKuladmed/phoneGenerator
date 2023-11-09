import sys
from cx_Freeze import setup, Executable

main_script = "main.py"

additional_modules = []

include_files = ["images", "const.py", "functions.py", "user_data.txt"]

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable(
        script=main_script,
        base=base,
        icon="images/logo_1.ico",
    )
]


options = {
    "build_exe": {
        "includes": additional_modules,
        "include_files": include_files,
    }
}

setup(
    name="NumMaker",
    version="1.0",
    description="Your application description",
    executables=executables,
    options=options
)