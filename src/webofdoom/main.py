import click

@click.group(invoke_without_command=True)
@click.option("-t", default="http://localhost:3000/", help="Target url or IP address Ex: (http://localhost:3000/)")
@click.option("-w", type=click.Path(exists=True), help="Wordlist to use for endpoint busting.")
def cli(t: str, w: str):
    # Print logo.
    click.echo(click.style("""
         _______
        |.-----.|
        ||x . x||
        ||_.-._||
        `--)-(--`
       __[=== o]___
      |:::::::::::|\\
      `-=========-`()
""", fg="red"))

    click.echo(click.style(f'{" " * 8 + "WebOfDoom" + " " * 4}', fg="green"))
    click.echo(click.style("Made with <3 by Kleo Hasani", fg="blue"))

    print("\n")

    # Print target and attack info.
    click.echo(f'{click.style("  Attack", fg="red")} -> {click.style(t, fg="yellow")}')
    click.echo(f'{click.style("Wordlist", fg="red")} -> {click.style(w, fg="yellow")}')
    click.echo(f'{click.style("  Method", fg="red")} -> {click.style("GET", fg="yellow")}')

    print("\n")

    # Send requests.

    pass