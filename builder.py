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
import questionary, os, cchardet, pickle
from halo import Halo
from buildMarkov import buildMarkov
from cleaner import cleanText

# == Build Model ==
def buildModel():
    # Model Settings
    modelName = questionary.text("Model Name:").ask()
    modelFile = modelName.replace(" ", "-")
    modelArch = questionary.select("Model Architecture:", choices=["Markov Chain"]).ask()
    trainingData = os.path.expanduser(os.path.expandvars(questionary.path("Training Data Path:", validate=lambda text: True if os.path.isfile(os.path.expanduser(os.path.expandvars(text))) else "Please enter a valid file path").ask()))
    
    # Detect Encoding
    encodingSpinner = Halo(text='Detecting dataset encoding...', spinner=spinAnimation) # type: ignore (Variable is global)
    encodingSpinner.start()
    with open(trainingData, 'rb') as f:
        dataEncoding = cchardet.detect(f.read())['encoding']
    encodingSpinner.succeed(f"Detected \"{dataEncoding}\" encoding")
    
    # Read and clean data
    cleaningSpinner = Halo(text='Cleaning dataset...', spinner=spinAnimation) # type: ignore (Variable is global)
    cleaningSpinner.start()
    try:
        with open(trainingData, "r", encoding=dataEncoding) as data:
            trainingText = cleanText(data.read())
        cleaningSpinner.succeed(f"Cleaned dataset \"{os.path.basename(trainingData)}\"")
    except Exception as e:
        cleaningSpinner.fail(f"Failed to clean dataset: {e}")
        return
    
    # Select, train and export model
    match modelArch:
        case "Markov Chain":
            windowSize = int(questionary.text("Window Size:", default="3", validate=lambda x: True if x.isdigit() else "Please enter a valid number").ask())
            model = buildMarkov(trainingText.lower(), windowSize)
            with open(f"{modelFile}.yap", "wb") as exportFile:
                pickle.dump({"name": modelName, "arch": modelArch, "window": windowSize, "minVersion": yappatronVersion, "model": model}, exportFile) # type: ignore (Variable is global)