"""
Help/utility functions for the documentation and examples
"""

import urllib.request
from zipfile import ZipFile
import pathlib
from typing import Union
import io

def download_repo_snapshot(target_path: Union[pathlib.Path, str], error_if_exists=False, repo_name='dss_python', use_version=True) -> bool:
    """
    This will try to download the snapshot of `repo_name` (from DSS-Extensions) as a 
    zip file, decompressing it inside `target_path`, renaming the resulting folder 
    to `repo_name`.

    The file will be decompressed inside `target_path` first to avoid potential
    issues with moving across different filesystems.
    """
    if use_version:
        from . import __version__ as ver
        if 'dev' not in ver:
            # Download the tagged version
            ref = f'tags/{ver}.zip'
            tag = ver

    if not use_version or 'dev' in ver:
        # Download the master branch
        ref = 'heads/master.zip'
        tag = 'master'

    target = pathlib.Path(target_path).absolute()

    if not target.exists():
        target.mkdir(parents=True)

    tmp_target = target / f'{repo_name}-{tag}'
    final_target = target / repo_name
    if final_target.exists():
        if not error_if_exists:
            return final_target
        
        raise FileExistsError(f"Target path already exists: {final_target}")

    if tmp_target.exists():
        if not error_if_exists:
            return None
        
        raise FileExistsError(f"Temporary target path already exists: {tmp_target}")
    
    url = f"https://github.com/dss-extensions/{repo_name}/archive/refs/{ref}"
    with urllib.request.urlopen(url) as f:
        zip_data = f.read()
        
    with io.BytesIO(zip_data) as f, ZipFile(f) as zf:
        zf.extractall(target_path)

    tmp_target.rename(final_target)
    return final_target


def download_examples(target_path: Union[pathlib.Path, str], error_if_exists=False, repo_name='dss_python'):
    out_path = download_repo_snapshot(target_path=target_path, error_if_exists=error_if_exists, repo_name=repo_name)
    download_repo_snapshot(target_path=out_path / 'docs' / 'examples', error_if_exists=error_if_exists, repo_name='electricdss-tst')


__all__ = [
    'download_repo_snapshot',
]
