Hard to Soft:


Requirements:

Phone app that takes at least 1 picture of the photograph

	2 options for what it does next:
		1. Save the image to the disk, and do all the merging into one later
		2. Do the image processing and cut out the picture on device

Phone app then sends signal to Arduino that the picture has been taken and can move the robot onto the next photograph to take the picture of


Research topics:
	-How to combine images into one, and if it is possible to increase resolution by doing this
	-communicating between an Android app and the Arduino
	-Image processing on the phone vs sending to a computer to do the image combinations


Python code:
	Seperate images into each individual photograph
	match up photographs with similar other photographs from other files
	superresolution the resulting photos and save their data


Future ideas:
	Add some sort of IO to add year data to each batch of photographs
	Add date recognition to photos with the date in the corner
	