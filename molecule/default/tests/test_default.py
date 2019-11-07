import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_recon_user(host):
    """ Assert user exists on host with the right shell
    and in the right group. """
    user = host.user('recon')

    assert user.exists
    assert user.shell == '/bin/bash'
    assert user.home == '/home/recon/'
    assert 'sudo' in user.groups


def test_source_file(host):
    """ Assert recon_tools directory exists in user's home folder. """
    recon_tools = host.file('/home/recon/.recon_tools')

    assert recon_tools.exists


def test_ssh_authorized_file(host):
    """ Assert SSH authorized key exists in user's home folder. """
    authorized_keys = host.file('/home/recon/.ssh/authorized_keys')

    assert authorized_keys.exists
    assert authorized_keys.contains('SomeTestKey')


def test_custom_dir(host):
    """ Assert recon_tools directory exists in user's home folder. """
    custom_dir = host.file('/home/recon/targets')

    assert custom_dir.exists
    assert custom_dir.is_directory
    assert custom_dir.user == 'recon'
    assert custom_dir.group == 'recon'
    assert oct(custom_dir.mode) == '0700'
