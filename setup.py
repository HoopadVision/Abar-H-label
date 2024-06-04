from cx_Freeze import setup, Executable
setup(
    name="your_script",
    version="0.1",
    description="Description of your script",
    executables=[Executable("your_script.py")]
)