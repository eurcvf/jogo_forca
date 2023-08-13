from palavraforca import palavras
import os

letras_usuario = []
chances = 4
ganhou = False

while True:
  # Criar lógica
  for letra in palavras:
    if letra.lower() in letras_usuario:
      print(letra, end=" ")
    else:
      print('_', end=" ")
      
  print(f"Você tem {chances} chances!")
  tentativa = input('Escolha uma letra para completar a palavra: ')
  letras_usuario.append(tentativa.lower())
  
  if tentativa.lower() not in palavras.lower():
    chances -= 1
    
  ganhou = True
  for letra in palavras:
    if letra.lower() not in letras_usuario:
      ganhou = False
  
  if chances == 0 or ganhou:
    break
     
if ganhou:
  print("")
  print(f'Você ganhou o jogo! A palavra era: {palavras}')
  os.
else:
  print("")
  print(f'Você perdeu! A palavra era: {palavras}')
