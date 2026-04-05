

def gridgen(gridSizeX,gridSizeY):
    grid=[]
    for i in range(gridSizeY):
        grid.append([])
        for j in range(gridSizeX):
            grid[i].append("[]")
    return grid


gridsizeX=10
gridsizeY=5
grid= gridgen(gridsizeX,gridsizeY)


posx= int(input("X: "))
posy= int(input("Y: "))

grid[posy][posx]="[x]"
opt = ""
while True: 
    for line in grid:print(line)
    opt=input("w cima a baixo s esquerda d direita")
    match opt:
        case "w":
            if posy>0: 
                grid[posy][posx]="[]"
                posy-=1
                grid[posy][posx]="[x]"
            else:
                print("MOVEERROR")
    
        case "s":
            if posy<gridsizeY-1: 
                grid[posy][posx]="[]"
                posy+=1
                grid[posy][posx]="[x]"
            else:
                print("MOVEERROR")
        case "a":
            if posx>0: 
                grid[posy][posx]="[]"
                posx-=1
                grid[posy][posx]="[x]"
            else:
                print("MOVEERROR")
    
        case "d":
            print(posx)
            if posx<gridsizeX-1: 
                grid[posy][posx]="[]"
                posx+=1
                grid[posy][posx]="[x]"
            else:
                print("MOVEERROR")
        case "n":
            print("bye bye!")
            break