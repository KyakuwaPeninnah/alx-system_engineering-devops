# fixing file extension
exec { 'replace phpp with php':
  command  => 'sed -ie \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php',
  provider => shell
}

#restarting  apache2
exec { 'restart apache2 service':
  command  => 'service apache2 restart',
  provider => shell
}
