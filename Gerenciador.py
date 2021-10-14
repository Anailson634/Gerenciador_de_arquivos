import os
import shutil
import re

class Gerenciador_Arquivos:
    def __init__(self, dir):
        self.dir=dir
        self.extensoes=[]
        self.files=os.listdir(self.dir)
        
    def criar_pastas(self):
        self.extensoes=[]
        for v in self.files:
            self.extensoes.append(str(re.findall(r'\..+', v)).replace("[", "").replace("]", "").replace("'", "").replace(' ', '').replace('.', ''))  # Organiza as extensões
        for v in self.extensoes:
            try:
                os.mkdir(f'{self.dir}\{v.replace(".", "")}')
            except:
                continue
    
    def organizar(self):
        import time as tm
        for i, v in enumerate(self.extensoes):
            if v in self.files[i]:
                try:
                    shutil.move(r'{}\{}'.format(self.dir, self.files[i]), r'{}\{}'.format(self.dir, v))
                except:
                    continue
