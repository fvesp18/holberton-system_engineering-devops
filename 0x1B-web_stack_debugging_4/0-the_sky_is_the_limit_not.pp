# Manifest to change request limits
exec { 'sed -i "s/-n 15/-n 4096/g" /etc/default/nginx && sudo service nginx restart':
provider => shell,
}
