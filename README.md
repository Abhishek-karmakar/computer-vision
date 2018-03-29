Computer vision. 
----------------

Overall plan

Face detection intiution
 - Viola jones algorithm. 
 - Haar like features
 - Integral image
 - Training Classifiers
 - Adaptive Boosting (Ada boost)
 - Cascading


 Viola Jones Algorithms

 	- One of the most powerful algorithms todate.
 	- Developed in 2001, 
 	- Slowly being surpassed by deeplearning but still very effective.
 	- Real time face detection in videos and photos.
 	- The algorithm first does Training & then Detection.

How the face detection happens. 

 	- We'll take a photo, a frontal face, Viola Jones is designed for frontal face. 
 	- It first turns it into Grayscale. It will start looking for a face. 
 	- It will start from the top left and it will start looking for the features. Predefined features. Like Eyebrow, eyes, Nose, Mouth, Cheek,Chin
 	- In every step it will look for a feature and it will start looking for features like, Eyebrow, Nose, when it can detect a full face then it will
 	- When it finds all the features present in its box then it will highlight it 
 	- The size of the box also increase or decrease becase the face in the picture can be bigger or smaller. 
 	- When many boxes overlap then it understands that there is a face and it will finally highlight it.  

Harr Like Features. 

	- Developed by Mr. Alfred Harr. Some features. 
	- Edge Features, Line Features & Four Rectangle feature. These features are understood by viola-jones and they were worked on. 
	- In a photo they detect edges which help in understanding what kind of feature is present in a photo. 
	- The viola-jones algorithm understands which Harr like feature is present in a block of calculation and then. 
	- If you convert any photo in a grayscale then because of the light and shadow, there are most of the features which are present in almost any face. 
	- If we devide a part of the box into a 2D array of pixel then we can devide the whole box into various intensity from 
	- calculate the sum of all the pixels and then it divides by the number of pixel to find out the average to find out the intensity of the pixel. 
	- Difference between the Average of Black and Average of white pixel , if that is equal to 1 or more than 0.3 then its similar to harr like feature
	- If the value is > 0.3 then there is a Harr Like Feature, If on the other hand there is a 0.1 or less than the threshhold then there is no harr like feature. 
	- The only thing that the algo knows that a set of pixel which is called a a feature needs to be found inthe whole image. 
	- It might detect a type of feature in a lot of places in a photo but with the help of other attributes it will find out that maybe the detected features is not what it is. This happens via training. 
	- after training it detects which features are commonly found in some part of the space. 


Integral Image

	- In order to evaluate if a feature is present we need to calculate the pixels and this is going to take a lot of compute power and is not very effecient , specially if this needs to be done very quickly over and over again. 
	- To prevent this we have a hack and this is where the integral image comes in. 

	- The larger the feature the more pixels value we have to add to detect a feature and if there are more features. 
	- To solve this we will use an integral image. 
	- integral image is a set of pixel where each pixel is a sum of all the left side and up pixels and then find the differene of the sum of the pixels of the left outer and up outer cell . This reduces the operation to only 4 calculations however big the image might be. 

Training classifiers
	
	- Identify the featuers and set the features. 
	- How to know when it is present. 
	- Shrink the image to 24 x 24 pixel. When the image is bigger then its difficult to calculate. 
	- One image is not enough, so its good to have a lots and lots of image to give more and more data. 
	- If you are training your own algorithm then its also kay to mirror these images because they are completely different for the computer.
	 - From the 9000 images we can find out what features are common for faces but only for faces. 
	 - Also image which are non face images also need to supplied and there has to be absolutely no faces present in them. 350000000 windows
	 - Face Images - the algorithm should pick up a lot of features which from the face images but it should also know frm the non face images which featuers are labled as false-positive which means it might detect some facelike features from the non-face images but since they are already labled as a non-face, it would know that these images are not supposed to be detected as face detection features. 


