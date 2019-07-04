# -*- coding: utf-8 -*-

# "Cheque por Extenso" -> http://dojopuzzles.com/problemas/exibe/cheque-por-extenso/

unidades = {
    0: 'zero',
    1: 'um',
    2: 'dois',
    3: 'três',
    4: 'quatro',
    5: 'cinco',
    6: 'seis',
    7: 'sete',
    8: 'oito',
    9: 'nove',
}

excecoes = {
    11: 'onze',
    12: 'doze',
    13: 'treze',
    14: 'catorze',
    15: 'quinze',
    16: 'dezesseis',
    17: 'dezessete',
    18: 'dezoito',
    19: 'dezenove',
}

dezenas = {
    10: 'dez',
    20: 'vinte',
    30: 'trinta',
    40: 'quarenta',
    50: 'cinquenta',
    60: 'sessenta',
    70: 'setenta',
    80: 'oitenta',
    90: 'noventa',
}

def escreve_por_extenso(numero):

    if numero == 1:
        return 'um real'

    if numero in range(0, 10):
        return unidades[numero] + ' reais'

    if numero in range(11, 20):
        return excecoes[numero] + ' reais'

    if numero % 10 == 0 and numero < 100:
        return dezenas[numero] + ' reais'
        
    dezena = (numero / 10) * 10
    unidade = numero % dezena

    if numero in range(21,100):
        return dezenas[dezena] + ' e ' + unidades[unidade] + ' reais'
    
    return 'numero ainda não suportado'


def test_escreve_por_extenso_numeros_simples():
    assert(escreve_por_extenso(0) == 'zero reais')
    assert(escreve_por_extenso(1) == 'um real')
    assert(escreve_por_extenso(3) == 'três reais')
    assert(escreve_por_extenso(8) == 'oito reais')

def test_escreve_por_extenso_numeros_excecao():
    assert(escreve_por_extenso(13) == 'treze reais')
    assert(escreve_por_extenso(15) == 'quinze reais')
    assert(escreve_por_extenso(19) == 'dezenove reais')


def test_escreve_por_extenso_numeros_com_2_digitos():
    casos = [
        (10, 'dez reais'),
        (11, 'onze reais'),
        (19, 'dezenove reais'),
        (20, 'vinte reais'),
        (21, 'vinte e um reais'),
        (22, 'vinte e dois reais'),
        (23, 'vinte e três reais'),
        (24, 'vinte e quatro reais'),
        (29, 'vinte e nove reais'),
        (30, 'trinta reais'),
        (31, 'trinta e um reais'),
        (39, 'trinta e nove reais'),
        (40, 'quarenta reais'),
        (41, 'quarenta e um reais'),
        (49, 'quarenta e nove reais'),
        (57, 'cinquenta e sete reais'),
        (72, 'setenta e dois reais'),
        (89, 'oitenta e nove reais'),
        (96, 'noventa e seis reais'),
    ]

    for n, expected in casos:
        result = escreve_por_extenso(n) == expected
        if not result:
            print 'ERRO:', n

test_escreve_por_extenso_numeros_simples()
test_escreve_por_extenso_numeros_excecao()
test_escreve_por_extenso_numeros_com_2_digitos()
