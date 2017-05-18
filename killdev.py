#!/usr/bin/python
#
#~ kills django dev instances
import sys
import subprocess as p


def get_procs(port=8000, user='vagrant'):
    """find pids for runserver-processes running under `user` on `port`"""
    proc = "manage.py runserver 0.0.0.0:{p}".format(p=port)
    ps = p.check_output(['ps', 'aux']).split('\n')
    procs = []
    for line in ps:
        if proc in line:
            # line looks like:
            # <user>   <pid>  <other junk>
            info = line.strip().split(' ')
            user_name = info[0]
            if user_name != user:
                continue
            info = ' '.join(info[1:]).strip()
            pid = info.split(' ')[0]
            try:
                pid = int(pid)
            except ValueError:
                continue
            procs.append((pid, line))
    return procs


def main(port):
    procs = get_procs(port=port)
    for proc_info in procs:
        pid, info = proc_info
        kill = p.call(['kill', str(pid)])
        if kill == 0:
            print("Killed zombie 'runserver' running on port={}".format(port))
        else:
            print("Error occurred while trying to kill zombie 'runserver'")
            sys.exit(2)


if __name__ == '__main__':
    args = sys.argv[1:]
    port = 8000
    if args:
        try:
            port = int(args[0])
        except ValueError:
            print("Usage: killdev.py [port-num] --- default: port-num=8000")
    main(port)
    sys.exit(0)
