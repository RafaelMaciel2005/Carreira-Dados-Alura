def resumo_vendas(vendas_smartphones, vendas_smartwatch):

    total_vendas = vendas_smartphones + vendas_smartwatch
    print("O total de vendas foi {}.".format(total_vendas))
    if vendas_smartwatch > vendas_smartphones:
       print("O produto mais vendido foi o SmartWatch.")     
    else:
      print("O produto mais vendido foi o smartphone.")

smartphones = int(input("Insira o total de vendas do smartphones"))

smartwatch = int(input("Insira o total de vendas do smartwatch"))

vendas = resumo_vendas(smartphones, smartwatch)
