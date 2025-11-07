import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox, filedialog
import tkinter as tk
from automator.sige_automator import SigeAutomator
from data.data_manager import DataManager


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("SIGE Automator 3.0")
        self.root.geometry("650x500")

        self.excel_path = ""
        self.navegador = tb.StringVar(value='chrome')
        self.dry_run = tb.BooleanVar(value=False)

        self._montar_interface()

    def _montar_interface(self):
        tb.Label(
            self.root,
            text="Automação Escolar 3.0",
            font=("Segoe UI", 20, "bold"),
            bootstyle="primary"
        ).pack(pady=20)

        frame = tb.Frame(self.root, padding=10)
        frame.pack(fill=X, padx=30)

        tb.Label(frame, text="Usuário:").pack(anchor=W)
        self.entrada_usuario = tb.Entry(frame, width=50)
        self.entrada_usuario.pack(anchor=W)

        tb.Label(frame, text="Senha:").pack(anchor=W)
        self.entrada_senha = tb.Entry(frame, width=50, show="*")
        self.entrada_senha.pack(anchor=W)

        tb.Label(frame, text="Arquivo Excel:").pack(anchor=W)
        excel_frame = tb.Frame(frame)
        excel_frame.pack(fill=X, pady=5)
        self.entrada_excel = tb.Entry(excel_frame, width=40)
        self.entrada_excel.pack(side=LEFT, padx=(0, 10))
        tb.Button(excel_frame, text="Selecionar", command=self.selecionar_arquivo).pack(side=LEFT)

        tb.Checkbutton(frame, text="Modo simulação", variable=self.dry_run).pack(anchor=W, pady=5)

        tb.Button(
            frame,
            text="Importar do Word",
            bootstyle="info",
            command=self.importar_word_ui
        ).pack(pady=10)

        tb.Button(
            self.root,
            text="Executar",
            bootstyle="success",
            command=self.executar
        ).pack(pady=10)

        self.status = tb.Label(self.root, text="", bootstyle="info")
        self.status.pack(pady=10)

    def selecionar_arquivo(self):
        path = filedialog.askopenfilename(filetypes=[("Planilhas Excel", "*.xlsx")])
        if path:
            self.excel_path = path
            self.entrada_excel.delete(0, tk.END)
            self.entrada_excel.insert(0, path)

    def executar(self):
        usuario, senha = self.entrada_usuario.get(), self.entrada_senha.get()
        if not usuario or not senha or not self.excel_path:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        self.status.config(text="⏳ Executando...")
        self.root.update()

        try:
            automator = SigeAutomator(self.excel_path, dry_run=self.dry_run.get())
            automator.executar(usuario, senha)
            self.status.config(text="✅ Concluído! Verifique o relatório.")
            messagebox.showinfo("Sucesso", "Processo finalizado com sucesso!")
        except Exception as e:
            self.status.config(text="❌ Falha na execução.")
            messagebox.showerror("Erro", f"Ocorreu um erro durante a execução:\n{e}")

    def importar_word_ui(self):
        caminho = filedialog.askopenfilename(
            title="Selecione o arquivo Word",
            filetypes=[("Documentos Word", "*.docx")]
        )
        if caminho:
            try:
                excel_path = DataManager.importar_dados_word(caminho)
                messagebox.showinfo("Sucesso", f"Arquivo importado e salvo em:\n{excel_path}")
                self.excel_path = excel_path
                self.entrada_excel.delete(0, tk.END)
                self.entrada_excel.insert(0, excel_path)
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao importar o arquivo:\n{e}")
