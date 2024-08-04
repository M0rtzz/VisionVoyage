#!/home/m0rtzz/Program_Files/anaconda3/envs/VisionVoyage/bin/python3

import dataset_utils
from get_fisheye_dataset import DataCollector
import os
import argparse


def main():
    parser = argparse.ArgumentParser(description='arg parser')
    parser.add_argument('-c', '--cfg_file', type=str, default='fish_eye.yaml', help='specify the config for collector')

    args = parser.parse_args()
    cfg_file = os.path.join("./scripts/configs", args.cfg_file)
    collector_config = dataset_utils.config_from_yaml(cfg_file)

    data_collector = DataCollector(collector_config)
    data_collector.start_collecting()


if __name__ == '__main__':
    main()
