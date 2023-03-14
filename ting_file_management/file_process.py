from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    pathProcess = txt_importer(path_file)
    outPut = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(pathProcess),
        "linhas_do_arquivo": pathProcess
    }
    queueInstance = instance.queue
    for item in queueInstance:
        if item["nome_do_arquivo"] == path_file:
            return None
    instance.enqueue(outPut)
    print(outPut)


def remove(instance):
    queueInstance = instance.queue
    if len(queueInstance) == 0:
        print("Não há elementos")
        return
    pathFile = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    print(f"Arquivo {pathFile} removido com sucesso")
    

def file_metadata(instance, position):
    """Aqui irá sua implementação"""
