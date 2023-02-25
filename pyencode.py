#!/usr/bin/python

import sys, os, argparse

def	get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("script", type=str)
	parser.add_argument('-i', '--ifs', action='store_true')
	args = parser.parse_args()
	if not os.path.exists(args.script):
		sys.stderr.write(f"[-] Error <{args.script}> not a file")
	return args.script, args.ifs


def encode_script(script_name: str):
	contents = ''
	with open(script_name, "rb") as f:
		contents = f.read().decode('utf-8')
	code = '+'.join([f"chr{ord(char)}" for char in contents])
	script = '+'.join([f"chr{ord(char)}" for char in "<script>"])
	exe = '+'.join([f"chr{ord(char)}" for char in "exec"])
	return str(code), str(script), str(exe)


if __name__ == '__main__':
	script_name, ifs = get_args()
	code, script, exe = encode_script(script_name)
	out = f'python -c "exec(compile({code}, {script}, {exe}))"'
	if ifs:
		out = out.replace(" ", "${IFS}")
	print(out)
