from MatrixTTT import * 

# Executa um jogo entre dois jogadores humanos 
p1 = JogadorHumano(0)
p2 = JogadorHumano(1)

jogo1 = MatrixTTT(p1, p2)
jogo1.jogar()

# Executa um jogo entre um jogador humano e uma máquina 
p3 = JogadorComputador(0)
p4 = JogadorHumano(1)

jogo2 = MatrixTTT(p3, p4)
jogo2.jogar()