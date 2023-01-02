import argparse
import sys

import erutils.command_line_interface as cli

if __name__ == "__main__":
    pars = argparse.ArgumentParser()
    pars.add_argument('-url', '--url')
    opt = pars.parse_args()
    cli.fprint('this project is still in beta be careful how you use this')
    cli.fprint(sys.version)

    import erutils.utils as eu

    cli.fprint(f'Downloading {opt.url}')
    eu.download(f'{opt.url}')
