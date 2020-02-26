Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.box_check_update = true
  config.vm.network "forwarded_port", guest: 80, host: 8000

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
  SHELL
end
