# Projeto Técnico de futebol
O projeto tem como objetivo ao final de sua execusão imprimir uma formação de um time de futebol com os jogadores escolhidos pelo usuario.

## Entrada:
(Ao digitar uma entrada invalida, o usuario deve digitar a opção novamente)

A entrada consiste em opções de 1 ao 5, sendo o numero 5 o criterio de parada.

**Nº 1**: Caso o usuario digite o numero 1, ele escolheu a opção "Contratar jogador", após isso ele deve digitar a na seguinte sequência:

      nome_do_jogador posição habilidade
       
OBS: devem se atentar para entrada correta onde as posições validas são apenas: **goleiro, zagueiro, meia e atacante**. Qualquer posição diferente dessas citadas não seram validas, e quanto a habilidade do jogador, deve ser de um numero inteiro que varia de **0 a 10**, não podendo ultrapassar esse valor.

Exemplo de entrada valida: (Letra minuscula) 

      neymar meia 10

**Nº 2**: Ao digitar o numero 2, o usuario seleciona a opção trocar jogador, e para tracar o jogador ele deve digitar na seguinte seguencia:

      nome_do_jogador posição habilidade x nome_do_jogador_novo posição habilidade

Exemplo de entrada valida: (Letra minscula)

      neymar meia 10 x coutinho meia 10

Neste exemplo estamos trocando o jogador Neymar pelo jogador Coutinho.

**Nº 3**: Essa opção serve para estabelecer um esquema tatico, a entrada consiste em 3 numeros inteiros onde a soma dos numeros deve ser igual a 10.

Exemplo de entrada valida:

      4 4 2

**Nº 4**: Na opção 4 (Montar time), caso o usuario não tenha estabelecido o esquema tático primeiro uma mensagem de advertencia será impressa. Se usuario tiver "contratado" todos os jogadores necessarios para formar o time, será impresso uma visulização da escalação, caso contrário será impresso as posições necessarias e sua quantidade para completar o time.

**Nº 5**: Esta opção finaliza o codigo.
