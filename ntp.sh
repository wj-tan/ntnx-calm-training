dnf install -y chrony

systemctl enable chronyd
systemctl start chronyd

echo "server time.google.com iburst" | tee -a /etc/chrony.conf

systemctl restart chronyd
