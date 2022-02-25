import typer
import wordlecli.wordle as wordle
from wordlecli.wordle import get_wordle_num

wordle_num = get_wordle_num()
app = typer.Typer(add_completion=False)

@app.command()
def word(num: str = typer.Argument(str(wordle_num), show_default=False),
         hard: bool = typer.Option(False, help="Play without an on-screen-keyboard")
):
    if not(hard):
        wordle.main(num, True)
    else:
        wordle.main(num, False)

def main():
    app()

if __name__ == "__main__":
    typer.run(word)
