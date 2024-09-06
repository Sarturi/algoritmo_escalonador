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

    def __repr__(self) -> str:
        return f'VM{self.id}'
        
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

    def verificarEspaço(self, vm):
        spaces = self.lista_tarefa.count(0)

        if vm.vCPU <= spaces:  
            return True
        else:
            return False

    # sobre lista https://stackoverflow.com/questions/522372/finding-first-and-last-index-of-some-value-in-a-list-in-python
    # count() pode ser demorado, testar futuramente a differença com 'from collections import Counter' 
    def alocarTarefa(self, vm):
        # print("a")
        if self.lista_tarefa.count(0) == 0:
            self.lista_cheia = True
        else:
            self.lista_cheia = False

        if not self.lista_cheia:
            # print("b")

            # Número de espaços livres
            spaces = self.lista_tarefa.count(0)

            if vm.vCPU <= spaces:  
                # print("c")

                # Pode dar errado nesta situação:
                # [1, 2, 2, 3] -> [0, 2, 2, 0]
                # pois irá sobrescrever o 2. talvez o if abaixo resolva
                first_pos = self.lista_tarefa.index(0)
                last_pos = first_pos + vm.vCPU

                # Último 0 encontrado
                # last_pos = len(self.lista_tarefa) - self.lista_tarefa[::-1].index(0) # - 1

                for i in range(first_pos, last_pos):
                    # print(i)
                    # este if
                    if self.lista_tarefa[i] == 0:
                        self.lista_tarefa[i] = vm.id

            if self.lista_tarefa.count(0) == 0:
                self.lista_cheia = True
            else:
                self.lista_cheia = False
            # cpu.info()
        else:
            print("Lista cheia")

    def removerTarefa(self, vm):
        for i in range(len(self.lista_tarefa)):
            if vm.id == self.lista_tarefa[i]:
                self.lista_tarefa[i] = 0
        # print(self.vm_list)
        self.vm_list.remove(vm)

        if self.lista_tarefa.count(0) > 0:
            self.lista_cheia = False
        # cpu.info()
    
    def info(self):
        print(self.lista_tarefa)
        
         #print("tempo: " + tempo)
    
tempo = 0 # primeira tarefa em 20 min
tempo_max = 0 # tempo max first fit = 170 minutos aumentar de 5min em 5 min por ciclo
ciclo = 0
rodada = 0
cont = 0
vm_running_list = []
vm_pending_list = []
list_espera = []
list_ordenada = []

# def main():
cpu = CPU(1, Status.OCIOSO.value)

#Lista de VM's n
vm1 = VM(1, 4, 35, 40, 3)
vm2 = VM(2, 2, 40, 45, 1)
vm3 = VM(3, 4, 30, 45, 1)
vm4 = VM(4, 4, 25, 20, 3) ##
vm5 = VM(5, 2, 40, 25, 3)##
vm6 = VM(6, 4, 20, 20, 2) ##
vm7 = VM(7, 1, 20, 40, 0)##
vm8 = VM(8, 4, 20, 30, 1)
vm9 = VM(9, 4 , 10, 20, 2) ##
vm10 = VM(10, 1, 35, 30, 3)##

# vm_list.append(vm1).append(vm2).append(vm3).append(vm4).append(vm5).append(vm6).append(vm7).append(vm8).append(vm9).append(vm10)
vm_list = [vm1, vm2, vm3, vm4, vm5, vm6, vm7, vm8, vm9, vm10]
cpu.receberLista(vm_list)
    
# cpu.info()
# cpu.alocarTarefa(vm1)
# cpu.alocarTarefa(vm2)
# cpu.removerTarefa(vm1)
# cpu.removerTarefa(vm2)
# cpu.alocarTarefa(vm3)
# cpu.info()
    
while len(cpu.vm_list) > 0:
    print(" ")
    print("===  ===  ===  ")
    print("Ciclo:", ciclo, "|", tempo, "min.")

    # Verificia se há alguma tarefa em execução e quando irá sair
    if len(vm_running_list) > 0:
        for vmr in vm_running_list:
            # !!!!! erro: tem que considerar o tempo atual também, por isso não funciona
            if vmr.at < tempo and (vmr.et) == tempo:  #+ vmr.at
                cpu.removerTarefa(vmr)
                vm_running_list.remove(vmr)
                print("Saiu vm " + str(vmr.id) + " no tempo " + str(tempo))


    # Pega todas as vms que entram no tempo atual
    while cont < len(cpu.vm_list):
        vm = cpu.vm_list[cont]

        if vm.at == tempo:
            if vm not in list_espera:
                list_espera.append(vm)
        cont += 1

    cont = 0
    menor = 0
    list_menor = []
    
    # for i in list_espera:
    #     print(i, i.priority, i.et, i.at)
        
    # ordena as vms do tempo atual da prioridade menor e tempo menor
    # para maior
    while len(list_espera) > 0:
        for i, vm in enumerate(list_espera):
            if i == 0:
                menor = vm
            else:
                if vm.priority < menor.priority:
                    menor = vm
                if vm.priority == menor.priority:
                    if vm.et < menor.et:
                        menor = vm
            
        list_menor.append(menor)
        cont += 1
        list_espera.remove(menor)
    cont = 0

    # print("Lista espera:", list_menor)
    list_ordenada.extend(list_menor)
    # print("Lista ordenada:", list_ordenada)
    # print("Lista pending:", vm_pending_list)
    # Reseta a lista de prioridade ordenada do tempo atual para não atrapalhar o próximo tempo
    list_menor = []

    # Verifica e aloca tarefas
    while cont < len(list_ordenada):
        vm = list_ordenada[cont]

        if cpu.verificarEspaço(vm):
            vm.et += tempo
            cpu.alocarTarefa(vm)
            vm_running_list.append(vm)
            list_ordenada.remove(vm)
            print("Entrou vm " + str(vm.id) + " no tempo " + str(tempo))
        cont += 1
    cont = 0


    cpu.info()
    tempo += 5
    ciclo += 1






    
    # while rodada < 5:
    # futuramente, comparar tempo estimado caso tempo de chegada e prioridade sejam iguais
    # while cont < len(cpu.vm_list):
    #     pass
    #     vm = cpu.vm_list[cont]
    #     # print(vm)
    #     # print(cpu.vm_list)
    #     # print(vm_pending_list)
        
        
    #     # print("antes ", cpu.lista_cheia)
    #         # print("depois ", cpu.lista_cheia)
    #     if len(vm_pending_list) > 0:
    #         # como verifica todas uma por uma, pode quebrar a order quando a lista estiver ordenada em piroridade e outros
    #         for i, vmp in enumerate(vm_pending_list):
    #             if cpu.verificarEspaço(vmp):
    #                 vmp.et += tempo
    #                 cpu.alocarTarefa(vmp)
    #                 vm_running_list.append(vmp)
    #                 vm_pending_list.pop(i)
    #                 print("Entrou vm " + str(vmp.id) + " no tempo " + str(tempo))

    #     if vm.at == tempo:
    #         list_espera.append(vm)

    #         if cpu.verificarEspaço(vm):
    #             # problema: a verificação de espaço só ocorre dentro do alocarTarefa,
    #             # então se tiver 1 espaço mas precisa de 2 não vai alocar, mas vai fazer o resto aqui
    #             vm.et += tempo
    #             cpu.alocarTarefa(vm)
    #             vm_running_list.append(vm)
    #             print("Entrou vm " + str(vm.id) + " no tempo " + str(tempo))
    #         else:
    #             if not vm in vm_pending_list:
    #                 vm_pending_list.append(vm)
       
            
    #     # print(cpu.vm_list[cont])
    #     # print(vm_running_list)
    #     cont += 1
    # cont = 0

    # menor = 0
    
    # for i, vm in enumerate(list_espera):
    #     if i == 0:
    #         menor = vm
    #     else:
    #         if vm.priority < menor.priority:
    #             menor = vm

    # print(menor)

    



    # for vm in cpu.vm_list:
        # print(vm)
    
    # if cont == 10:
    #     cont = 0
    #     vm = cpu.vm_list[cont]
    # else:
    #     vm = cpu.vm_list[cont]
    #     cont += 1
        
    # # for vm in cpu.vm_list:
    # if not cpu.lista_cheia:
    #     if vm.at == tempo:
    #         cpu.alocarTarefa(vm)
    #         vm_running_list.append(vm)
    #         print("Entrou vm " + str(vm.id) + " no tempo " + str(tempo))
    # if len(vm_running_list) > 0:
    #     for vmr in vm_running_list:
    #         if vmr.at < tempo and (vmr.et + vmr.at) == tempo:
    #             cpu.removerTarefa(vmr)
    #             vm_running_list.remove(vmr)
    #             print("Saiu vm " + str(vmr.id) + " no tempo " + str(tempo))
    # # if vm.at < tempo and (vm.et + vm.at) == tempo:
    # #     cpu.removerTarefa(vm)
    # #     print("Saiu vm " + str(vm.id) + " no tempo " + str(tempo))
    # # cpu.alocarTarefa(vm)
    
    # print(cpu.vm_list)
    # cpu.info()
    # tempo += 5
    # ciclo += 1