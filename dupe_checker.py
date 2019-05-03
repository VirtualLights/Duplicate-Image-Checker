import os
from PIL import Image
#https://python-pillow.org/	
	
def main():
	#File path of the script
	filepath = os.path.realpath(__file__)
	
	#Image file extensions, more can be added if necessary
	ext = ('.jpg', '.jpeg', '.gif', '.png')
	
	#Dict of two tuples
		#Key = (width, height)
		#Value = (filename, phash)
	checked_images = {}
	#List of tuples of potentially duplicate images (filename1, filename2)
	potential_duplicates = []
	
	for filename in os.listdir(filepath):
		#Skips non-image files
		if filename.endswith(ext):
			#Gets the dimensions of the image
			with Image.open(filename) as img:
				width, height = img.size
				if (width, height) in checked_images:
					#Checks if a hash already exists for the other file
					if checked_images.get((width, height))[1] is None:
						#Calculate the hash of the other image and update value
					#Calculate the hash of the current image
				#Calculate pHash of the two images, if they are the same, add them to the potential_duplicates list
				else:
				#Add the dimensions to the checked_images dict
				#Hash is not calculated unless there is a potential duplicate image
					checked_images[(width, height)] = (filename,None)
		else:
			continue
			
	print(f'Found {len(potential_duplicates)} potential duplicate images.')
	if len(potential_duplicates) != 0:
		for i in potential_duplicates:
			print(i)