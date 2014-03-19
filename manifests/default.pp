
define tarball($pkg_tgz, $module_name, $install_dir, $source_locations) {

    # create the install directory
    file { "$install_dir":
        ensure  => directory,
    }

    # download the tgz file
    file { "$pkg_tgz":
        path    => "/tmp/$pkg_tgz",
        source  => $source_locations, 
        notify  => Exec["untar $pkg_tgz"],
    }

    # untar the tarball at the desired location
    exec { "untar $pkg_tgz":
        command => "/bin/rm -rf $install_dir/*; /bin/tar --strip-components=1  --extract --gzip --verbose --file /tmp/$pkg_tgz -C $install_dir/",
        refreshonly => true,
        require => File["/tmp/$pkg_tgz", "$install_dir"],
    }
}
$ossec_packages = [
  "make",
  "gcc", 
]
package { $ossec_packages:
  ensure => "installed"
}

tarball { "ossec-hids.tar.gz":
  module_name => "ossec-hids",
  install_dir => "/tmp/ossec-hids",
  source_locations => [
    "/vagrant/ossec-hids-2.8.0.tar.gz",
    "/vagrant/ossec-hids-2.7.1.tar.gz",
    "/vagrant/ossec-hids-2.7.tar.gz",
    "/vagrant/ossec-hids.tar.gz",
    ],
  pkg_tgz => "ossec-hids.tar.gz", 
}

file { "preloaded-vars.conf":
  path => "/tmp/ossec-hids/etc/preloaded-vars.conf",
  source => "/vagrant/${ossec_type}-preloaded-vars.conf",
  notify => Exec["install.sh"],
  require => Tarball["ossec-hids.tar.gz"],
}

exec { "install.sh":
  command => "/bin/bash -x install.sh", 
  cwd => "/tmp/ossec-hids/",
  require => [
      File["preloaded-vars.conf"],
      package["make"],
      package["gcc"],
    ]
}


