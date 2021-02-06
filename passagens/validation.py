def origem_destino_iguais(origem, destino, lista_de_erros):
    '''
    Verifica se origem e destino são igais
    :param origem: str
    :param destino: str
    :param lista_de_erros: []
    '''
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais.'


def tem_caracter_numerico(valor_campo, nome_campo, lista_de_erros):
    '''
    Verifica se há caracteres numéricos no campo informado.
    :param valor_campo: str
    :param nome_campo: str
    :param lista_de_erros: []
    '''
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números.'


def data_ida_maior_que_a_data_volta(data_ida, data_volta, lista_de_erros):
    '''
    Verifica se data de ida é maior que a data de volta
    :param data_ida: date.
    :param data_volta: date.
    :param lista_de_erros: []
    :return:
    '''

    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de ida não pode ser maior que a data de volta.'