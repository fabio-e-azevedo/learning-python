import concurrent.futures
import time
import requests

def fetch(url):
    """
    Função que simula uma tarefa de I/O, baixando o conteúdo de uma URL.
    """
    print(f"Iniciando download de {url}")
    try:
        response = requests.get(url, timeout=5)
        print(f"Download de {url} concluído. Tamanho: {len(response.content)} bytes")
        return f"Download de {url} concluído com sucesso."
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar {url}: {e}")
        return f"Falha ao baixar {url}."

if __name__ == "__main__":
    urls = [
        "https://www.google.com",
        "https://www.python.org",
        "https://www.github.com",
        "https://www.wikipedia.org",
        "https://www.example.com"
    ]

    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as thread_executor:
        results = thread_executor.map(fetch, urls)

    # for url in urls:
    #     print(fetch(url))
        
    end_time = time.time()
    
    print("\n--- Resultados ---")
    for result in results:
        print(result)
    
    print(f"\nTempo total de execução: {end_time - start_time:.2f} segundos")
