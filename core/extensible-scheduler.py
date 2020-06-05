import sys
import os.path
import time

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

# esse import all, é para evitar manutenção neste arquivo
from extensions import *

# esse laço monta uma lista com os itens importados da pasta extensions
importedExtension = []
for extension in sys.modules.keys():
    if "extensions." in extension:
        importedExtension.append(extension.replace("extensions.", ""))


def main():

    while True:

        # percorre a lista de extensoes importadas, e aciona os agendamentos
        # metodo eval pega uma string, e converte em objeto, assim é possivel pegar pelo nome de cada arquivo, e disparar os agendamentos, sem precisar editar este arquivo
        for ext in importedExtension:
            eval(ext).loop.run_until_complete(eval(ext).schedule.run_pending())

        time.sleep(1)


if __name__ == "__main__":
    main()
