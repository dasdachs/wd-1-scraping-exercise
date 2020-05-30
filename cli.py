import click

# from .src.main import execute_search


@click.command()
@click.argument('search')
def scrape(search: str) -> None:
    # results = execute_search(search)
    # Implement
    raise NotImplemented


if __name__ == '__main__':
    scrape()
