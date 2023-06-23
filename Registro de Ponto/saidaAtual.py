import pyautogui
import time
from datetime import datetime
from pynput import mouse


# Laço de repetição para validar horário de iniciar a automação
while True:
    data_e_hora_atuais = datetime.today()
    if data_e_hora_atuais.hour >= 17 and data_e_hora_atuais.minute >= 23:
        data_e_hora_atuais = datetime.today()
        time.sleep(10)
    if data_e_hora_atuais.hour == 17 and data_e_hora_atuais.minute == 24:
        time.sleep(10)
        print("Agora vou continuar o programa, já são",
              data_e_hora_atuais.hour, ":", data_e_hora_atuais.minute)
    else:
        today = datetime.today()
        print("Não está na hora...", "...ainda são", data_e_hora_atuais.hour,
              ":", data_e_hora_atuais.minute, ":", data_e_hora_atuais.second)
        time.sleep(20)
        continue

# Abrir
    time.sleep(3)
    pyautogui.click(1072, 1049, duration=10)
    pyautogui.FAILSAFE = True

# Logar
    time.sleep(3)
    pyautogui.click(951, 411, duration=10)
    pyautogui.FAILSAFE = True


# Callback para confirmar os eventos de click


    def on_click(x, y, button, pressed):
        data_e_hora_atuais = datetime.today()
        if button == mouse.Button.left and pressed:
            # Retornar False para a execução do listener de eventos
            print('Seu ponto foi registrado com sucesso',
                  'em', data_e_hora_atuais.hour, ":", data_e_hora_atuais.minute, ":", data_e_hora_atuais.second)
            return False


# Mudar de Janela
# pyautogui.keyDown("alt")
# pyautogui.press(["tab"])
# pyautogui.keyUp("alt")

# Bater Ponto Verdadeiro
    time.sleep(3)
    pyautogui.click(1035, 403, duration=10)
    pyautogui.FAILSAFE = True


# Listener para verificar quando o mouse clicará
    with mouse.Listener(on_click=on_click) as listener:
        while True:
            now = datetime.today()
            # Assim que clicado, o listener irá encerrar e parar o loop
            if not listener.running:
                break

            pyautogui.click(1798, 14, duration=1)

        pyautogui.alert('Seu ponto foi registrado com sucesso')
    break

# Escrever pyautogui.write('')
