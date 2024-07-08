exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.0.3',
  path    => ['/usr/bin', '/usr/sbin'],
  unless  => '/usr/bin/pip3 show Flask | grep Version | grep -q 2.1.0',
}