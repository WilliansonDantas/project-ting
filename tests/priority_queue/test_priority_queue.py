import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():

    instanceTest = PriorityQueue()
    with pytest.raises(IndexError):
        instanceTest.search(99)

    instanceTest = PriorityQueue()
    instanceTest.enqueue({"nome_do_arquivo": "arquivo_test_0.txt",
                          "qtd_linhas": 4})
    instanceTest.enqueue({"nome_do_arquivo": "arquivo_test_1.txt",
                          "qtd_linhas": 6})
    instanceTest.enqueue({"nome_do_arquivo": "arquivo_test_2.txt",
                          "qtd_linhas": 3})
    instanceTest.enqueue({"nome_do_arquivo": "arquivo_test_3.txt",
                          "qtd_linhas": 9})
    assert len(instanceTest.high_priority) == 2
    assert len(instanceTest.regular_priority) == 2

    instanceTest = PriorityQueue()
    instanceTest.enqueue({"nome_do_arquivo": "arquivo_test_0.txt",
                          "qtd_linhas": 4})
    instanceTest.enqueue({"nome_do_arquivo": "arquivo_test_1.txt",
                          "qtd_linhas": 6})
    instanceTest.enqueue({"nome_do_arquivo": "arquivo_test_2.txt",
                          "qtd_linhas": 3})
    instanceTest.enqueue({"nome_do_arquivo": "arquivo_test_3.txt",
                          "qtd_linhas": 9})
    assert instanceTest.dequeue() == {"nome_do_arquivo": "arquivo_test_0.txt",
                                      "qtd_linhas": 4}
    assert len(instanceTest.high_priority) == 1
    assert len(instanceTest.regular_priority) == 2

    instanceTest = PriorityQueue()
    instanceTest.enqueue({"nome_do_arquivo": "arquivo_test_0.txt",
                          "qtd_linhas": 4})
    instanceTest.enqueue({"nome_do_arquivo": "arquivo_test_1.txt",
                          "qtd_linhas": 6})
    instanceTest.enqueue({"nome_do_arquivo": "arquivo_test_2.txt",
                          "qtd_linhas": 3})
    instanceTest.enqueue({"nome_do_arquivo": "arquivo_test_3.txt",
                          "qtd_linhas": 9})
    assert instanceTest.search(0) == {"nome_do_arquivo": "arquivo_test_0.txt",
                                      "qtd_linhas": 4}
    assert instanceTest.search(1) == {"nome_do_arquivo": "arquivo_test_2.txt",
                                      "qtd_linhas": 3}
    assert instanceTest.search(2) == {"nome_do_arquivo": "arquivo_test_1.txt",
                                      "qtd_linhas": 6}
    assert instanceTest.search(3) == {"nome_do_arquivo": "arquivo_test_3.txt",
                                      "qtd_linhas": 9}
