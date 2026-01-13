velocidade = 0

input_velocidade = int(input("Digite a velocidade do carro em km/h: "))
if input_velocidade > 80:
    velocidade = input_velocidade - 80
    multa = velocidade * 7
    print(f"Você foi multado! Sua multa é de R$ {multa:.2f}")
else:
    print("Tenha um bom dia! Dirija com segurança!")
