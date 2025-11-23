# Mapeamento de Terreno com Flood Fill

Esse projeto é uma implementação do algoritmo **Flood Fill**. A ideia é mapear terrenos desconhecidos, identificando áreas livres e obstáculos.

Basicamente, a gente pega um grid onde tem espaços livres (0) e obstáculos (1). O código varre esse mapa e "pinta" as áreas conectadas com cores diferentes. Assim, o robô sabe exatamente onde pode andar e quais áreas estão separadas por barreiras.

## Como funciona o Flood Fill

O algoritmo é bem direto ao ponto:
1.  **Ponto de partida**: A gente dá uma coordenada inicial $(x, y)$ pra ele começar.
2.  **Espalhando a tinta**: Se o lugar for navegável (0), ele pinta com uma cor (tipo 2).
3.  **Vizinhos**: Daí ele olha pros vizinhos de cima, baixo, esquerda e direita. Se eles também forem navegáveis, ele vai pra lá e repete o processo com recursão.
4.  **Limites e Obstáculos**: Se bater num obstáculo (1) ou na borda do mapa, ele para e volta.
5.  **Mapeamento Total**: Depois de pintar a primeira região, o código continua varrendo o resto do mapa. Se achar outro pedaço de terra livre (0) que não foi pintado, ele começa tudo de novo com uma nova cor (3, 4, etc).

No final, cada região isolada fica com uma cor diferente.

## Como rodar

Pra testar o código, é só ter o Python instalado.

1.  Clone o repo ou baixe os arquivos.
2.  Abra o terminal na pasta do projeto.
3.  Rode o comando:

```bash
python main.py
```

O script já tem uns testes prontos no final do arquivo, então você vai ver o resultado direto no terminal.

