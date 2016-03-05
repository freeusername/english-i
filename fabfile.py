# -*- coding: utf-8 -*-
# fabfile for Django:
from fabric.api import *
from djlime.fabfile import *


# globals
env.git_host = 'git.freshlimestudio.com'
env.project_name = 'efit'
env.venv_name = 'efit'
env.django_settings_module = 'efit.settings.dev'
env.repo = 'git@{git_host}:/projects/{project_name}'.format(**env)
env.use_ssh_config = env.remote_deployment
env.shared_dirs = 'config media/uploads media/sitemaps static releases/{current,previous}'


@task
def dev():
    """Development server"""
    env.user = 'deploy'
    env.branch = 'master'
    env.django_settings_module = 'efit.settings.stage'
    env.hosts = ['']
    env.vhosts_root = '/var/www/vhosts'
    env.host_name = 'freshlimestudio.com'
    env.vhost_path = '{vhosts_root}/{project_name}.{host_name}'.format(**env)
    env.release_path = '{vhosts_root}/{project_name}.{host_name}/releases/current'.format(**env)


@task
def prod():
    """Production server"""
    env.user = 'deploy'
    env.branch = 'master'
    env.django_settings_module = 'efit.settings.prod'
    env.hosts = ['']
    env.host_name = 'english-i.com'
    env.vhosts_root = '/var/www/vhosts'
    env.vhost_path = '{vhosts_root}/{host_name}'.format(**env)
    env.release_path = '{vhosts_root}/{host_name}/releases/current'.format(**env)
