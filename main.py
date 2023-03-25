import argparse

from train import train
from yamlparser import read_config


def main():
    # parser = argparse.ArgumentParser(description="Semantic Segmentation Model")
    
    # parser.add_argument("-train", type = str, help = "config file", required = False)
    
    # args = parser.parse_args()
    
    # if args.train is not None:
    #     kwargs = read_config(args.train)
    #     train(kwargs)
        
    # else:
    #     print("No Train")
    
    train(read_config("config.yaml"))
        

if __name__ == "__main__":
    main()
    
# python main.py -train config.yaml