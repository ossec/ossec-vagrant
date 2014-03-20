from paver.easy import *
from pygithub3 import Github
import pprint 

def _gh():
    gh = Github(user="ossec", repo="ossec-hids")
    return gh

@task
@consume_args
def status(args):
    print args
    cmd = "vagrant status"
    sh(cmd) 

@task
@consume_args
def destroy(args):
    cmd = "vagrant destroy"
    if "force" in args:
        cmd += " -f"
    else: 
        cmd += " ".join(args)
    sh(cmd) 

@task
@consume_args
def halt(args):
    cmd = "vagrant halt "
    if "force" in args:
        cmd += " -f "
    else: 
        cmd += " ".join(args)
    sh(cmd) 

@task
@consume_args
def up(args):
    cmd = "vagrant up "
    cmd += " ".join(args)
    sh(cmd)



@task
def pulls():
    gh = _gh()
    pull_requests = gh.pull_requests.list().all()
    for i in pull_requests:
        print "{0.number}\t{0.title}".format(i)


@task 
def getmaster():
    sh("wget -O files/ossec-hids-master.tar.gz https://github.com/ossec/ossec-hids/archive/master.tar.gz") 
    sh("ln -s files/ossec-hids-master.tar.gz ossec-hids.tar.gz")




@task
@consume_nargs(1)
def getpull(args):
    gh = _gh()
    pull_number = args[0]
    pull = gh.pull_requests.get(pull_number)

    #print dir(pull) 
    branch = pull.head['ref']
    full_name = pull.head['repo']['full_name']
    print "{}/tree/{}".format(branch, full_name)
    url = "https://github.com/{}/archive/{}.tar.gz".format(full_name, branch)
    sh("wget -O files/ossec-hids-pull-{}.tar.gz {}".format(pull_number, url))
    sh("ln -s files/ossec-hids-pull-{}.tar.gz ossec-hids.tar.gz".format(pull_number))


@task
@consume_args
def rebuild(args):
    halt(args)
    destroy(args)
    up(args)


