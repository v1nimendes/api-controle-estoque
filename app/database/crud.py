from .db import get_conexacao 
from fastapi import HTTPException
import sqlite3

def add_produto(nome: str, quantidade: int):
    conn = get_conexacao()
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO estoque (nome, quantidade) VALUES (?, ?)', (nome, quantidade))
        conn.commit()

        novo_id = cursor.lastrowid
        return {"ID": novo_id, "Nome": nome, "Quantidade": quantidade}
    
    except sqlite3.IntegrityError:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Produto já existe")
    finally:
        conn.close()


def listar_produtos():
    conn = get_conexacao()
    cursor = conn.cursor()

    cursor.execute('SELECT id, nome, quantidade FROM estoque')
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "nome": r[1], "quantidade": r[2]} for r in rows]

def excluir_produto(id: int):
    conn = get_conexacao()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM estoque WHERE id = ?', (id,))

    if cursor.rowcount == 0:
        conn.close() 
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    conn.commit()
    conn.close()

    return {"message": "Produto excluído com sucesso"}


def editar_quantidade(id: int, quantidade: int):
    conn = get_conexacao()
    cursor = conn.cursor()

    cursor.execute('UPDATE estoque SET quantidade = ? WHERE id = ?', (quantidade, id))

    conn.commit()
    conn.close()

    return {"message": "Produto editado com sucesso"}

