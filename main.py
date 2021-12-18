#%%
# tu bedzie gra kolko i krzyzyk

PlanszaDoGry = {'7':' ','8':' ' ,'9':' ',
                '4':' ','5':' ','6':' ',
                '1':' ','2':' ','3':' '}
klawiszeGry=[]

for key in PlanszaDoGry:
    klawiszeGry.append(key)

def drukujPlansze(pole):
    print(f"{pole['7']}|{pole['8']}|{pole['9']}")
    print('-+-+-')
    print(f"{pole['4']}|{pole['5']}|{pole['6']}")
    print('-+-+-')
    print(f"{pole['1']}|{pole['2']}|{pole['3']}")
#drukujPlansze(PlanszaDoGry)

def gra():

    gracz='X'
    licznik=0

    for i in range(10):
        drukujPlansze(PlanszaDoGry)
        move=input(f'To jest ruch, {gracz}. Wybierz gdzie chcesz ustawić znak!')

        if PlanszaDoGry[move]==' ':
            PlanszaDoGry[move]=gracz
            licznik +=1
        else:
            print('Miejsce jest juz zajete!!!\nWstaw swój znak gdzieś indziej!')
            continue

        if licznik >=5:
            


    

# %%
