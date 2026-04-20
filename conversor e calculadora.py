"""
print("Calculadora e Conversor\n")#\n quebra linha
print("="*45)# coloca enfeite
num1 = int(input("Informe um numero: "))#frase = "Isso é uma 'aspas' simples dentro de duplas"
num2 = int(input('Informe outro numero: '))
Resultado = num1 * num2
print("Resultado: ",Resultado)
"""
print("="*45)
print("Calculadora e Conversor".center(45))# outra forma de alinhar ao centro
#print(f"{'Teste':^45}")# Alinhamento ao centro, mesmo resultado do .center()
print("="*45)

while True:
    try:# tente
        # Menu de Opções
        print("1: para somar")
        print("2: para subtrair")
        print("3: para multiplicar")
        print("4: Dividir")
        print("5: Conversor")
        print("0 Sair" )
        print("="*45)
        print("="*45)

        opcao = input("Informe uma opcao: \n").strip()# O .strip() remove espaços vazios
                                              # antes e depois do que foi escrito

        match opcao:
            case "1":
                num1 = float(input("Informe um numero: ").strip().replace(",", "."))# pede digitar pelo teclado
                num2 = float(input("Informe outro numero: ").strip().replace(",","."))#pede para digitar pelo teclado
                Resultado = num1 + num2
                print("Resultado: ",Resultado)
                input("Pressione ENTER para voltar ao menu")
                print("="*45)
            case "2":
                num1 = float(input("Informe um numero: ").strip().replace(",","."))#pede para digitar pelo teclado
                num2 = float(input("Informe outro numero: ").strip().replace(",","."))#pede para digitar pelo teclado
                Resultado = num1 - num2
                print("Resultado: ",Resultado)
                input("Pressione ENTER para voltar ao menu")
                print("=" * 45)
            case "3":
                num1 = float(input("Informe um numero: ").strip().replace(",","."))
                num2 = float(input("Informe outro numero: ").strip().replace(",","."))
                Resultado = num1 * num2
                print("Resultado: ",Resultado)
                input("Pressione ENTER para voltar ao menu")
                print("=" * 45)
            case "4":
                num1 = float(input("Informe um numero: ").strip().replace(",","."))
                num2 = float(input("Informe outro numero: ").strip().replace(",","."))
                if num2 == 0:

                    print("Erro: operação não é possível dividir por 0")
                else:
                    Resultado = num1 / num2
                    print(f"Resultado: {Resultado:.1f}")
                    input("Pressione ENTER para voltar ao menu")
                    print("=" * 45)
            case "5":
                print("=" * 45)
                print(f"{'Conversor de Medidas':^45}")
                print("="*45)
                print("1:Converter para Centimetros")
                print("-"*45)
                print("2:Converter para Milimetros")
                print("-"*45)
                print("3:Converter para Kilometros")
                print("-"*45)
                print("4:Converter para Milhas")
                print("-"*45)
                opcaoC = input("Escolha o tipo de conversão:")
                print("=" * 45)
                if opcaoC == "1":
                    print("Conversão para Centimetros")
                    print("=" * 45)
                    ValorEmMetros = float(input("Informe o valor em metros: ").strip().replace(",","."))
                    print("-"*45)
                    print("Valor em Metros informado: ",ValorEmMetros)
                    ConverterCentimetros = (ValorEmMetros * 100)
                    print(f"Valor em Centimetros: {ConverterCentimetros:.3f}")
                    print("="*45)
                elif opcaoC == "2":
                    print("Conversão para Milimetros")
                    ValorEmMetros = float(input("Informe o valor em metros: ").strip().replace(",","."))
                    print("-"*45)
                    print("Valor em Metros informado: ",ValorEmMetros)
                    ConverterMilimetros = (ValorEmMetros * 1000)
                    print(f"Valor em Milimetros: {ConverterMilimetros:.3f}")
                    print("=" * 45)
                elif opcaoC == "3":
                    print("Conversão para Kilometros")
                    ValorEmMetros = float(input("Informe o valor em metros: ").strip().replace(",","."))
                    print("-"*45)
                    print("Valor em Metros informado: ", ValorEmMetros)
                    ConverterParaKilometros = (ValorEmMetros / 1000)
                    print(f"Resultado em KM: {ConverterParaKilometros:.3f}")
                    print("=" * 45)
                elif opcaoC == "4":
                    print("Conversão para Milhas")
                    print("-" * 45)
                    ValorEmKilometros = float(input("Informe o valor em kilometros: ").strip().replace(",","."))
                    print("="*45)
                    print("Valor em Kilometros: ",ValorEmKilometros)
                    print("=" * 45)
                    ValorEmMilhas = (ValorEmKilometros * 0.621371)
                    print("Distância em Milhas: ", ValorEmMilhas)
                    print("=" * 45)
                else:
                    print("Apenas as opções Listadas")
            case "0":
                print("Operação encerrada")
                break
            case _:
                print("Opção Invalida, Apenas opções listadas")
                print("=" * 45)
                input("Pressione ENTER Para voltar ao menu")
    except ValueError as e:
        print(e,"Apenas números são aceitos nas operações")
        input("Pressione ENTER para voltar ao menu")
    except ZeroDivisionError:
        print("Não é possível Dividir um Valor por Zero")
        input("Pressione ENTER para voltar ao menu")
    except Exception as erro:
        print("Acontceu um erro inesperado",erro)
        input("Pressione ENTER para voltar ao menu")



