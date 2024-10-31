import random
import time
X_O = [['-']*3 for i in range(3)]
L_1 = [(0, 0), (0, 1), (0, 2)]
L_2 = [(1, 0), (1, 1), (1, 2)]
L_3 = [(2, 0), (2, 1), (2, 2)]
C_1 = [(0, 0), (1, 0), (2, 0)]
C_2 = [(0, 1), (1, 1), (2, 1)]
C_3 = [(0, 2), (1, 2), (2, 2)]
D_1 = [(0, 0), (1, 1), (2, 2)]
D_2 = [(0, 2), (1, 1), (2, 0)]
G_T = [L_1,L_2,L_3,C_1,C_2,C_3,D_1,D_2]
G_T_2 =[]
for L in G_T:
    G_T_2.append(L.copy())
P_M = [(0, 0), (0, 1), (0, 2),(1, 0), (1, 1), (1, 2),(2, 0), (2, 1), (2, 2)]
Crs = [(0, 0),(0, 2),(2, 0),(2, 2)]
times = [0.2,0.3,0.35,0.15,0.25]
end = 0
start = random.choice((1,2))
diag = random.choice((G_T_2[6],G_T_2[7]))



def AfficheMatrice(L):
    '''Permet d'afficher une matrice'''
    for i in range(len(L)):
        for j in range(len(L[i])) :
            if j != len(L[i])-1:
                print(L[i][j] ,end='  ')
            else:
                print(L[i][j])

def Dif_lists(L,M):
    '''Permet de produire un liste apartir de la difference de deux lists'''
    L,M = set(L),set(M)
    D = L.difference(M)
    D = list(D)
    return D
    

def Search_G_T(i,j):
    '''Permet de chercher les lignes, colonnes, diagonales de G_T
contenants (i,j)'''
    L = []
    k = 0
    while k <= 7:
        if (i,j) in G_T[k]:
            L.append(G_T[k])
        k += 1
    return L

def Search_G_T_2(i,j):
    '''Permet de chercher les lignes, colonnes, diagonales de G_T_2
contenants (i,j)'''
    L = []
    k = 0
    while k <= 7:
        if (i,j) in G_T_2[k]:
            L.append(G_T_2[k])
        k += 1
    return L
                             
def Is_Valide(i,j):
    '''Permet de verifier si la cellule n'est pas encore remplit'''
    if X_O[i][j] == '-':
        return True
    else:
        return False

def Test_Saisie(a,b):
    '''Permet de tester si les variables entrées par le joueur sont valides'''
    if not a.isnumeric() or not b.isnumeric():
        return False
    else:
        a,b = int(a) - 1, int(b) - 1
        if not a in [0,1,2] or not b in [0,1,2]:
            return False
        else:
            if not Is_Valide(a,b):
                return False
            else:
                return True

def C_move(i,j):
    '''Pemet de produire l'ensemble des modification qui accompagnent
le move d' ordinateur'''
    X_O[i][j] = 'O'
    P_M.remove((i,j))
    for L in Search_G_T_2(i,j):
        L.remove((i,j))
    if (i,j) in Crs:
        Crs.remove((i,j))
    

def Test_end():
    '''Permet de tester si le jeu a terminé ou non et determiner le gagnant'''
    global end
    for L in G_T:
        if len(L) == 0 :
            end = 1
            return None
    for L in G_T_2:
        if len(L) == 0 :
            end = 2
            return None
    if len(P_M)==0:
        end = -1
                
def Jouer(i,j):
    '''Pemet de produire l'ensemble des modification qui accompagnent
le move du joueur'''
    X_O[i][j] = 'X'
    P_M.remove((i,j))
    for L in Search_G_T(i,j):
        L.remove((i,j))
    if (i,j) in Crs:
        Crs.remove((i,j))
        
M_diag_1 = random.choices(Dif_lists(diag,[(1,1)]),k=1)
M_diag_2 = Dif_lists(diag,[(1,1)] + M_diag_1)

def C_jouer():
    '''Permet de determiner le move convenable'''
    global end
    
    if Is_Valide(1,1) and start == 1:
        C_move(1,1)

    elif start == 2 and len(P_M) == 9:
        L = M_diag_1[0]
        i = L[0]
        j = L[1]
        C_move(i,j)

    elif start == 2 and len(P_M) == 7 and Is_Valide(M_diag_2[0][0],M_diag_2[0][1]):
        L = M_diag_2[0]
        i = L[0]
        j = L[1]
        C_move(i,j)
             
    elif len(P_M)==0:
        return None
    
    else:
        for L in G_T_2:
            if len(L) == 1 :
                i = L[0][0]
                j = L[0][1]
                if Is_Valide(i,j):
                    C_move(i,j)
                    return None

        for L in G_T:
            if len(L) == 1 :
                i = L[0][0]
                j = L[0][1]
                if Is_Valide(i,j):
                    C_move(i,j)
                    return None

        if X_O[1][1] == 'O' and (len(D_1)==1 or len(D_2)==1):
            L = random.choice(Dif_lists(P_M,Crs))
            i = L[0]
            j = L[1]
            C_move(i,j)
            return None            
            
        while len(Crs)!=0:
            L = random.choice(Crs)
            i = L[0]
            j = L[1]
            C_move(i,j)
            return None
        else:
            L = random.choice(P_M)
            i = L[0]
            j = L[1]
            C_move(i,j)
            return None            
          

if start ==1:                                    #Le programme principale
    while end ==0:
        a = input('enter N ligne: ')
        b = input('enter N colonne: ')
        while not Test_Saisie(a,b) :
            print("Error")
            a = input('enter N ligne: ')
            b = input('enter N colonne: ')
        a,b = int(a)-1,int(b)-1
        Jouer(a,b)
        AfficheMatrice(X_O)
        print("-------")
        ti = random.choice(times)
        time.sleep(ti)
        C_jouer()
        AfficheMatrice(X_O)
        Test_end()
else:
    while end ==0:
        ti = random.choice(times)
        time.sleep(ti)
        C_jouer()
        AfficheMatrice(X_O)
        Test_end()
        if end != 0:
            continue
        a = input('enter N ligne: ')
        b = input('enter N colonne: ')
        while not Test_Saisie(a,b) :
            print("Error")
            a = input('enter N ligne: ')
            b = input('enter N colonne: ')
        a,b = int(a)-1,int(b)-1
        Jouer(a,b)
        AfficheMatrice(X_O)
        print("-------")
        Test_end()

if end == 1:
    print("You win")
    time.sleep(3)
elif end ==2:
    print("You lose")
    time.sleep(3)
else:
    print("We are even!")
    time.sleep(3)
