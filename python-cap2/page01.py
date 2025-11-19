"""Creating Venv"""


def create():
    print("to create a venv, you just need to type: python -m venv (name of venv)")


def activate(*args):
    print(
        "to activate a virtual enviroment, you just need to type: (name\Script\activate"
    )


def deactivate(*args):
    print("for deactivate a venv, just type:  desactivate")


def addPackage(*arg):
    print(
        "for add a new package outside python Type: pip install (visit Pypi.org to see)"
    )


def removePackage(*args):
    print("To unistall a package, you need to type: pip uninstall (name of package)")


def FreezeFunctions(*arg):
    print(
        "To see the version of packages in which you have installed, type: pip freeze"
    )

    print(
        "To Create one txt with the version of your venv package, type: \
        pip freeze > name(normally requirements).txt, you can use this archive to \
        install in another venv, just typing: pip install -r .\requirements.txt"
    )
