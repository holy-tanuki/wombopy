from typing import Optional

import typer

from wombopy import __app_name__, __version__
from wombopy.core import identify
from wombopy.core.generation import generate

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.command(help="Create an image from wombo.art")
def run(identify_key: str, prompt: str, style: int, open_result: Optional[bool] = typer.Option(
    None,
    "--open",
    "-o",
    help="Show back the image"
)):
    typer.secho(f"Prompt: {prompt}\tStyle: {style}")
    typer.secho("Starting...")

    res = identify(identify_key=identify_key)
    generate(res['id_token'], prompt, style, open_result)


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True,
        )
) -> None:
    return
