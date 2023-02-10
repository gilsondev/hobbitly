import typer

from sqlmodel import Session

from src.core.config import settings
from src.core.database import engine


main = typer.Typer(name="Hobbitly CLI", add_completion=True)


@main.command()
def shell():
    """Interactive shell"""
    instances = {
        "settings": settings,
        "engine": engine,
        "session": Session,
    }
    typer.echo(f"Auto imports: {list(instances.keys())}")

    try:
        from IPython import start_ipython
        start_ipython(argv=["--ipython-dir=/tmp"], user_ns=instances)
    except ImportError:
        import code

        code.InteractiveConsole(instances).interact()
