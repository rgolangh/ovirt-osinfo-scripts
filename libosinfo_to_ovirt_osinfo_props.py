#!/usr/bin/python

from gi.repository import Libosinfo as osinfo;

loader = osinfo.Loader()
loader.process_path("/usr/share/libosinfo/db")
db = loader.get_db()

def get_os_id(os):
    return os.get_short_id().replace(".", "_")

osId = 1000
for os in sorted(db.get_os_list().get_elements()):
    osId+=1
    print "os.{0}.id.value = {1}".format(get_os_id(os), osId)
    print "os.{0}.name.value = {1}".format(get_os_id(os), os.get_name())
    print "os.{0}.family.value = {1}".format(get_os_id(os), os.get_family())
    print "os.{0}.derivedFrom = Other".format(get_os_id(os))

    for resources in os.get_minimum_resources().get_elements():
        print "os.{0}.cpu_architecture = {1}".format(get_os_id(os), resources.get_architecture())
        print "os.{0}.resources.minimum.ram.value = {1}".format(get_os_id(os), resources.get_ram() / 1048576)
        print "os.{0}.resources.minimum.disksize.value = {1}".format(get_os_id(os), resources.get_storage()/ 1048576)
        print "os.{0}.resources.minimum.numberOsCpus.value = {1}".format(get_os_id(os), resources.get_n_cpus())









