# O código proposto tem como objetivo calcular a idade em anos, meses e dias com base em uma quantidade de dias fornecida como entrada
# OBS: Será considerado nesse software que todos os meses possuem 30 dias, e todos os anos com 365 dias, desconsiderando os anos bissextos. 


def calcular_idade (entrada):
    
    # Calcula a quantidade de anos completos
    anos= entrada//365
    
    if anos>=1: 
        # Calcula a quantidade de meses completos
        meses= ( entrada - ( 365*anos ) ) // 30
        
        if meses<1:
            # Se não houver meses completos, calcula os dias restantes
            dias = entrada- (365*anos)
        else:
            # Se houver meses completos, calcula os dias restantes após subtrair os meses
            dias= (entrada-(365*anos)-(30*meses))
        
    else:
        
        # Se não houver anos completos, calcula a quantidade de meses completos
        meses= entrada//30 
        if meses<1 :
            # Se não houver meses completos, a quantidade de dias é igual à entrada
            dias= entrada
        else:
             # Se houver meses completos, calcula os dias restantes após subtrair os meses
            dias= entrada-(30*meses)
            
    print(f'{anos} anos, {meses} meses, {dias} dias')
    
    
    
entrada = input("Digite a quantidade de dias:")
entrada= int(entrada)

calcular_idade(entrada)

