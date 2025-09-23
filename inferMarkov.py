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
import cleaner, random, time

# == Inference method ==
def inferMarkov(message, ngram, mappings, maxLen):
    msg = cleaner.cleanText(message.lower()).split()
    
    # We'll try and find the closest match to their prompt
    if len(msg) < ngram:
        # Search all the keys... (slow A.F)
        keys = list(mappings.keys())
        random.shuffle(keys) # Fastest
        for key in keys:
            window = key.split()
            if window[-len(msg):] == msg:
                break # Best option
    else:
        window = msg[-ngram:]
        
    genLen = 0
    print("AI: ", end="")
    
    inChain = mappings.get(' '.join(window))
    
    # Hallucinate an answer if we don't know... (Keeps it fluid.)
    if not inChain:
        keys = list(mappings.keys())
        random.shuffle(keys)
        window = keys[0].split()
        inChain = mappings.get(' '.join(window))
        
    while inChain and genLen <= maxLen:
        result = random.choice(inChain)
        print(result.upper(), end=" ", flush=True)
        genLen += 1
        window.pop(0)
        window.append(result)
        time.sleep(0.1)
        inChain = mappings.get(' '.join(window))
    
    print()