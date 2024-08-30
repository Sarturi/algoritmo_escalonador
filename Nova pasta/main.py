from enum import Enum

class Status(Enum):
    OCUPADO = 1
    OCIOSO = 2
    
class VM():
    def __init__(self, id, vCPU, et, at, priority):
        self.id = id
        self.vCPU = vCPU
        self.et = et
        self.at = at
        self.priority = priority
        
## CPU deve ter no max 4 
class CPU():
    def __init__(self, id, Status): #status = tirar
        self.id = id
        self.lista_tarefa = [0, 0, 0, 0]
        self.Status = Status
        self.lista_cheia = False
        self.startPos = 0
        
    def alocarTarefa(self, vm):
        print("a")
        if not self.lista_cheia:
            print("b")
            if vm.vCPU <= len(self.lista_tarefa):                
                for i in self.lista_tarefa:
                    if self.lista_tarefa[i] == 0:
                        self.startPos = i
                        
                # print(startPos)
                
                start = self.startPos
                print(start)
                        
                # restante = len(self.lista_tarefa) - vm.vCPU
                # print("c")
                # print(self.lista_tarefa)
                for start in range(vm.vCPU):
                    if self.lista_tarefa[start] == 0:
                        self.lista_tarefa[start] = vm.id
                    # print(self.lista_tarefa[i])
                
                    
        # if len(self.lista_tarefa) == 4:
        #     self.lista_cheia = True
    
    def info(self):
        print(self.lista_tarefa)
        
         #print("tempo: " + tempo_ini)
    
tempo_ini = 0 # primeira tarefa em 20 min
tempo_max = 0 # tempo max first fit = 170 minutos aumentar de 5min em 5 min por ciclo
# cpu_list = []
vm_list = []

# def main():
cpu = CPU(1, Status.OCIOSO.value)

# cpu_list.append(cpu)


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
    
    
cpu.info()
cpu.alocarTarefa(vm1)
cpu.alocarTarefa(vm2)
cpu.info()
    
# while True:
    
    # tempo_ini += 5