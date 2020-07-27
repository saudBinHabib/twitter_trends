import pkg_resources

__version__ = '0.1.0'

try:
    pkg_version = pkg_resources.get_distribution('ttrends').version
except pkg_resources.DistributionNotFound:
    raise RuntimeError('Install ttrends, eg "pip install -e ."')

if pkg_version != __version__:
    raise RuntimeError('Reinstall ttrends, eg "pip install -e ."')
