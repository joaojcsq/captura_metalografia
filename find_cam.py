import cv2

def verificar_cameras(max_testes=5):
    """
    Verifica quantas câmeras estão disponíveis no sistema.
    
    Parâmetros:
    max_testes (int): Número máximo de câmeras a serem testadas
    
    Retorna:
    list: Lista com os índices das câmeras disponíveis
    """
    cameras_disponiveis = []
    
    for i in range(max_testes):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            cameras_disponiveis.append(i)
            cap.release()
        else:
            cap.release()
    
    return cameras_disponiveis

if __name__ == "__main__":
    print("Verificando câmeras disponíveis...")
    cams = verificar_cameras()
    
    if not cams:
        print("Nenhuma câmera encontrada!")
    else:
        print(f"Câmeras disponíveis: {cams}")
        
        # Mostrar informações detalhadas sobre cada câmera
        for cam_idx in cams:
            cap = cv2.VideoCapture(cam_idx)
            print(f"\nInformações da câmera {cam_idx}:")
            
            # Tenta obter algumas propriedades
            try:
                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                fps = cap.get(cv2.CAP_PROP_FPS)
                print(f"Resolução: {width}x{height}")
                print(f"FPS estimado: {fps:.2f}")
                
                # Testa se consegue capturar um frame
                ret, frame = cap.read()
                if ret:
                    print("Status: Funcionando corretamente")
                    # Mostra uma pré-visualização rápida
                    cv2.imshow(f'Camera {cam_idx} - Preview', frame)
                    cv2.waitKey(1000)  # Mostra por 1 segundo
                    cv2.destroyAllWindows()
                else:
                    print("Status: Detectada mas não consegue capturar frames")
            except:
                print("Status: Detectada mas com problemas de acesso")
            
            cap.release()