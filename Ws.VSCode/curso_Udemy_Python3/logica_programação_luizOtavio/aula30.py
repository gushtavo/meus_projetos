# COSTANTE = 'variaveis' que não vão mudar
# Muitas condições no mesmo if (ruim)
#   <- contagem de complexidade(ruim)


velocidade = 70  # velocidade atual do carro
local_atual = 100  # local em que o carro esta na estrada

RADAR_1 = 60  # velocidade maxima do radar 1
LOCAL_1 = 100  # Local onde o radar 1 está
RADAR_RANGE = 1  # Alcance do radar

vel_carro_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_atual >= (LOCAL_1 - RADAR_RANGE) and \
    local_atual <= (LOCAL_1 + RADAR_RANGE)
multa_radar_1 = carro_passou_radar_1 and vel_carro_radar_1

if velocidade > RADAR_1:
    print('velocidade do Carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if multa_radar_1:
    print('Carro multado em radar 1')
