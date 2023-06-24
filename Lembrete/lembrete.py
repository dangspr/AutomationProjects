import pyautogui
import time
from datetime import datetime
import pygame


# Laço de repetição para validar horário de iniciar o alerta
while True:
    
    data_e_hora_atuais = datetime.today()
    if data_e_hora_atuais.hour == 1 and data_e_hora_atuais.minute == 6 or data_e_hora_atuais.hour == 8 and data_e_hora_atuais.minute == 21:
        time.sleep(10)
        print("Agora vou continuar o programa, já são",
              data_e_hora_atuais.hour, ":", data_e_hora_atuais.minute)
    else:
        print("Não está na hora...", "...ainda são", data_e_hora_atuais.hour,
              ":", data_e_hora_atuais.minute, ":", data_e_hora_atuais.second)
        time.sleep(20)
        continue
    pygame.init()
    pygame.mixer.music.load('c:/Projetos/Concluidos/Automation/Lembrete/sound.mp3')
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.event.wait()
    pyautogui.alert('Está na hora!!!')  
    
    break
