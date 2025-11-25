import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime


class FormularioCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro")
        self.root.geometry("400x450")
        self.root.configure(bg='white')
        
        # Frame principal centralizado
        self.main_frame = tk.Frame(root, bg='white', padx=30, pady=30)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Campo Nome
        tk.Label(self.main_frame, text="Nome:", bg='white', fg='black', font=('Arial', 10)).grid(row=0, column=0, sticky='w', pady=(0, 5))
        self.nome_entry = tk.Entry(self.main_frame, width=30, fg='black')
        self.nome_entry.insert(0, "Nome")
        self.nome_entry.bind('<FocusIn>', lambda e: self.clear_placeholder(e, "Nome"))
        self.nome_entry.bind('<FocusOut>', lambda e: self.restore_placeholder(e, "Nome"))
        self.nome_entry.config(fg='gray')
        self.nome_entry.grid(row=1, column=0, pady=(0, 15))
        
        # Campo Sobrenome
        tk.Label(self.main_frame, text="Sobrenome:", bg='white', fg='black', font=('Arial', 10)).grid(row=2, column=0, sticky='w', pady=(0, 5))
        self.sobrenome_entry = tk.Entry(self.main_frame, width=30, fg='black')
        self.sobrenome_entry.insert(0, "Sobrenome")
        self.sobrenome_entry.bind('<FocusIn>', lambda e: self.clear_placeholder(e, "Sobrenome"))
        self.sobrenome_entry.bind('<FocusOut>', lambda e: self.restore_placeholder(e, "Sobrenome"))
        self.sobrenome_entry.config(fg='gray')
        self.sobrenome_entry.grid(row=3, column=0, pady=(0, 15))
        
        # Seletor de Data de Nascimento
        tk.Label(self.main_frame, text="Data de Nascimento:", bg='white', fg='black', font=('Arial', 10)).grid(row=4, column=0, sticky='w', pady=(0, 5))
        self.data_nascimento = DateEntry(
            self.main_frame, 
            width=27, 
            background='darkblue',
            foreground='white', 
            borderwidth=2,
            date_pattern='dd/mm/yyyy',
            maxdate=datetime.now(),
            fg='black'
        )
        self.data_nascimento.grid(row=5, column=0, pady=(0, 15))
        
        # Campo Sexo (Dropdown)
        tk.Label(self.main_frame, text="Sexo:", bg='white', fg='black', font=('Arial', 10)).grid(row=6, column=0, sticky='w', pady=(0, 5))
        self.sexo_var = tk.StringVar()
        self.sexo_combo = ttk.Combobox(
            self.main_frame, 
            textvariable=self.sexo_var,
            values=["Masculino", "Feminino", "Outro", "Prefiro não informar"],
            state='readonly',
            width=28
        )
        self.sexo_combo.grid(row=7, column=0, pady=(0, 25))
        
        # Frame para botões
        button_frame = tk.Frame(self.main_frame, bg='white')
        button_frame.grid(row=8, column=0, pady=(10, 0))
        
        # Botão Enviar (azul com texto branco)
        self.btn_enviar = tk.Button(
            button_frame,
            text="Enviar",
            command=self.enviar,
            bg='blue',
            fg='white',
            width=12,
            height=1,
            font=('Arial', 10, 'bold'),
            cursor='hand2',
            relief='flat'
        )
        self.btn_enviar.pack(side='left', padx=(0, 10))
        
        # Botão Limpar (branco com borda e texto vermelho)
        self.btn_limpar = tk.Button(
            button_frame,
            text="Limpar",
            command=self.limpar,
            bg='white',
            fg='red',
            width=12,
            height=1,
            font=('Arial', 10, 'bold'),
            cursor='hand2',
            relief='solid',
            borderwidth=2,
            highlightbackground='red',
            highlightcolor='red',
            highlightthickness=1
        )
        self.btn_limpar.config(bd=2)
        self.btn_limpar.pack(side='left')
    
    def clear_placeholder(self, event, placeholder):
        widget = event.widget
        if widget.get() == placeholder:
            widget.delete(0, tk.END)
            widget.config(fg='black')
    
    def restore_placeholder(self, event, placeholder):
        widget = event.widget
        if widget.get() == '':
            widget.insert(0, placeholder)
            widget.config(fg='gray')
    
    def enviar(self):
        # Validar se a data é a atual
        data_selecionada = self.data_nascimento.get_date()
        data_atual = datetime.now().date()
        
        if data_selecionada == data_atual:
            messagebox.showerror("Erro", "Insira uma data válida")
            return
        
        messagebox.showinfo("Sucesso", "Cadastro efetuado com sucesso!")
    
    def limpar(self):
        # Limpar campo Nome
        self.nome_entry.delete(0, tk.END)
        self.nome_entry.insert(0, "Nome")
        self.nome_entry.config(fg='gray')
        
        # Limpar campo Sobrenome
        self.sobrenome_entry.delete(0, tk.END)
        self.sobrenome_entry.insert(0, "Sobrenome")
        self.sobrenome_entry.config(fg='gray')
        
        # Resetar data para hoje
        self.data_nascimento.set_date(datetime.now())
        
        # Limpar seleção de sexo
        self.sexo_combo.set('')


if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioCadastro(root)
    root.mainloop()
