from invoke import task
from rich import print, inspect

@task
def hello(c, name):
    """Exibe uma saudação simples."""
    print(f"Hello {name}!")

@task
def build(c):
    """Simula a construção de um projeto."""
    print("Construindo o projeto...")

@task
def test(c):
    """Executa os testes do projeto."""
    c.run("echo 'pytest'") # 'c.run' executa comandos de shell

@task
def debug(c):
    """Inspeciona o objecto \"c\" de contexto."""
    inspect(c)
