import typer

app = typer.Typer()

@app.command()
def greet(name: str):
    print(f"Hey {name}, welcome to Python 3.14!")

@app.command()
def farewell(name: str):
    print(f"Goodbye {name}, see you soon!")

if __name__ == "__main__":
    app()
