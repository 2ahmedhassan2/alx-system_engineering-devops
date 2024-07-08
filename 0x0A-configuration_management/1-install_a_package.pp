# installing specified package

exec { 'Flask':
  command => '/usr/bin/apt-get -y install puppet-lint -v 2.1.0 ',
}