#!/usr/bin/env python
import click
from mlib.mchange import change


@click.command()
@click.option(
    "--amount",
    prompt="Amount: ",
    help="Creates change for dollar and cents value:  i.e. 1.34",
)
def make_change(amount):
    """Gives Correct Change"""

    result = change(float(amount))
    click.echo(click.style(f"Change for {amount}:", fg="red"))
    for correct_change in result:
        for num, coin in correct_change.items():
            click.echo(click.style(f"{coin}: {num}", fg="green"))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    make_change()
