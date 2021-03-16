import argparse
def parse_args(args):
    parser = argparse.ArgumentParser(...)
    parser.add_argument("-n", "--name", default="ahui", help="your name")
    args = parser.parse_args(args)
    assert args.name=='ahui1'

def test_parser(self):
    parser = parse_args(['-l', '-m'])
