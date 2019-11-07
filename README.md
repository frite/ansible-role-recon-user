Role Name
=========

This role creates a user, sets up his SSH key, creates custom directories, 
adds user to sudo and installs [recon profile](https://github.com/nahamsec/recon_profile)

Requirements
------------
If you are running this from a Mac, you need to install passlib.

`pip install passlib`.


Role Variables
--------------
The following variables can be set

* `include_recon_profile`. 
    - By default, it is set to `true` 
    - It will install [recon profile](https://github.com/nahamsec/recon_profile).
    - Example value `include_recon_profile: true`
* `authorized_key`. 
    - By default, it is set to `files/id_rsa.pub`.
    - Points to where the SSH key is.
    - Example value `authorized_key: files/id_rsa.pub`   
* `username` 
    - By default it is set to `recon`.
    - It controls the preferred username.
    - Example value `username: recon`.
* `preferred_shell`
    - By default it is set to `/bin/bash`.
    - It controls the default shell for the user.
    - Example value `preferred_shell: /bin/bash`
* `home_dir`
    - By default it is set to `/home/{{ username }}/`
    - It controls the preferred home for user.
    - Example value `home_dir:"/home/{{ username }}"`
* `group_membership`
    - By default, it is set to `sudo`.
    - It controls the privileged group.
    - Example value `group_membership: 'sudo'`
* `custom_dirs`
    - By default, it contains only `targets`.
    - It can contain as many directories as you want.
    - Example value 
        ```
            custom_dirs:
                - targets
                - whatever      
        ```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: frite.recon-user }

License
-------

BSD


