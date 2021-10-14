from Gerenciador import *

path=str(input(r'Diretorio: '))
gerenciador=Gerenciador_Arquivos(path)

gerenciador.criar_pastas()
gerenciador.organizar()
