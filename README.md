# Duplicate Image Detector
Checks to find potentially duplicate images in a folder.
Uses pHash, dHash, or wHash to find similar images, regardless of file format or resizing.
Uses BK-trees to find potential matches efficiently (runtime ≈ O(nlogn)) 

## Requirements:

* Python 3.0+
* [Pillow](https://python-pillow.org/) </li>
* [ImageHash](https://github.com/JohannesBuchner/imagehash) </li>
* [pybktree](https://github.com/Jetsetter/pybktree) </li>

## Instructions:
Place the script in the folder containing the images. Then, call the string with the following argments:
* Argument 1:  
	p: Uses pHash  
	d: Uses dHash  
	w: Uses wHash
* Argument 2: Non-negative number (Hamming distance), 0 for exact matches, suggested values are 0-10

Example: dupe_checker.py p 5.4
