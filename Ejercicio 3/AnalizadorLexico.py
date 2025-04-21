import re

#Reglas de tokens
token_specification = [
    ('Palabra_clave', r'\b(int|if|while|print|return)\b'),
    ('Identificador', r'\b[A-Za-z_][A-Za-z0-9_]*\b'),
    ('Literal_entero', r'\b\d+\b'),
    ('Literal_cadena', r'"[^"\n]*"'),
    ('Operador', r'[+\-*/=><]'),
    ('Separador', r'[(){};,]'),
    ('Espacio', r'[ \t]+'),       
    ('Nueva_linea', r'\n'),       
    ('Desconocido', r'.'),        
]

#Diccionario 
nombres_legibles = {
    'Palabra_clave': 'Palabra clave',
    'Literal_entero': 'Literal (entero)',
    'Literal_cadena': 'Literal (cadena)',
    'Nueva_linea': 'Nueva línea'
}

#Compilar todas las expresiones en una sola
tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
get_token = re.compile(tok_regex).match

def analizar_codigo(codigo):
    tokens = []
    lineas = codigo.split('\n')

    for num_linea, linea in enumerate(lineas, start=1):
        pos = 0
        while pos < len(linea):
            match = get_token(linea, pos)
            if not match:
                break
            tipo = match.lastgroup
            if tipo != 'Espacio':
                valor = match.group(tipo)
                columna = pos + 1
                tipo_legible = nombres_legibles.get(tipo, tipo)
                tokens.append((valor, tipo_legible, num_linea, columna))
            pos = match.end()
    
    return tokens

#Codigo de prueba
codigo = '''int suma = 10 + 5;
if (suma > 10) {
    print("El resultado es mayor que 10");
}'''

resultado = analizar_codigo(codigo) #Ejecutar y mostrar resultado

print(f"{'Token':<30}{'Tipo':<20}{'Línea':<10}{'Columna'}")
for token in resultado:
    print(f"{token[0]:<30}{token[1]:<20}{token[2]:<10}{token[3]}")
