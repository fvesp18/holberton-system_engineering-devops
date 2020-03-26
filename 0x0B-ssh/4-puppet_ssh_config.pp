#!/usr/bin/env bash
# Creates puppet to update config file
file_line {
'Turn off pass auth in config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no'
;
'Key Location',
  ensure => present,
  path   => '~/.ssh/holberton'
  line   => 'IdentityFile ~/.ssh/holberton'
}
