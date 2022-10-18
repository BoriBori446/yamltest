import yaml
import argparse
import os


def init_parser():
    parser = argparse.ArgumentParser(description="for GINOU-DENSYO")
    parser.add_argument("--config", "-c", type=str, default="", help="ID of the using config", required=True)
    parser.add_argument("--dataset_name", "-dn", type=str, default="")
    parser.add_argument("--loadcell_args", "-la", type=str,default="")
    return parser


def update_params(parser, args):
    if os.path.exists("settings/{}.yaml".format(args.config)):
        with open("settings/{}.yaml".format(args.config), "r") as f:
            try:
                yaml_args = yaml.load(f, Loader=yaml.FullLoader)
            except:
                yaml_args = yaml.load(f)
            default_arg = vars(args)
            for key in yaml_args.keys():
                if key not in default_arg.keys():
                    raise ValueError("Do NOT exist this parameter {}".format(key))
                parser.set_defaults(**yaml_args)
    else:
        raise ValueError('Do NOT exist this file in \'configs\' folder: {}.yaml!'.format(args.config))

    return parser.parse_args()


def main():
    print("")
    parser = init_parser()
    args = parser.parse_args()

    args = update_params(parser, args)

    print(args.loadcell_args["divid"])


if __name__ == "__main__":
    main()
