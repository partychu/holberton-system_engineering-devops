# SSH configuration file so that you can connect to a server without typing a password

file_line { 'identity file':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => 'IdentityFile',
}

file_line { 'password authentication':
  ensure  => present,
  path    => '~/.ssh/config',
  line    => 'PasswordAuthentication no',
  match   => 'PasswordAuthentication',

