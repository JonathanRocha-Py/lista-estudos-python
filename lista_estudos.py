```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerenciador de Lista de Estudos
Jonathan Rocha — Outubro/2026
Exercício de lógica de programação
"""

from datetime import datetime

def inicializar_lista():
    """Retorna uma lista vazia para os estudos"""
    return []

def adicionar_item(lista, descricao):
    """Adiciona um novo item à lista"""
    novo_item = {
        "id": len(lista) + 1,
        "descricao": descricao,
        "data": datetime.now().strftime("%d/%m/%Y"),
        "concluido": False
    }
    lista.append(novo_item)
    print(f"✅ Item '{descricao}' adicionado com sucesso!")

def listar_itens(lista):
    """Exibe todos os itens da lista"""
    if not lista:
        print("\n📋 A lista está vazia.")
        return
    
    print("\n" + "=" * 50)
    print("   LISTA DE ESTUDOS")
    print("=" * 50)
    
    for item in lista:
        status = "✅ Concluído" if item["concluido"] else "⏳ Pendente"
        print(f"\nID: {item['id']}")
        print(f"Descrição: {item['descricao']}")
        print(f"Data: {item['data']}")
        print(f"Status: {status}")
    
    total = len(lista)
    concluidos = sum(1 for i in lista if i["concluido"])
    pendentes = total - concluidos
    print("\n" + "-" * 50)
    print(f"Total: {total} | Concluídos: {concluidos} | Pendentes: {pendentes}")
    print("=" * 50)

def marcar_concluido(lista, item_id):
    """Marca um item como concluído"""
    for item in lista:
        if item["id"] == item_id:
            item["concluido"] = True
            print(f"✅ Item {item_id} marcado como concluído!")
            return
    print(f"❌ Item com ID {item_id} não encontrado.")

def remover_item(lista, item_id):
    """Remove um item da lista"""
    for indice, item in enumerate(lista):
        if item["id"] == item_id:
            removido = lista.pop(indice)
            print(f"✅ Item '{removido['descricao']}' removido com sucesso!")
            return
    print(f"❌ Item com ID {item_id} não encontrado.")

def main():
    print("=" * 50)
    print("   GERENCIADOR DE LISTA DE ESTUDOS")
    print("=" * 50)
    
    # Inicializa com exemplos
    minha_lista = inicializar_lista()
    adicionar_item(minha_lista, "Estudar conceitos básicos de Python")
    adicionar_item(minha_lista, "Praticar exercícios de lógica")
    adicionar_item(minha_lista, "Aprender conceitos iniciais de SAP ABAP")
    
    # Mostra a lista completa
    listar_itens(minha_lista)
    
    # Marca um item como concluído
    marcar_concluido(minha_lista, 1)
    
    # Mostra atualizada
    listar_itens(minha_lista)
    
    print("\n✅ Programa executado com sucesso!")

if __name__ == "__main__":
    main()
