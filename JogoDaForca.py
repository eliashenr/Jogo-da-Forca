import tkinter as tk
import random

# Categorias e palavras originais
carros = ["bmw", "mercedes", "audi", "tesla", "ford", "chevrolet", "honda", "toyota"]
tecnologia = ["celular", "computador", "programacao", "python", "javascript"]
jogos = ["leagueoflegends", "jogo", "videogame", "xbox", "playstation", "nintendo"]
empresas = ["microsoft", "apple", "linux", "windows"]
redes_sociais = ["facebook", "instagram", "twitter", "whatsapp", "telegram"]
geral = ["carro", "casa", "comida", "bola", "familia", "futebol", "rede social", "internet"]

categorias = {
    "Carros": carros,
    "Tecnologia": tecnologia,
    "Jogos": jogos,
    "Empresas": empresas,
    "Redes Sociais": redes_sociais,
    "Geral": geral
}

# Função para iniciar novo jogo
def novo_jogo(event=None):
    global palavra, palavra_oculta, erros, max_erros, dica
    categoria, lista = random.choice(list(categorias.items()))
    palavra = random.choice(lista)
    palavra_oculta = ["_" if letra != " " else " " for letra in palavra]
    erros = []
    max_erros = 7
    dica = categoria
    dica_label.config(text=f"💡 Dica: {dica}")
    palavra_label.config(text=" ".join(palavra_oculta), fg="white")
    erros_label.config(text="Erros: ", fg="red")
    tentativas_label.config(text=f"Tentativas restantes: {max_erros}", fg="white")
    entrada.delete(0, tk.END)
    status_label.config(text="", fg="white", font=("Arial", 14, "normal"))
    canvas.delete("all")
    desenhar_forca(0)

# Função para verificar letra
def verificar_letra(event=None):
    global erros
    letra = entrada.get().lower()
    entrada.delete(0, tk.END)

    if not letra.isalpha() or len(letra) != 1:
        status_label.config(text="Digite apenas uma letra.", fg="yellow")
        return

    if letra in erros or letra in palavra_oculta:
        status_label.config(text="Você já tentou essa letra.", fg="yellow")
        return

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                palavra_oculta[i] = letra
        palavra_label.config(text=" ".join(palavra_oculta))
        status_label.config(text=f'✅ Boa! A letra "{letra}" está na palavra.', fg="lightgreen")
    else:
        erros.append(letra)
        status_label.config(text=f'❌ A letra "{letra}" não está na palavra.', fg="red")
        desenhar_forca(len(erros))
    
    erros_label.config(text="Erros: " + ", ".join(erros), fg="red")
    tentativas_label.config(text=f"Tentativas restantes: {max_erros - len(erros)}", fg="white")

    if "_" not in palavra_oculta:
        status_label.config(
            text=f"🎉 Parabéns! Você venceu! A palavra era: {palavra.upper()}",
            fg="#00BFFF",  # azul-claro
            font=("Arial", 14, "bold")
        )
    elif len(erros) >= max_erros:
        palavra_label.config(text=palavra.upper(), fg="red")
        status_label.config(text=f"💀 Você perdeu! A palavra era: {palavra.upper()}", fg="red", font=("Arial", 14, "bold"))

# Desenhar forca no Canvas
def desenhar_forca(erros):
    canvas.create_line(70, 300, 250, 300, width=4)  # base
    canvas.create_line(120, 300, 120, 50, width=4)  # poste
    canvas.create_line(120, 50, 220, 50, width=4)   # topo
    canvas.create_line(220, 50, 220, 80, width=4)   # corda

    if erros >= 1:
        canvas.create_oval(200, 80, 240, 120, width=3)  # cabeça
    if erros >= 2:
        canvas.create_line(220, 120, 220, 180, width=3)  # corpo
    if erros >= 3:
        canvas.create_line(220, 140, 190, 160, width=3)  # braço esq
    if erros >= 4:
        canvas.create_line(220, 140, 250, 160, width=3)  # braço dir
    if erros >= 5:
        canvas.create_line(220, 180, 190, 220, width=3)  # perna esq
    if erros >= 6:
        canvas.create_line(220, 180, 250, 220, width=3)  # perna dir
    if erros >= 7:
        canvas.create_text(170, 30, text="☠️ GAME OVER", font=("Arial", 14, "bold"), fill="red")

# Interface
root = tk.Tk()
root.title("🎯 Jogo da Forca")
root.geometry("600x650")
root.configure(bg="#001f3f")  # Azul marinho

# Layout principal
frame = tk.Frame(root, bg="#001f3f")
frame.pack(pady=20)

dica_label = tk.Label(frame, text="", font=("Arial", 15, "bold"), bg="#001f3f", fg="yellow")
dica_label.pack(pady=5)

palavra_label = tk.Label(frame, text="", font=("Arial", 30, "bold"), bg="#001f3f", fg="white")
palavra_label.pack(pady=15)

entrada = tk.Entry(frame, font=("Arial", 18), justify="center", width=5)
entrada.pack()
entrada.bind("<Return>", verificar_letra)

verificar_btn = tk.Button(frame, text="Verificar Letra (ENTER)", command=verificar_letra,
                          font=("Arial", 12), width=25, bg="white", relief="raised")
verificar_btn.pack(pady=8)

nova_btn = tk.Button(frame, text="Nova Partida (1)", command=novo_jogo,
                     font=("Arial", 12), width=25, bg="white", relief="raised")
nova_btn.pack(pady=8)

tentativas_label = tk.Label(frame, text="", font=("Arial", 12, "bold"), bg="#001f3f", fg="white")
tentativas_label.pack(pady=3)

erros_label = tk.Label(frame, text="", font=("Arial", 12, "bold"), bg="#001f3f", fg="red")
erros_label.pack(pady=3)

status_label = tk.Label(frame, text="", font=("Arial", 14, "normal"), bg="#001f3f", fg="white")
status_label.pack(pady=10)

canvas = tk.Canvas(root, width=350, height=350, bg="#f8f8f8", highlightthickness=2, highlightbackground="#cccccc")
canvas.pack(pady=10)

root.bind("<KeyPress-1>", novo_jogo)

novo_jogo()
root.mainloop()
