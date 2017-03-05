import subprocess
from invoke import task


@task
def serve(ctx):
    run('cd static && python -m http.server')


@task
def download(ctx):
    """
    Download and install TinyMCE. Download link can be found at:

    https://www.tinymce.com/download/

    """
    url = 'http://download.ephox.com/tinymce/community/tinymce_4.5.4.zip'
    filename = url.rsplit('/', 1)[1]
    run('wget {}'.format(url))
    cmd = '&&'.join([
        'unzip ' + filename,
        'mv tinymce/js/tinymce static',
        'rm -r tinymce'
    ])
    run(cmd)


def run(cmd):
    shell = isinstance(cmd, str)
    print(cmd)
    subprocess.call(cmd, shell=shell)
