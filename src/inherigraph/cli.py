"""Console script for inherigraph."""
from __future__ import annotations

import typer
from rich.console import Console

console = Console()


def main(name: str):
    """Console script for inherigraph."""
    console.print(f"Hello [green]{name}[/green]")
    return 0


def entrypoint():
    """Entry point function that wraps `typer` entrypoint"""
    return typer.run(main)


if __name__ == "__main__":
    entrypoint()
