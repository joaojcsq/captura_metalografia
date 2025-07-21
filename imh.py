import cv2
import numpy as np

def capturar_regiao(frame, contador, x, y, w, h):
    """Captura e salva a região delimitada do frame"""
    regiao = frame[y:y+h, x:x+w]
    nome_arquivo = f"captura_{contador}.jpg"
    cv2.imwrite(nome_arquivo, regiao)
    print(f"Região capturada salva como {nome_arquivo}")
    return contador + 1

def main():
    # Inicializa a webcam
    cap = cv2.VideoCapture(2)
    
    if not cap.isOpened():
        print("Não foi possível abrir a webcam")
        return
    
    # Configurações da região de captura
    largura_janela = 640
    altura_janela = 480
    cv2.namedWindow("Webcam com Região de Captura", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Webcam com Região de Captura", largura_janela, altura_janela)
    
    # Parâmetros do retângulo vermelho (centralizado)
    rect_w, rect_h = 600, 400  # Largura e altura do retângulo
    rect_x = (largura_janela - rect_w) // 2
    rect_y = (altura_janela - rect_h) // 2
    
    contador = 1
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Não foi possível capturar o frame")
            break
        
        # Redimensiona o frame para o tamanho da janela
        frame = cv2.resize(frame, (largura_janela, altura_janela))
        
        # Desenha o retângulo vermelho (2px de espessura)
        cv2.rectangle(frame, (rect_x, rect_y), (rect_x + rect_w, rect_y + rect_h), 
                     (0, 0, 255), 2)
        
        # Adiciona texto informativo
        # cv2.putText(frame, "Pressione 'c' para capturar a area dentro do retangulo", 
        #            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        # cv2.putText(frame, "Pressione 'q' para sair", 
        #            (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        cv2.imshow("Webcam com Região de Captura", frame)
        
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('c'):
            contador = capturar_regiao(frame, contador, rect_x, rect_y, rect_w, rect_h)
            # Feedback visual
            frame[rect_y:rect_y+rect_h, rect_x:rect_x+rect_w] = \
                cv2.addWeighted(frame[rect_y:rect_y+rect_h, rect_x:rect_x+rect_w], 
                                0.5, np.zeros((rect_h, rect_w, 3), dtype=np.uint8), 
                                0.5, 0)
            cv2.imshow("Webcam com Região de Captura", frame)
            cv2.waitKey(300)
        
        if key == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()