import customtkinter as ctk
from tkinter import filedialog, messagebox

# Fucntions


def normalizar_chave(chave):
    return chave % 26


def cifrar(texto, chave):
    chave = normalizar_chave(chave)
    resultado = ""
    for c in texto:
        if c.isupper():
            codigo = ord(c) - ord('A')
            resultado += chr((codigo + chave) % 26 + ord('A'))
        elif c.islower():
            codigo = ord(c) - ord('a')
            resultado += chr((codigo + chave) % 26 + ord('a'))
        else:
            resultado += c
    return resultado


def decifrar(texto, chave):
    return cifrar(texto, -chave)


def brute_force(texto):
    resultado = ""
    for chave in range(1, 26):
        resultado += f"Chave {chave:02d}: {decifrar(texto, chave)}\n"
    return resultado


def ler_arquivo(nome):
    try:
        with open(nome, "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado.")
        return None


def salvar_arquivo(nome, conteudo):
    with open(nome, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)


# UI

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class AppCifraCesar(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cifra de César - Pro")
        self.geometry("900x650")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = ctk.CTkFrame(self, width=220, corner_radius=20)

        self.sidebar_frame.grid(
            row=0, column=0, sticky="nsew", padx=15, pady=15)

        self.sidebar_frame.grid_rowconfigure(
            8, weight=1)

        self.logo_label = ctk.CTkLabel(
            self.sidebar_frame, text="OPERAÇÕES", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.lbl_chave = ctk.CTkLabel(
            self.sidebar_frame, text="Chave de Deslocamento:", anchor="w")
        self.lbl_chave.grid(row=1, column=0, padx=20, pady=(10, 0), sticky="w")

        self.entry_chave = ctk.CTkEntry(
            self.sidebar_frame, placeholder_text="Ex: 3")
        self.entry_chave.grid(row=2, column=0, padx=20,
                              pady=(5, 20), sticky="ew")

        self.btn_cifrar = ctk.CTkButton(
            self.sidebar_frame, text="Criptografar Texto", command=self.criptografar_texto)
        self.btn_cifrar.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.btn_decifrar = ctk.CTkButton(
            self.sidebar_frame, text="Descriptografar Texto", command=self.descriptografar_texto)
        self.btn_decifrar.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

        self.btn_brute = ctk.CTkButton(self.sidebar_frame, text="Força Bruta", fg_color="transparent",
                                       border_width=2, text_color=("gray10", "#DCE4EE"), command=self.ataque_forca_bruta)
        self.btn_brute.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        self.divisor = ctk.CTkProgressBar(self.sidebar_frame, height=2)
        self.divisor.set(1)
        self.divisor.grid(row=6, column=0, padx=20, pady=20, sticky="ew")
        self.divisor.configure(progress_color="gray50")

        self.lbl_arq = ctk.CTkLabel(self.sidebar_frame, text="ARQUIVOS .TXT", font=ctk.CTkFont(
            size=12, weight="bold"), text_color="gray")
        self.lbl_arq.grid(row=7, column=0, padx=20, pady=(0, 10), sticky="w")

        self.btn_arq_cifrar = ctk.CTkButton(self.sidebar_frame, text="Criptografar Arq.",
                                            command=self.criptografar_arquivo, fg_color="#2E8B57", hover_color="#20603D")
        self.btn_arq_cifrar.grid(row=8, column=0, padx=20, pady=5, sticky="ew")

        self.btn_arq_decifrar = ctk.CTkButton(self.sidebar_frame, text="Descriptografar Arq.",
                                              command=self.descriptografar_arquivo, fg_color="#2E8B57", hover_color="#20603D")
        self.btn_arq_decifrar.grid(
            row=9, column=0, padx=20, pady=(5, 20), sticky="ew")

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(
            row=0, column=1, sticky="nsew", padx=(0, 15), pady=15)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(3, weight=1)

        self.lbl_input = ctk.CTkLabel(
            self.main_frame, text="Texto de Entrada", font=ctk.CTkFont(size=14, weight="bold"))
        self.lbl_input.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.caixa_texto = ctk.CTkTextbox(
            self.main_frame, corner_radius=15, border_width=1)
        self.caixa_texto.grid(row=1, column=0, sticky="nsew", pady=(0, 20))

        self.lbl_output = ctk.CTkLabel(
            self.main_frame, text="Resultado", font=ctk.CTkFont(size=14, weight="bold"))
        self.lbl_output.grid(row=2, column=0, sticky="w", pady=(0, 5))

        self.caixa_resultado = ctk.CTkTextbox(
            self.main_frame, corner_radius=15, fg_color=("gray90", "#2b2b2b"), border_width=0)
        self.caixa_resultado.grid(row=3, column=0, sticky="nsew")
        self.caixa_resultado.configure(state="disabled")

    # Functions aux

    def obter_chave(self):
        try:
            val = int(self.entry_chave.get())
            return val
        except ValueError:
            messagebox.showerror("Erro", "A chave deve ser um número inteiro.")
            return None

    def escrever_resultado(self, texto):
        self.caixa_resultado.configure(state="normal")
        self.caixa_resultado.delete("1.0", "end")
        self.caixa_resultado.insert("end", texto)
        self.caixa_resultado.configure(state="disabled")

    def criptografar_texto(self):
        chave = self.obter_chave()
        if chave is not None:
            texto = self.caixa_texto.get("1.0", "end-1c")
            self.escrever_resultado(cifrar(texto, chave))

    def descriptografar_texto(self):
        chave = self.obter_chave()
        if chave is not None:
            texto = self.caixa_texto.get("1.0", "end-1c")
            self.escrever_resultado(decifrar(texto, chave))

    def ataque_forca_bruta(self):
        texto = self.caixa_texto.get("1.0", "end-1c")
        self.escrever_resultado(brute_force(texto))

    def criptografar_arquivo(self):
        chave = self.obter_chave()
        if chave is None:
            return
        entrada = filedialog.askopenfilename(
            title="Abrir arquivo", filetypes=[("Texto", "*.txt")])
        if not entrada:
            return
        saida = filedialog.asksaveasfilename(
            title="Salvar como", defaultextension=".txt", filetypes=[("Texto", "*.txt")])
        if not saida:
            return
        texto = ler_arquivo(entrada)
        if texto:
            salvar_arquivo(saida, cifrar(texto, chave))
            messagebox.showinfo("Sucesso", "Arquivo Criptografado salvo!")

    def descriptografar_arquivo(self):
        chave = self.obter_chave()
        if chave is None:
            return
        entrada = filedialog.askopenfilename(
            title="Abrir arquivo", filetypes=[("Texto", "*.txt")])
        if not entrada:
            return
        saida = filedialog.asksaveasfilename(
            title="Salvar como", defaultextension=".txt", filetypes=[("Texto", "*.txt")])
        if not saida:
            return
        texto = ler_arquivo(entrada)
        if texto:
            salvar_arquivo(saida, decifrar(texto, chave))
            messagebox.showinfo("Sucesso", "Arquivo Descriptografado salvo!")


if __name__ == "__main__":
    app = AppCifraCesar()
    app.mainloop()
