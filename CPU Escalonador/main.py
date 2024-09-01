from enum import Enum

class Status(Enum):
    OCUPADO = 1
    OCIOSO = 2
    
class VM():
    def __init__(self, id, vCPU, et, at, priority):
        self.id = id
        self.vCPU = vCPU
        self.et = et # estimetated time
        self.at = at # arrival time
        self.priority = priority
        
## CPU deve ter no max 4 
class CPU():
    def __init__(self, id, Status): #status = tirar
        self.id = id
        self.lista_tarefa = [0, 0, 0, 0]
        self.Status = Status
        self.lista_cheia = False
        self.startPos = 0
        self.vm_list = []

    def receberLista(self, vm_list):
        self.vm_list = vm_list

    # sobre lista https://stackoverflow.com/questions/522372/finding-first-and-last-index-of-some-value-in-a-list-in-python
    def alocarTarefa(self, vm):
        # print("a")
        if not self.lista_cheia:
            # print("b")

            # Número de espaços livres
            spaces = self.lista_tarefa.count(0)

            if vm.vCPU <= spaces:  
                # print("c")
                first_pos = self.lista_tarefa.index(0)
                last_pos = first_pos + vm.vCPU

                # Último 0 encontrado
                # last_pos = len(self.lista_tarefa) - self.lista_tarefa[::-1].index(0) # - 1

                for i in range(first_pos, last_pos):
                    # print(i)
                    self.lista_tarefa[i] = vm.id
                    
            cpu.info()
        else:
            print("Lista cheia")


        # count() pode ser demorado, testar futuramente a differença com 'from collections import Counter'            
        if self.lista_tarefa.count(0) == 0:
            self.lista_cheia = True
    
    def info(self):
        print(self.lista_tarefa)
        
         #print("tempo: " + tempo_ini)
    
tempo_ini = 0 # primeira tarefa em 20 min
tempo_max = 0 # tempo max first fit = 170 minutos aumentar de 5min em 5 min por ciclo
vm_list = []

# def main():
cpu = CPU(1, Status.OCIOSO.value)

#Lista de VM's n
vm1 = VM(1, 2, 35, 40, 3)
vm2 = VM(2, 2, 40, 45, 1)
vm3 = VM(3, 4, 30, 45, 1)
vm4 = VM(4, 4, 25, 20, 3)
vm5 = VM(5, 2, 40, 25, 3)
vm6 = VM(6, 4, 20, 20, 2)
vm7 = VM(7, 1, 20, 40, 0)
vm8 = VM(8, 4, 20, 30, 1)
vm9 = VM(9, 4 , 10, 20, 2)
vm10 = VM(10, 1, 35, 30, 30)

# vm_list.append(vm1).append(vm2).append(vm3).append(vm4).append(vm5).append(vm6).append(vm7).append(vm8).append(vm9).append(vm10)
vm_list.extend([vm1, vm2, vm3, vm4, vm5, vm6, vm7, vm8, vm9, vm10])
cpu.receberLista(vm_list)
    
cpu.info()
cpu.alocarTarefa(vm1)
cpu.alocarTarefa(vm2)
cpu.alocarTarefa(vm3)
# cpu.info()
    
# while len(cpu.vm_list) > 0:
while tempo_ini < 200:
    for vm in vm_list:
        if vm.at == tempo_ini:
            print("Entrou vm " + str(vm.id) + " no tempo " + str(tempo_ini))
        if vm.at < tempo_ini and (vm.et + vm.at) == tempo_ini:
            print("Saiu vm " + str(vm.id) + " no tempo " + str(tempo_ini))

        # cpu.alocarTarefa(vm)
        
    tempo_ini += 5