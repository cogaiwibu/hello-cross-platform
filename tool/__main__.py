#! /usr/bin/python

import argparse
import logging
import os
from pathlib import Path

from build_executor_factory import BuildExecutorFactory
from cleaner import Cleaner
from project_generator_factory import ProjectGeneratorFactory


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-profile', '--profile', default='Debug', type=str, help='Build profile')
    parser.add_argument('-platform', '--platform', default='osx', type=str,
                        help='Platform <android/ios/osx/linux/windows>')
    parser.add_argument('command', type=str, help='Command <build/clean>')

    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    root_path = Path(os.path.abspath(os.path.join(os.path.realpath(__file__), '..', '..')))
    build_path = Path(root_path, 'build')

    args = parse_arguments()

    build_factory = BuildExecutorFactory(root_path, args.platform)
    project_generator_factory = ProjectGeneratorFactory()

    if args.command == 'build':
        project_generator_factory.generate(args.platform, root_path, build_path, args.profile)
        build_factory.build(args.profile)

    elif args.command == 'clean':
        Cleaner(root_path).clean_all()
