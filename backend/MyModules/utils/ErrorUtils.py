from colorama import Fore


def error(message, line=None):
    if line is not None:
        print(Fore.RED + 'Error en la línea ' + str(line) + ':\n\t' + message + '.')
    else:
        print(Fore.RED + 'Error: ' + message + '.')
    exit(3)
