import typer
from typing import Optional

from aws_infra_graph.aws.session import AWSSession

app = typer.Typer()


@app.command()
def scan(
    profile: Optional[str] = typer.Option(
        None,
        "--profile",
        help="AWS profile name",
    ),
    region: Optional[str] = typer.Option(
        None,
        "--region",
        help="AWS region",
    ),
):
    """
    Scan AWS infrastructure.
    """
    session = AWSSession(profile=profile, region=region)

    sts = session.client("sts")
    identity = sts.get_caller_identity()

    typer.echo("Connected to AWS")
    typer.echo(f"Account: {identity['Account']}")
    typer.echo(f"UserArn: {identity['Arn']}")


@app.command()
def version():
    typer.echo("aws-infra-graph v0.1.0")


if __name__ == "__main__":
    app()
