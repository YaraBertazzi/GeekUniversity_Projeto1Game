from models.calcular import Calcular


def main() -> None:
  pontos: int = 0
  jogar(pontos)

def jogar(pontos: int) -> None:
  dificuldade: int = int(input('\033[1;42mInforme o nível de  dificuldade desejada [1, 2, 3, ou 4]: \033[m'))
  calc: Calcular = Calcular(dificuldade)

  print('Informe o resultado para a seguinte operação: ')
  calc.mostrar_operacao() # 5 + 4 = ?

  resultado: int = int(input())

  if calc.checar_resultado(resultado):
    pontos += 1
    print(f'\033[0;35mVocê tem {pontos} ponto(s).\033[m')

  continuar: int = int(input('\033[mDeseja continuar no jogo? [1 - sim, 0- não]: \033[m'))

  if continuar:
    jogar(pontos)

  else:
    print(f'\033[1;35mVocê finalizou com {pontos} ponto(s).\033m')
    print('Até a proxima...')




if __name__=='__main__':
  main()
