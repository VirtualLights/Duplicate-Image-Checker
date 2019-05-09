import os
import sys
from PIL import Image
import imagehash
import pybktree
#https://python-pillow.org/	

def hdist(x, y):
	return pybktree.hamming_distance(x[1], y[1])

def main():
	#File path of the script
	filepath = os.path.realpath(__file__)
	
	#Makes sure arguments are correct
	if len(sys.argv) != 3:
		raise TypeError("Invalid number of arguments.")
	
	#Determines which hash functions to use
	if sys.argv[1] == 'p':
		hash_function = imagehash.phash
	if sys.argv[1] == 'd':
		hash_function = imagehash.dhash
	if sys.argv[1] == 'w':
		hash_function = imagehash.whash
	else:
		raise ValueError("Invalid hash function selection, expected 'p', 'd', or 'w', recieved {}".format(sys.argv[1])

	#Hamming distance to be used 
	try:
		if float(sys.argv[2]) >= 0:
			distance = sys.argv[2]
	except:
		raise ValueError("Invalid Hamming distance value, expected positive number, recieved {}.".format(sys.argv[2])
	
	#Image file extensions, more can be added if necessary
	ext = ('.jpg', '.jpeg', '.gif', '.png')
	
	tree = pybktree.BKTree(hdist, [])
	potential_duplicates = []
	for filename in os.listdir(filepath):
		if filename.endswith(ext):
			#Calculates the hash and adds it to the tree
			with Image.open(filename) as img:
				hash = hash_function(img)
				tree.add(filename, hash)
			
				#Checks for potentially duplicate images
				for pd in sorted(tree.find((filename, hash), dist)):
					potential_duplicates.append((filename, pd[0]))
			
	print(f'Found {len(potential_duplicates)} potential duplicate images.')
	if len(potential_duplicates) != 0:
		for i in potential_duplicates:
			print(i)			
			
if __name__ == '__main__':
	main()