import sys
import subprocess

import re


def get_process_stack(pid):
  cmd="pstack %s" % pid
  res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
  return res.stdout.read()

def filter(stacks):
  pattern = '''^Thread [0-9]*'''
  in_stack = False
  user_space = False
  lines = stacks.split('\n')
  groups = []
  i = 0
  group = []
  while i < len(lines):
    if re.search(pattern, lines[i]):
      if group:
        groups.append(group)
      group = []
    group.append(lines[i])
    i = i+1

  for grp in groups:
    if 'GLIBC' in grp[1] or 'libc.so' in grp[1] or 'libpthread.so' in grp[1]:
      continue
    for line in grp:
      print line


if len(sys.argv) != 2:
  print "usage: ustack pid"
  sys.exit(1)

pid = sys.argv[1]

res = get_process_stack(pid)

filter(res)
