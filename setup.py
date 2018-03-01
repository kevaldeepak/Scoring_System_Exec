#setup.py is used to create exe file for python programs
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "re", "time", "pickle", "smtplib","email","zipfile","sys","string"],
                     "excludes": ["tkinter"],
                     "include_files": ["icon.ico"]}


base = None

setup(  name = "Scoring System",
        version = "0.9",
        description = "Tournament Scoring System By Keval Deepak",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Scoring_System_Keval Deepak.py", base=base, icon="icon.ico"),
                       Executable("Launcher.py", base=base, icon="icon.ico"),
                       Executable("Sending.py", base=base, icon="icon.ico")])

