import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    list = txt_importer(path_file)

    insert = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list),
        "linhas_do_arquivo": list,
    }

    instance.enqueue(insert)

    print_str = str(insert)

    return print(f"{print_str}", file=sys.stdout)


def remove(instance):
    if len(instance) > 0:

        removed_file = instance.dequeue()["nome_do_arquivo"]

        return print(
            f"Arquivo {removed_file} removido com sucesso", file=sys.stdout
        )
    else:
        return print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    meta_list = instance.search(position)
    print_str = str(meta_list)
    return print(f"{print_str}", file=sys.stdout)
