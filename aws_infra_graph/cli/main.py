import typer

app = typer.Typer()

@app.command()
def version():
    """Show version."""
    typer.echo("aws-infra-graph v0.1.0")

if __name__ == "__main__":
    app()
