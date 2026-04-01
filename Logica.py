def jogo():
    posicaoatual = 0
    while True:
        movimento = ["[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]"]
        ferramentas = {"quadrado": 4, "retangulo": 4, "triangulo": 4, "circulo": 4}

        v=0
        print("clique numa tecla:")
        botao=input()

        match botao:

            case "w":
                posicaoatual -= 3
                if posicaoatual < 0:
                    posicaoatual = -1
                movimento[posicaoatual]="[X]"
                movimento[posicaoatual+4]="[]"

                for i in range(4):
                    print(movimento[v:v + 4])
                    v += 4

            case "a":
                posicaoatual=posicaoatual-1
                if posicaoatual < 0:
                    posicaoatual = -1
                movimento[posicaoatual]="[X]"
                movimento[posicaoatual+1] = "[]"
                for i in range(4):
                    print(movimento[v:v + 4])
                    v += 4

            case "d":
                posicaoatual = posicaoatual + 1
                if posicaoatual>=len(movimento)-1:
                    movimento[posicaoatual - 1] = "[]"
                    posicaoatual=0
                    movimento[posicaoatual] = "[X]"
                movimento[posicaoatual]="[X]"
                movimento[posicaoatual+1] = "[]"
                for i in range(4):
                    print(movimento[v:v + 4])
                    v += 4
            case "s":
                posicaoatual = posicaoatual +4
                if posicaoatual>=len(movimento):
                    movimento[posicaoatual - 4] = "[]"
                    posicaoatual=0
                    movimento[posicaoatual] = "[X]"
                movimento[posicaoatual]="[X]"
                movimento[posicaoatual-4] = "[]"
                for i in range(4):
                    print(movimento[v:v + 4])
                    v += 4
            case "e":
                break

"""testes da logica  do  jogo
"""
print(jogo())