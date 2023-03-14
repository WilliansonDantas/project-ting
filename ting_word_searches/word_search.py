def exists_word(word, instance):
    queueInstance = instance.queue
    wordCaseInsensitive = word.lower()
    wordResult = []
    for file in queueInstance:
        lines = []
        for index, item in enumerate(file["linhas_do_arquivo"]):
            itemCaseInsensitive = item.lower()
            if wordCaseInsensitive in itemCaseInsensitive:
                lines.append({
                    "linha": index + 1
                })
        if len(lines) > 0:
            wordResult.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": lines
            })
    return wordResult


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
