from os.path import dirname, basename, isfile, join
import glob

# Este código carrega todos os arquivos de extensão .py dentro da pasta extensions.
# Dessa forma posso importar todos eles na classe principal (sysmo-health-monitor.py) sem precisar declarar cada uma delas

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [
    basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")
]
