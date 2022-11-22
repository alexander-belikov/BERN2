from app import create_app

import argparse
from waitress import serve

def parse():
    parser = argparse.ArgumentParser(description="Arguments for BERN2")

    # FLASK arguments
    parser.add_argument("--host",
                        default="0.0.0.0",
                        type=str,
                        help="Host for running flask")
    parser.add_argument("--port",
                        default=5000,
                        type=int,
                        help="Port for running flask")

    # BERN2 model arguments
    parser.add_argument("--mtner_home",
                        default="./multi_ner",
                        type=str)
    parser.add_argument("--mtner_port",
                        default=18894,
                        type=int)
    parser.add_argument("--gnormplus_home",
                        default="./resources/GNormPlusJava",
                        type=str)
    parser.add_argument("--gnormplus_port",
                        default=18895,
                        type=int)
    parser.add_argument("--tmvar2_home",
                        default="./resources/tmVarJava",
                        type=str)
    parser.add_argument("--tmvar2_port",
                        default=18896,
                        type=int)
    parser.add_argument('--cache_host',
                        default='localhost')
    parser.add_argument('--cache_port',  
                        default=27017,
                        type=int)
    parser.add_argument("--gene_norm_port",
                        default=18888,
                        type=int)
    parser.add_argument("--disease_norm_port",
                        default=18892,
                        type=int)
    parser.add_argument("--use_neural_normalizer",
                        action="store_true")
    parser.add_argument("--keep_files",
                        action="store_true")
    parser.add_argument("--front_dev",
                        action="store_true")
    parser.add_argument("--no_cuda",
                        action="store_true")
    parser.add_argument(
        "--threads", type=int, default=8, help="number of concur threads"
    )
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse()
    print("Arguments:")
    for arg in vars(args):
        print("\t{}: {}".format(arg, getattr(args, arg)))

    app = create_app(args)
    serve(app, host=args.host, port=int(args.port), threads=args.threads)
