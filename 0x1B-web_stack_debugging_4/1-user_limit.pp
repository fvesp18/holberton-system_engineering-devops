# Manifest to alot more open file space for user
exec { 'sed -i -e "s/hard nofile 5/hard nofile 30000/g" -e "s/soft nofile 4/soft nofile 50000/g" /etc/security/limits.conf':
provider => shell,
}
