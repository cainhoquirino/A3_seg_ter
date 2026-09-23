import tkinter as tk
from tkinter import messagebox

# --- Paleta de Cores ---
COR_PRIMARIA = "#005bb5"      # Azul Principal
COR_FUNDO = "#f0f4f8"         # Azul claro/gelo para o fundo
COR_TEXTO = "#333333"         # Cinza escuro para boa leitura
COR_BOTAO_TEXTO = "#ffffff"   # Branco para o texto dos botões
COR_INPUT = "#ffffff"         # Branco para os campos de digitação

class AppLoginCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Acesso")
        
        # --- TAMANHO DA TELA ALTERADO AQUI ---
        self.root.geometry("400x500") 
        
        self.root.configure(bg=COR_FUNDO)
        self.root.resizable(False, False)

        # Criando os frames para as duas telas
        self.frame_login = tk.Frame(self.root, bg=COR_FUNDO)
        self.frame_cadastro = tk.Frame(self.root, bg=COR_FUNDO)

        self.montar_tela_login()
        self.montar_tela_cadastro()

        # Inicia mostrando a tela de login
        self.mostrar_login()

    def mostrar_login(self):
        self.frame_cadastro.pack_forget()
        self.frame_login.pack(fill="both", expand=True)

    def mostrar_cadastro(self):
        self.frame_login.pack_forget()
        self.frame_cadastro.pack(fill="both", expand=True)

    def criar_label(self, frame, texto, tamanho=12, negrito=False):
        fonte = ("Arial", tamanho, "bold") if negrito else ("Arial", tamanho)
        return tk.Label(frame, text=texto, bg=COR_FUNDO, fg=COR_TEXTO, font=fonte)

    def criar_input(self, frame, oculto=False):
        show_char = "*" if oculto else ""
        return tk.Entry(frame, bg=COR_INPUT, fg=COR_TEXTO, font=("Arial", 12), show=show_char, relief="flat", highlightbackground=COR_PRIMARIA, highlightthickness=1)

    def criar_botao(self, frame, texto, comando, cor_fundo=COR_PRIMARIA, cor_texto=COR_BOTAO_TEXTO):
        return tk.Button(frame, text=texto, bg=cor_fundo, fg=cor_texto, font=("Arial", 12, "bold"), relief="flat", cursor="hand2", command=comando)

    # --- TELA DE LOGIN ---
    def montar_tela_login(self):
        # Título
        self.criar_label(self.frame_login, "Bem-vindo", tamanho=20, negrito=True).pack(pady=(45, 35))

        # Campo Usuário
        self.criar_label(self.frame_login, "Usuário:").pack(anchor="w", padx=50)
        self.entry_login_user = self.criar_input(self.frame_login)
        self.entry_login_user.pack(fill="x", padx=50, pady=(0, 15), ipady=5)

        # Campo Senha
        self.criar_label(self.frame_login, "Senha:").pack(anchor="w", padx=50)
        self.entry_login_senha = self.criar_input(self.frame_login, oculto=True)
        self.entry_login_senha.pack(fill="x", padx=50, pady=(0, 35), ipady=5)

        # Botão Entrar
        btn_entrar = self.criar_botao(self.frame_login, "ENTRAR", self.acao_login)
        btn_entrar.pack(fill="x", padx=50, pady=(0, 15), ipady=5)

        # Link para Cadastro
        btn_ir_cadastro = tk.Button(self.frame_login, text="Não tem uma conta? Cadastre-se", bg=COR_FUNDO, fg=COR_PRIMARIA, font=("Arial", 10, "underline"), relief="flat", cursor="hand2", command=self.mostrar_cadastro, activebackground=COR_FUNDO, activeforeground=COR_PRIMARIA, bd=0)
        btn_ir_cadastro.pack()

    # --- TELA DE CADASTRO ---
    def montar_tela_cadastro(self):
        # Título
        self.criar_label(self.frame_cadastro, "Criar Conta", tamanho=20, negrito=True).pack(pady=(35, 25))

        # Campo Usuário
        self.criar_label(self.frame_cadastro, "Novo Usuário:").pack(anchor="w", padx=50)
        self.entry_cad_user = self.criar_input(self.frame_cadastro)
        self.entry_cad_user.pack(fill="x", padx=50, pady=(0, 15), ipady=5)

        # Campo Senha
        self.criar_label(self.frame_cadastro, "Senha:").pack(anchor="w", padx=50)
        self.entry_cad_senha = self.criar_input(self.frame_cadastro, oculto=True)
        self.entry_cad_senha.pack(fill="x", padx=50, pady=(0, 15), ipady=5)

        # Confirmar Senha
        self.criar_label(self.frame_cadastro, "Confirmar Senha:").pack(anchor="w", padx=50)
        self.entry_cad_conf_senha = self.criar_input(self.frame_cadastro, oculto=True)
        self.entry_cad_conf_senha.pack(fill="x", padx=50, pady=(0, 25), ipady=5)

        # Botão Cadastrar
        btn_cadastrar = self.criar_botao(self.frame_cadastro, "CADASTRAR", self.acao_cadastrar)
        btn_cadastrar.pack(fill="x", padx=50, pady=(0, 15), ipady=5)

        # Link para Voltar
        btn_voltar = tk.Button(self.frame_cadastro, text="Já tem conta? Faça Login", bg=COR_FUNDO, fg=COR_PRIMARIA, font=("Arial", 10, "underline"), relief="flat", cursor="hand2", command=self.mostrar_login, activebackground=COR_FUNDO, activeforeground=COR_PRIMARIA, bd=0)
        btn_voltar.pack()

    # --- FUNÇÕES DE AÇÃO ---
    def acao_login(self):
        usuario = self.entry_login_user.get()
        senha = self.entry_login_senha.get()
        
        # Aqui você colocaria a lógica de validação com banco de dados
        if usuario == "" or senha == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
        else:
            messagebox.showinfo("Sucesso", f"Bem-vindo(a), {usuario}!")

    def acao_cadastrar(self):
        usuario = self.entry_cad_user.get()
        senha = self.entry_cad_senha.get()
        conf_senha = self.entry_cad_conf_senha.get()
        
        if usuario == "" or senha == "" or conf_senha == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
        elif senha != conf_senha:
            messagebox.showerror("Erro", "As senhas não coincidem!")
        else:
            # Aqui você salvaria o usuário no banco de dados
            messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
            self.entry_cad_user.delete(0, tk.END)
            self.entry_cad_senha.delete(0, tk.END)
            self.entry_cad_conf_senha.delete(0, tk.END)
            self.mostrar_login()

if __name__ == "__main__":
    janela_principal = tk.Tk()
    app = AppLoginCadastro(janela_principal)
    janela_principal.mainloop()
