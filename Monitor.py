
def monitor_simples():
    
    # Definição do limite de temperatura
    limite = 80
    
    print("Monitor de Servidor Ativo (Pressione Ctrl+C para encerrar)")
    
    while True:
        try:
            # Recebe o valor do sensor de temperatura
            leitura = input("Informe a temperatura atual: ")
            
            # Converte para número para poder comparar
            temperatura = float(leitura)
            
            # Lógica de decisão
            if temperatura > limite:
                print(f"Alerta: {temperatura}ºC! -> Resfriamento ativado")
            else:
                print("Status: Sistema operando em temperatura segura.")
                
        except ValueError: # Captura erros caso o usuário digite algo que não seja um número
            print("Entrada inválida. Digite apenas números.")
            
        except KeyboardInterrupt: # Permite que o usuário encerre o monitoramento com Ctrl+C
            print("\nMonitoramento encerrado pelo usuário.")
            break

# Execução
monitor_simples()