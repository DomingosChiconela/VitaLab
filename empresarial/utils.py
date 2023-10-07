from random import choice, shuffle
import string

def gerar_senha_aleatoria(tamanho):

    caracteres_especiais = string.punctuation   
    caracteres = string.ascii_letters
    numeros_list = string.digits

    
    sobra = 0
    qtd = tamanho // 3
    if not tamanho % 3 == 0:
        sobra = tamanho - qtd

    letras = ''
    for i in range(0, qtd + sobra):
        letras += choice(caracteres)

    numeros = ''
    for i in range(0, qtd):
        numeros += choice(numeros_list)

    especiais = ''
    for i in range(0, qtd):
        especiais += choice(caracteres_especiais)

    
    senha = list(letras + numeros + especiais)
    shuffle(senha)

    return ''.join(senha)


from django.conf import settings
from django.template.loader import render_to_string
from io import BytesIO
from weasyprint import HTML
import os


def gerar_pdf_exames(exame, paciente, senha):
#onde deve ser procurado o arquivo html
    path_template = os.path.join(settings.BASE_DIR, 'templates/partials/senha_exame.html')
    
    #apos achar , sendo renderizado
    template_render = render_to_string(path_template, {'exame': exame, 'paciente': paciente, 'senha': senha})
    
#instaciando a classe para bytesio para salvar em menoria(ram)
    path_output = BytesIO()
    
#escrevendo ou transformando o html em pdf e passando o caminho onde deve ser salvo
    HTML(string=template_render).write_pdf(path_output)
    
    #indicando o ponteiro ou o indice em que deve iniciar aleitura do ficheiro
    path_output.seek(0)
    
    return path_output