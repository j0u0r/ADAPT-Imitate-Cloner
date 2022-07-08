name = input("VM vagrant/vm provider display name: ")
hostname = input(f"({name}) VM hostname: ")
ip = input(f"({name}) IP address (192.168.56.123): ")
gateway = input(f"({name}) Gateway (192.168.56.1): ")
dns = input(f"({name}) DNS (8.8.8.8): ")
memory = int(input(f"({name}) Memory (3072): "))
cpus = int(input(f"({name}) CPUs: "))

# havent shifted scripts over (check vagrant-victim), havent changed scripts (change to user input)
vagrantcontent = f'\
Vagrant.configure("2") do |config|\n\
    config.vm.define "{name}" do |cfg|\n\
        cfg.vm.box = "detectionlab/win2016"\n\
        cfg.vm.hostname = "{hostname}"\n\
        cfg.vm.boot_timeout = 600\n\
        cfg.winrm.transport = :plaintext\n\
        cfg.vm.communicator = "winrm"\n\
        cfg.winrm.basic_auth_only = true\n\
        cfg.winrm.timeout = 300\n\
        cfg.winrm.retry_limit = 20\n\
        cfg.vm.network :private_network, ip: "{ip}", gateway: "{gateway}", dns: "{dns}"\n\
        cfg.vm.provision "shell", path: "scripts/fix-second-network.ps1", privileged: true, args: "-ip {ip} -dns {dns} -gateway {gateway}" \n\
        cfg.vm.provider "vmware_desktop" do |v, override|\n\
            v.vmx["displayname"] = "{name}"\n\
            v.memory = {memory}\n\
            v.cpus = {cpus}\n\
            v.gui = true\n\
        end\n\
    end\n\
end'

vagrantfile = open("./Vagrant/Vagrantfile","w")
vagrantfile.write(vagrantcontent)
vagrantfile.close()