import csv
import os
import sys
import time

import imagehash
from PIL import Image
import pybktree


def hdist(x, y):
    return x[0] - y[0]


def main():
    averageTime = []
    for i in range(55):
        start = time.time()

        distance = i // 5
        #hashFunction = imagehash.average_hash
        #hashFunction = imagehash.dhash
        #hashFunction = imagehash.phash
        hashFunction = imagehash.whash

        # Image file extensions, more can be added if necessary
        ext = ('.jpg', '.jpeg', '.gif', '.png')

        tree = pybktree.BKTree(hdist, [])
        potentialDuplicates = []

        for filename in os.listdir('.'):
            if filename.endswith(ext):
                # Calculates the hash and adds it to the tree
                with Image.open(filename) as img:
                    hashval = hashFunction(img)

                    # Checks for potentially duplicate images
                    for pd in tree.find((hashval, filename), distance):
                        potentialDuplicates.append((filename, pd[1][1]))
                    tree.add((hashval, filename))

        print(i)

        f = 'foundchanges' + str(i) + '.txt'
        with open(f, 'w') as out:
            writer = csv.writer(out, delimiter=',')
            writer.writerows(potentialDuplicates)

        end = time.time()
        averageTime.append((i, end - start))

    with open('whash.txt', 'w') as out:
        writer = csv.writer(out, delimiter=',')
        writer.writerows(averageTime)


if __name__ == '__main__':
    main()
