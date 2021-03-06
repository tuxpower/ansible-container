from setuptools import setup
import container

setup(
    name='ansible-container',
    version=container.__version__,
    packages=['container', 'container.shipit', 'container.shipit.openshift', 'container.shipit.openshift.modules'],
    include_package_data=True,
    url='https://github.com/j00bar/ansible-container',
    license='LGPLv3 (See LICENSE file for terms)',
    author='Joshua "jag" Ginsberg and others (See AUTHORS file for contributors)',
    author_email='jag@flowtheory.net',
    description=('Ansible Container empowers you to orchestrate, build, run, and ship '
                 'Docker images built from Ansible playbooks.'),
    entry_points={
        'console_scripts': ['ansible-container = container.cli:commandline']
    }
)
