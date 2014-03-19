Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: "echo Hello"

  config.vm.define "ossec_master" do |ossec_master|
    ossec_master.vm.box = "hashicorp/precise32"
    ossec_master.vm.hostname = "master"
    ossec_master.vm.network :private_network, ip: "172.17.2.10"
  end

  config.vm.define "agent_precise32" do |agent_precise32|
    agent_precise32.vm.box = "hashicorp/precise32"
    agent_precise32.vm.hostname = "precise32"
    agent_precise32.vm.network :private_network, ip: "172.17.2.20"
  end

#  config.vm.define "agent_obsd53" do |agent_obsd53|
#    agent_obsd53.vm.box = "https://dl.dropboxusercontent.com/u/12089300/VirtualBox/openbsd53_amd64_vagrant12.box"
#    agent_obsd53.vm.hostname = "precise32"
#    agent_obsd53.vm.network :private_network, ip: "172.17.2.21"
#  end
end
