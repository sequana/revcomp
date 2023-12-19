import os
import subprocess
import tempfile

from click.testing import CliRunner

from sequana_pipelines.revcomp.main import main

from . import test_dir

sharedir = f"{test_dir}/data"


def test_standalone_subprocess():
    directory = tempfile.TemporaryDirectory()
    cmd = "sequana_revcomp --input-directory {} "
    cmd += "--working-directory {} --force"
    cmd = cmd.format(sharedir, directory.name)
    subprocess.call(cmd.split())


def test_standalone_script(tmpdir):

    wkdir = tmpdir.mkdir("wkdir")
    args = ["--input-directory", sharedir, "--working-directory", wkdir, "--force"]
    runner = CliRunner()
    results = runner.invoke(main, args)
    assert results.exit_code == 0


def test_full():

    with tempfile.TemporaryDirectory() as directory:
        wk = directory
        cmd = "sequana_revcomp --input-directory {} "
        cmd += "--working-directory {} --force"
        cmd = cmd.format(sharedir, wk)
        subprocess.call(cmd.split())
        stat = subprocess.call("sh revcomp.sh".split(), cwd=wk)


def test_version():
    cmd = "sequana_revcomp --version"
    subprocess.call(cmd.split())
