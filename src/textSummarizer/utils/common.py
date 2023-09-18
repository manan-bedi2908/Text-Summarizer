import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the yaml file.
    
    Raises:
        BoxValueError: If the yaml file is empty.
    
    Returns:
        ConfigBox: A ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Loaded yaml file from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Yaml file at {path_to_yaml} is empty.")
    except Exception as e:
        raise e
        
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
    Creates directories if they don't exist.
    Args:
        path_to_directories (list): List of paths to directories.
        ignore_log(bool, optional): ignore if multiple dirs is to be created. Defaults to False
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns size of a file or a directory.
    Args: 
        path (Path): Path to the file or directory.
    Returns:
        str: Size of the file or directory.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
