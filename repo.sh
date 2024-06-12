touch /etc/yum.repos.d/media.repo

cat > /etc/yum.repos.d/media.repo <<EOF
[BaseOS]
name=BaseOS
baseurl=http://@@{repo_ip}@@/BaseOS
gpgcheck=0
enabled=1

[AppStream]
name=AppStream
baseurl=http://@@{repo_ip}@@/AppStream
gpgcheck=0
enabled=1
