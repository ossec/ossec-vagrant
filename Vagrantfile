


Vagrant.configure("2") do |config|
  
  #config.vm.provision "shell", inline: "sudo bash -x /vagrant/setup-host.sh"

  config.vm.define "master" do |master|
    master.vm.box = "hashicorp/precise32"
    master.vm.hostname = "master"
    master.vm.network :private_network, ip: "172.17.2.10"
    #master.vm.provision "shell", inline: "sudo bash -x /vagrant/setup-host.sh master"
    master.vm.provision "puppet" do |puppet|
      puppet.facter = {
        "vagrant" => "1",
        "ossec_type" => "master",
      }
    end
  end

  config.vm.define "agent_precise32" do |agent_precise32|
    agent_precise32.vm.box = "hashicorp/precise32"
    agent_precise32.vm.hostname = "precise32"
    agent_precise32.vm.network :private_network, ip: "172.17.2.20"
    #agent_master.vm.provision "shell", inline: "sudo bash -x /vagrant/setup-host.sh agent"
    agent_precise32.vm.provision "puppet" do |puppet|
      puppet.facter = {
        "vagrant" => "1",
        "ossec_type" => "agent",
        "ossec_agent_id" => "001",
      }
    end
  end
#  config.vm.define "agent_fbsd10" do |agent_fbsd10|
#    agent_fbsd10.vm.box = "http://files.wunki.org/freebsd-10.0-amd64-wunki.box"
#    agent_fbsd10.vm.hostname = "fbsd10"
#    agent_fbsd10.vm.network :private_network, ip: "172.17.2.21"
#    #agent_master.vm.provision "shell", inline: "sudo bash -x /vagrant/setup-host.sh agent"
#    agent_fbsd10.vm.provision "puppet" do |puppet|
#      puppet.facter = {
#        "vagrant" => "1",
#        "ossec_type" => "agent",
#        "ossec_agent_id" => "002",
#      }
#    end
#  end
#  config.vm.define "agent_obsd53" do |agent_obsd53|
#    agent_fbsd53.vm.box = "https://dl.dropboxusercontent.com/u/12089300/VirtualBox/openbsd53_amd64_vagrant12.box"
#    agent_obsd53.vm.hostname = "obsd53"
#    agent_obsd53.vm.network :private_network, ip: "172.17.2.22"
#    #agent_master.vm.provision "shell", inline: "sudo bash -x /vagrant/setup-host.sh agent"
#    agent_obsd53.vm.provision "puppet" do |puppet|
#      puppet.facter = {
#        "vagrant" => "1",
#        "ossec_type" => "agent",
#        "ossec_agent_id" => "003",
#      }
#    end
#  end

#  config.vm.define "agent_obsd53" do |agent_obsd53|
#    agent_obsd53.vm.box = "https://dl.dropboxusercontent.com/u/12089300/VirtualBox/openbsd53_amd64_vagrant12.box"
#    agent_obsd53.vm.hostname = "precise32"
#    agent_obsd53.vm.network :private_network, ip: "172.17.2.21"
#  end
end
