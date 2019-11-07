Ansible Role Recon User
=========
[![Build Status](https://travis-ci.org/frite/ansible-role-recon-user.svg?branch=master)](https://travis-ci.org/frite/ansible-role-recon-user)


This role creates a user, sets up his SSH key, creates custom directories,
adds user to sudo and installs [recon profile](https://github.com/nahamsec/recon_profile)

Requirements
------------
If you are running this from a Mac, you need to install passlib.

`pip install passlib`.


Role Variables
--------------
The following variables can be set

* `recon_user_include_recon_profile`.
    - By default, it is set to `true`
    - It will install [recon profile](https://github.com/nahamsec/recon_profile).
    - Example value `recon_user_include_recon_profile: true`
* `recon_user_authorized_key`.
    - By default, it is set to `files/id_rsa.pub`.
    - Points to where the SSH key is.
    - Example value `authorized_key: files/id_rsa.pub`
* `recon_user_username`
    - By default it is set to `recon`.
    - It controls the preferred username.
    - Example value `recon_user_username: recon`.
* `recon_user_preferred_shell`
    - By default it is set to `/bin/bash`. 
    - It controls the default shell for the user.
    - Example value `recon_user_preferred_shell: /bin/bash`
    - Updating this will require you to update `startup_file`, i.e. 
    ```
    startup_file:
        Ubuntu: .zsh
    ```
* `recon_user_home_dir`
    - By default it is set to `/home/{{ recon_user_username }}/`
    - It controls the preferred home for user.
    - Example value `recon_user_home_dir: "/home/{{ recon_user_username }}"`
* `recon_user_group_membership`
    - By default, it is set to `sudo`.
    - It controls the privileged group.
    - Example value `recon_user_group_membership: 'sudo'`
* `recon_user_custom_dirs`
    - By default, it contains only `targets`.
    - It can contain as many directories as you want.
    - Example value
        ```
            recon_user_custom_dirs:
                - targets
                - whatever
        ```
      
 Generally, you don't need to change anything but this is just me.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: frite.recon_user }

Installation is as easy as `ansible-galaxy install frite.recon_user`

Contribution guidelines
----------------------

Issues are welcome and so are code contributions.
Reg. code contributions, your code needs to pass all tests,
i.e. `molecule test` must succeed.

License
-------

BSD


