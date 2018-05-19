#!/usr/bin/python3

# This file is part of obs-service-rust2rpm
# Author: Neal Gompa <ngompa13@gmail.com>
#
# Fedora-License-Identifier: MIT
# SPDX-License-Identifier: MIT
# Please see LICENSE for the full details of the license terms
#
# This file is a wrapper script around rust2rpm for consumption by OBS

import argparse
import os
import pathlib
import shutil
import subprocess
import sys

parser = argparse.ArgumentParser(description="Generate Rust crate source package content")

parser.add_argument("-n", "--name", help="Name of crate on crates.io", required=True)
parser.add_argument("-v", "--version", help="Version of crate to fetch", default=None)
parser.add_argument("-t", "--type", help="Type of distribution package (default: %(default)s)", choices=["plain", "fedora", "mageia", "opensuse"], default="opensuse")
parser.add_argument("-o", "--outdir", help="Directory to generate packaging content", required=True)

args = parser.parse_args()

# Then, check for rust2rpm
rust2rpm = shutil.which("rust2rpm")

# Bomb out early if rust2rpm is missing
if rust2rpm is None:
	sys.exit("Missing rust2rpm, check if it is installed.")

# Build rust2rpm command
rust2rpm_cmd = [rust2rpm, "-s", "-t", args.type, args.name]

if args.version is not None:
	rust2rpm_cmd += [args.version]

# Adjust environment for source service rust2rpm run
rust2rpm_runenv = dict(os.environ)

if pathlib.Path("/var/cache/obs/rust2rpm").is_dir():
	rust2rpm_runenv["XDG_CACHE_HOME"] = "/var/cache/obs"

# Run rust2rpm command
try:
	subprocess.check_call(rust2rpm_cmd, cwd=args.outdir, env=rust2rpm_runenv)
except subprocess.CalledProcessError as rust2rpm_err:
	sys.exit("rust2rpm failed with error code: {}".format(rust2rpm_err.returncode))
