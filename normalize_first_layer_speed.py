#!/usr/bin/env python

import os
import re
import itertools
import concurrent.futures
import pathlib
import contextlib
import shutil

from python_toolbox import temp_file_tools
import click


@click.command()
@click.argument('path', type=click.Path(exists=True, dir_okay=False))
@click.option('-s', '--speed', default=10)
def normalize_first_layer_speed(path, speed):
    converted_speed = speed * 60
    path = pathlib.Path(path)
    with temp_file_tools.create_temp_folder() as temp_folder:
        with contextlib.ExitStack() as exit_stack:
            temp_path = temp_folder / '1.gcode'
            temp_file = exit_stack.enter_context(temp_path.open('w'))
            source_file = exit_stack.enter_context(path.open('r'))
            
            in_first_layer_section = False
            for line in source_file:
                if line.startswith('; layer 1,'):
                    in_first_layer_section = True
                elif line.startswith('; layer '):
                    in_first_layer_section = False
                if (in_first_layer_section and
                           re.match('^G1.* E[0-9.]*[1-9.]+[0-9.]*.* F', line)):
                    processed_line = re.sub(
                        ' F[0-9.]+', f' F{converted_speed}', line
                    )
                else:
                    processed_line = line
                temp_file.write(processed_line)
                
        path.unlink()
        shutil.copyfile(temp_path, path)
        
        
        

if __name__ == '__main__':
    normalize_first_layer_speed()