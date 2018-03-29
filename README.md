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


