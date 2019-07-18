import conexao
import main

# Adicionar Usuarios
def adicionar(control):
    # Requisitos e SQL
    nome = control.Et_Nome.get()
    telefone = control.Et_Telefone.get()
    sql = f"INSERT INTO usuario (nome, telefone) VALUES ('{nome}', '{telefone}');"

    # Tente Conectar
    try:
        conn = conexao.connexao()
        cursor = conn.cursor()
        cursor.execute(sql) # Execute
        conn.commit()
        cursor.close() # Concluido
        # Pós
        control.lb_Status.configure(text="Adicionado com Sucesso!", foreground="blue")
        clearField(control)
        atualizar(control)
    except Exception as e:
        control.lb_Status.configure(text="Nao Adicionado", foreground="red")
        print(f"Erro: {e}")
    
# Remover usuario
def remover(control):
    # Pega o valor selecionado
    values = control.tv_Treeview.item(control.tv_Treeview.focus())
    # Se tiver dados nele:
    if values['values']:
        # Formar SQL
        id_contato = values['values'][0]
        sql = f"delete from usuario where id = {id_contato};"
        # Tente Conectar
        try:
            conn = conexao.connexao()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            # Pós
            control.lb_Status.configure(text="Removido com Sucesso!", foreground="blue")
            atualizar(control)
        except Exception as e:
            print(f"Erro: {e}")
    else:
        control.lb_Status.configure(text="Selecione um campo", foreground="blue")

    
# Alterar
def alterar(control, modoAlterar):
    # Primeiro definir modo de alteração. Iniciar alteração ou conclui-la
    # |- Se não esta no modo de alteração, entre no modo de alteração, permitindo que o usuario mude os dados.
    if not modoAlterar:
        values = control.tv_Treeview.item(control.tv_Treeview.focus())
        clearField(control)
        control.id = values['values'][0]
        control.Et_Nome.insert(0, values['values'][1])
        control.Et_Telefone.insert(0, values['values'][2])
        control.lb_Status.configure(text=f"Alterando {values['values'][1]}...", foreground="blue")
        control.btn_Alterar['text'] = "Confirmar"
    # |- Se ja esta no modo de alteração, altere os dados no banco conforme o usuario mudou e saia do modo de alteração.
    else:
        id_contato = control.id
        nome_contato = control.Et_Nome.get()
        telefone_contato = control.Et_Telefone.get()
        sql = f"update usuario set nome='{nome_contato}', telefone='{telefone_contato}' where id = {id_contato};"
        try:
            conn = conexao.connexao()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            control.lb_Status.configure(text="Alterado com Sucesso!", foreground="blue")
            control.btn_Alterar['text'] = "Alterar"
            atualizar(control)
            clearField(control)
        except Exception as e:
            print(f"Erro: {e}")
    control.modoAlterar = not control.modoAlterar

# Atualizar Treeview
def atualizar(control):
    # Limpe todos os campos
    for i in control.tv_Treeview.get_children():
        control.tv_Treeview.delete(i) 
    # Pegue todos no banco e reponha-os
    sql = "SELECT * FROM usuario"
    try:
        conn = conexao.connexao()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = [coluna for coluna in cursor]
        # Alternar Cores
        control.tv_Treeview.tag_configure('gray', background="#CCCCCC")
        control.tv_Treeview.tag_configure('white', background="#FFF")
        color = ['gray', 'white']
        i = 2
        # Colocar na treeview
        for linha in resultado:
            i=0 if i>1 else 1
            control.tv_Treeview.insert("", "end", text=linha[0], value=[linha[0], linha[1], linha[2]], tags=(color[i],))
            i += 1
        cursor.close()
    except Exception as e:
        print(f"Erro: {e}")

# Limpar campos, nome e telefone
def clearField(control):
    control.Et_Nome.delete(0,"end")
    control.Et_Telefone.delete(0,"end")
