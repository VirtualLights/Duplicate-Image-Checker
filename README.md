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
Place the script in the folder containing the images. Then, call the script. Output format and hyperparameter tuning are a WIP.
