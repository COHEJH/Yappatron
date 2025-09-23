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
import alive_progress, os

# == Build method ==
def buildMarkov(trainingData: str, windowSize: int) -> dict[str, list[str]]:
    splitData = trainingData.split()
    windowSize = windowSize % len(splitData)
    window = splitData[:windowSize]
    mappings: dict[str, list[str]] = {}
    dataLen = len(splitData)
    
    columns = os.get_terminal_size().columns
    windows = alive_progress.alive_it(range(windowSize, dataLen), max_cols=columns)
    
    for position in windows:
        
        key = ' '.join(window)
        if mappings.get(key):
            mappings[key].append(splitData[position])
        else:
            mappings[key] = [splitData[position]]
        
        window.pop(0)
        window.append(splitData[position])
    
    return mappings