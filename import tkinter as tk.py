import tkinter as tk
import cv2  # Biblioteca para processamento de imagem (instale com pip install opencv-python)

# Função para ser executada quando o botão "Clique Aqui" for clicado
def clique_aqui():
    # Exibir uma mensagem na caixa de texto
    caixa_texto.insert(0, "Você clicou no botão!")

# Função para iniciar o reconhecimento facial
def iniciar_reconhecimento():
    # Obter o nome do usuário digitado
    nome_usuario = nome_usuario_entry.get()

    # Iniciar captura de vídeo da webcam
    captura = cv2.VideoCapture(0)  # 0 indica a webcam principal

    while True:
        # Capturar o quadro atual da webcam
        ret, frame = captura.read()

        # Processar o quadro para reconhecimento facial (implementação não detalhada aqui)
        # ... (utilizar bibliotecas como OpenCV ou dlib para detecção e reconhecimento de faces)

        # Exibir o quadro processado na área de vídeo
        video_area.config(image=frame)

        # Atualizar a tela
        janela.update()

        # Verificar se a tecla 'q' foi pressionada para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar a captura da webcam
    captura.release()

# Criar a interface gráfica principal
janela = tk.Tk()
janela.title("Janela Aprimorada")

# Criar elementos da interface:

# Rótulo para título
titulo = tk.Label(janela, text="Reconhecimento Facial", font=("Arial", 18))
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Caixa de entrada para nome
nome_usuario_entry = tk.Entry(janela)
nome_usuario_entry.grid(row=1, column=0, padx=10, pady=5)

# Botão "Iniciar Reconhecimento"
botao_iniciar = tk.Button(janela, text="Iniciar Reconhecimento", command=iniciar_reconhecimento)
botao_iniciar.grid(row=1, column=1, padx=10, pady=5)

# Área para exibir o vídeo da webcam
video_area = tk.Label(janela, width=320, height=240)
video_area.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Área para exibir o resultado do reconhecimento (ainda não implementada)
resultado_area = tk.Label(janela, text="Resultado:", font=("Arial", 12))
resultado_area.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Criar elementos da primeira janela (opcional)
janela_simples = tk.Tk()
janela_simples.title("Janela")

botao_clique_aqui = tk.Button(janela_simples, text="Clique Aqui", command=clique_aqui)
botao_clique_aqui.pack()

caixa_texto = tk.Entry(janela_simples)
caixa_texto.pack()

# Manter as janelas abertas
janela.mainloop()
janela_simples.mainloop()

#Explicação das Mudanças: Funções: clique_aqui: Exibe uma mensagem na caixa de texto da primeira janela quando o botão "Clique Aqui" é clicado.
#iniciar o reconhecimento:
 # Obtém o nome do usuário digitado na caixa de entrada.
# Inicia a captura de vídeo da webcam.
# Processa cada quadro para reconhecimento facial (implementação não detalhada, mas com instruções para usar bibliotecas como OpenCV ou dlib).
# Exibe o quadro processado na área de vídeo.
# Permite que o usuário pressione 'q' para sair.Libera a captura da webcam ao final.
# Adicionado título para a segunda janela.Ajustado o layout das interfaces para melhor organização.