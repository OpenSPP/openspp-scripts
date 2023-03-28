import click
import click_odoo

RECOMPUTABLE_FIELDS = {
    "p_father",
    "p_grand",
    "pseudo_uuid_2",
}


@click.command()
@click.option(
    "-f", "--fields",
    type=click.Choice(RECOMPUTABLE_FIELDS),
    help="List of pseudo uuid2 fields wanted to recompute",
    required=0
)
@click_odoo.env_options()
def main(env, fields):
    partner = env["res.partner"]
    partner.recompute_pseudo_uuid_2(fields)

if __name__ == "__main__":
    main()
