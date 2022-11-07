larg =  float(input('Digite a largura da sua parede:\n>>>'));
alt =  float(input('Digite a altura da sua parede:\n>>>'));
area = larg*alt;
tintaNecessaria = area/2;

print(f'Sua parede tem {larg}x{alt}, e sua área é de {area}m².\n Para pintar a parede, será necessário {tintaNecessaria}l de tinta.')
