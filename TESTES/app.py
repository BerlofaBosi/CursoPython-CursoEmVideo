treino_begginer = '''
*Dia 1: Treino de Costas, Pernas e Bíceps*
    1. Pulley frente aberto: 4x6
    3. Rosca alternada com haltere: 4x6
    4. Barra Graviton: 4x6
    5. Rosca direta com a barra: 4x8

*Dia 2: Treino de Ombros, Peito e Tríceps*
    1. Elevação Lateral com Haltere: 4x6
    2. Supino reto: 4x6
    3. Triceps corda: 4x8

*Dia 3: Treino de Pernas, Abdômen e Estabilização*
    1. Agachamento Sumô: 4x6
    2. Abaixamento no smith: 4x6
    3. Prancha: 4x30 segundos
'''
treino_intermediate = '''
*Dia 1: Treino de Costas e Bíceps*
	1.	Pull Down: 4x10
	2.	Pulley neutro com triângulo: 4x12
	3.	Supino na máquina: 4x12
	4.	Voador na máquina: 3x10
	5.	Rosca Scott: 4x12

*Dia 2: Treino de peito e triceps*
	1.	supino reto com Haltere: 4x12
	2.	Tríceps corda: 4x12
	3.	Peck deck: 4x12
	4.	barra paralela: 4x12

*Dia 3: Descanso*

*Dia 4: Treino de Perna e ombro*
	1.	Agachamento livre: 4x8-10
	2.	Leg press: 4x10-12
	3.	Extensora: 3x12-15
	4.	Elevação lateral com haltere: 3x12
	5.	Desenvolvimento com haltere: 3x12
'''
treino_advanced = '''
*Dia 1: Peito e Tríceps*
    1. Supino inclinado: 4x8-10
    2. Supino reto: 4x8-10
    3. Crucifixo na máquina: 3x12-15
    4. Pulley tríceps: 4x10-12
    5. Tríceps testa com barra: 3x10-12

*Dia 2: Costas e Bíceps*
    1. Barra fixa: 4x8-10
    2. Puxada frontal na máquina: 4x10-12
    3. Remada curvada: 3x10-12
    4. Rosca direta com barra: 3x10-12
    5. Rosca martelo: 3x12-15

*Dia 3: Pernas*
    1. Agachamento livre: 4x8-10
    2. Leg press: 4x10-12
    3. Extensora: 3x12-15
    4. Flexora: 3x10-12
    5. Panturrilha em pé: 4x15-20

*Dia 4: Ombros e Trapézio*
    1. Desenvolvimento com barra: 4x8-10
    2. Elevação lateral: 3x12-15
    3. Elevação frontal com halteres: 3x10-12
    4. Encolhimento de ombros: 4x10-12

*Dia 5: Cardio e Abdominais*
    - 30 minutos de cardio (corrida, ciclismo, ou elíptico)
    - Prancha: 4x1 minuto
    - Crunch: 3x15-20
    - Obliquo na polia alta: 3x12-15 cada lado

*Dia 6: Treino Funcional*
    - Realize exercícios que envolvam movimentos complexos, como agachamentos com bola medicinal, burpees, e prancha com rotação.
'''

cont_perfil = 0
    
print('-'*20)

while True:
    print(''' NUTRIFITPRO
          
    [0] Seu perfil
    [1] Seus metas diários
    [2] Consumo calórico
    [3] Treino
    [4] Sair
    ''')
    print('-'*20)
    user = int(input('Sua escolha>>> '))
    print()
    match user:
        case 0:
            if cont_perfil == 0:
                name = str(input('Insira seu nome: ').strip().title())
                age = int(input('Insira sua idade: '))
                gender = str(input('Insira o seu sexo:[M/F] ').strip().upper())
                altura = int(input('Insira a sua altura [cm]: '))
                peso = float(input('Insira o seu peso [Kg]: '))
                print('''Qual o seu meta?
[1] Perder 1.0 Kg por semana
[2] Perder 0.5 Kg por semana
[3] Manter o peso
[4] Ganhar 0.5 Kg por semana
[5] Ganhar 1.0 Kg por semana
''')
                meta = int(input('Sua escolha>>> '))
                match meta:
                    case 1:
                        meta = -1000
                    case 2:
                        meta = -500
                    case 3:
                        meta = 0.0
                    case 4:
                        meta = +500
                    case 5:
                        meta = +1000

                print('''Em uma escala de 1 a 5, qual é o seu nível de atividade fisica?
      
[1] Sedentários (pouco ou nenhum exercício)
[2] Levemente ativo (exercício leve 1 a 3 dias por semana)
[3] Moderadamente ativo (exercício moderado, faz esportes 3 a 5 dias por semana)
[4] Altamente ativo (exercício pesado de 5 a 6 dias por semana)
[5] Extremamente ativo (exercício pesado diariamente e até 2 vezes por dia)
''')
                gymlvl = int(input('Sua escolha>>> '))
                match gymlvl:
                    case 1:
                        gymlvl = 1.2
                    case 2:
                        gymlvl = 1.375
                    case 3:
                        gymlvl = 1.55
                    case 4:
                        gymlvl = 1.725
                    case 5:
                        gymlvl = 1.9

                cont_perfil += 1

                if gender in 'Mm':
                    caloria = gymlvl * (66 + ((13.7 * peso) + (5 * altura) - (6.8 * age))) + meta
                elif gender in 'Ff':
                    caloria = gymlvl * (655 + ((9.6 * peso) + (1.8 * altura) - (4.7 * age))) + meta
            else:
                print(f'''Nome: {name}
Idade: {age} anos
Sexo: {gender}
Altura: {altura} cm
Peso: {peso} Kg
Meta: {meta} Kcal por semana
Nível de atividade Física: {gymlvl}''')
        case 1:
            if cont_perfil != 0:
                print(f'Seu meta diario de caloria a se consumir é de: {caloria:.2f}')
            else:
                print('Ainda não foi realizado o cadastro do perfil.')
        case 3:
            print('Sugestão de treino de acordo com o seu nível: ')
            if gymlvl < 1.50:
                print(treino_begginer)
            elif gymlvl < 1.8:
                print(treino_intermediate)
            elif gymlvl < 2.0:
                print(treino_advanced)

        case 4:
            print('Aplicativo encerrado.')
            break

    print('-'*20)
