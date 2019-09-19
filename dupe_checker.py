import os
import sys
from PIL import Image
import imagehash
import pybktree
import csv


def hdist(x, y):
    return x[0] - y[0]


def main():
    distance = 2
    #hashFunction = imagehash.average_hash
    hashFunction = imagehash.dhash
    #hashFunction = imagehash.phash
    #hashFunction = imagehash.whash

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
                    potentialDuplicates.append((filename, pd[1]))

                tree.add((hashval, filename))

    print(f'Found {len(potentialDuplicates)} potential duplicate images.')

    with open('foundchanges.txt', 'w') as out:
        csv_out = csv.writer(out)
        for row in potentialDuplicates:
            csv_out.writerow(row)


if __name__ == '__main__':
    main()
