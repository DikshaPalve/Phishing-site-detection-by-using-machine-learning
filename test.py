# Purpose - Receive the call for testing a page from the Chrome extension and return the result (SAFE/PHISHING)
# for display. This file calls all the different components of the project (The ML model, features_extraction) and
# consolidates the result.

import joblib
import features_extraction
import sys
import numpy as np
import pickle

from features_extraction import LOCALHOST_PATH, DIRECTORY_NAME


def main():
    url = sys.argv[1]

    # Extract features from the given URL using your existing functions
    features = features_extraction.main(url)
    print(features)

    # Perform classification based on the count of -1 and 1 in the features array
    classification = classify_website(features)

    if classification == "SAFE":
        print("SAFE")
    elif classification == "PHISHING":
        print("PHISHING")

def classify_website(features):
    # Count the number of -1 and 1 in the features array
    negative_count = features.count(-1)
    positive_count = features.count(1)

    # Determine the classification based on counts
    if negative_count > positive_count:
        return "PHISHING"
    else:
        return "SAFE"


if __name__ == "__main__":
    main()
