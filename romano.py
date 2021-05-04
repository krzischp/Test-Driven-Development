class Romano:
    ###############################################################################
    # Especificação Romano
    # ---------------------------
    #
    # Dado um numeral romano, 
    # o programa deve convertê-lo para o número inteiro correspondente. 
    # 
    #
    # - Regra 1: Um numero romano válido deve ser representado por sete diferentes simbolos, listados na tabela a seguir.
    # I, unus, 1, (um)
    #
    # V, quinque, 5 (cinco)
    #
    # X, decem, 10 (dez)
    #
    # L, quinquaginta, 50 (cinquenta)
    #
    # C, centum, 100 (cem)
    #
    # D, quingenti, 500 (quinhentos)
    #
    # M, mille, 1.000 (mil)
    #
    # - Regra 2: Algarismos de menor ou igual valor à direita são somados ao algarismo de maior valor;
    # - Regra 3: Algarismos de menor valor à esquerda são subtraídos do algarismo de maior valor.
    # - Regra 4: Além disso nenhum símbolo pode ser repetido lado a lado por mais de 3 vezes
    #
    ###############################################################################

    @staticmethod
    def convert_romano(c):
        if not is_romano(c):
            return None
        curr = c[-1]
        prev = curr
        res = map_romanos[curr]
        if len(c) == 1:
            return res
        length = len(c)
        k = length - 2
        while k >= 0:
            prev = curr
            curr = c[k]
            if map_romanos[curr] >= map_romanos[prev]:
                res += map_romanos[curr]
            else:
                res = res - map_romanos[curr]
            k -= 1
        return res
    

map_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def is_romano_rule_1(c):
    ###############################################################################
    # Especificação is_romano_rule_1
    # ---------------------------
    #
    # Dado um numeral romano, 
    # o programa deve verificar que ele respeita as regras seguinte:
    # - Um numero romano válido deve ser representado por sete diferentes simbolos, listados na tabela a seguir.
    # I, unus, 1, (um)
    #
    # V, quinque, 5 (cinco)
    #
    # X, decem, 10 (dez)
    #
    # L, quinquaginta, 50 (cinquenta)
    #
    # C, centum, 100 (cem)
    #
    # D, quingenti, 500 (quinhentos)
    #
    # M, mille, 1.000 (mil)
    #
    ###############################################################################
    return isinstance(c, str) and all([v in map_romanos.keys() for v in c])


def is_romano_rule_2(c):
    ###############################################################################
    # Especificação is_romano_rule_2
    # ---------------------------
    # - Nenhum símbolo pode ser repetido lado a lado por mais de 3 vezes
    #
    ###############################################################################
    if len(c) == 1:
        return True
    else:
        curr = c[0]
        prev = curr
        acc = 0
        length = len(c)
        k = 1
        while k < length and acc < 3:
            prev = curr
            curr = c[k]
            if curr == prev:
                acc += 1
            else:
                acc = 0
            k += 1
        return acc < 3



def is_romano(c):
    ###############################################################################
    # Especificação is_romano
    # ---------------------------
    #
    # Dado um numeral romano, 
    # o programa deve verificar que ele respeita as regras seguinte:
    # - Um numero romano válido deve ser representado por sete diferentes simbolos, listados na tabela a seguir.
    # I, unus, 1, (um)
    #
    # V, quinque, 5 (cinco)
    #
    # X, decem, 10 (dez)
    #
    # L, quinquaginta, 50 (cinquenta)
    #
    # C, centum, 100 (cem)
    #
    # D, quingenti, 500 (quinhentos)
    #
    # M, mille, 1.000 (mil)
    #
    # - Além disso nenhum símbolo pode ser repetido lado a lado por mais de 3 vezes
    ###############################################################################
    return is_romano_rule_1(c) and is_romano_rule_2(c)