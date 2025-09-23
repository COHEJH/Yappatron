# Yappatron - Build and run language models quickly and easily
# Copyright (C) 2025 COHEJH <jcohenkadosh@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# == Imports ==
from builder import buildModel
from inferer import inferModel
import builtins, argparse, os

# == Args ==
parser = argparse.ArgumentParser(description='Build and run language models quickly and easily')
parser.add_argument('MODEL', nargs="?", default=None, help="Model to run. If no model is specified, training mode is enabled.")
parser.add_argument('-l', '--length', default=128, help="Maximum response length (words) a model can give. Defaults to 128.")
args = parser.parse_args()

# == Global ==
builtins.yappatronVersion = 1
builtins.maxLength = args.length
builtins.spinAnimation = {"interval": 80,"frames": ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]}

if args.MODEL:
    inferModel(os.path.expanduser(os.path.expandvars(args.MODEL)))
else:
    buildModel()