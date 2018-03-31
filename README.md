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

Haar-Like Features. 

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

Adaboost or Adaptive Boosting.

	- Using Training classifiers the algorithms understand features which detect faces and discasrd which are classified and non-face features. Even in a 24 x 24 pixel image the number of features are approximately 180,000 base features using. 
	- We might have to calculate 180,000 for all the ~10000 faces. and when we re deteting this might take another set of 180000 features. 
	- Adaptive Boosting helps solve this problem. 
	- fx = A1F1(x) + A2F2(x) + A3F3(x) + ... each one of them is a feature in its own. They together become a strong classifier. 
	- fx = Strong Classifier but the rest of them independently are weak classifier. 
	- Lets you have 10 photos . 5 faces and 5 non faces. 
	- We identify a featuer which is important, exaple nose bridge. So in 3 face photos it does find the feature. which are correct and it also finds a feature on a non-face photo. 
	- The best approach is to complement it with something which will fix the weakness of one of the features 
	- The algorithm will now pick each feature classifier and run each photo wth it and it will keep on checking all the features with the previous one till the time it had detected all of them. 
	- The idea is to reach a high level of classification result. 

Cascading
	
	- Another hack to speedup the process
	- We take a sub-window and we look for the first feature in the sub window, then we reject the sub windown and we do not even look at that sub-window anymore. 
	- If the first feature is present then we move to the second feature and look for it. If its present then we move ahead and look for the third feature else we reject and we move forward. 
	- In actuality in the first step it looks for Top 5 features. If none of them are present, Then in the next feature it will look for next 15 features .. then next step it will look for 25 features. 
	- If the feature is not present in the Subwindow then it will simply reject the subwindow ompletely. 
	- THis really speeds up the whole process. 
	

Setting up the envinroment for creating the virtual environment. 

	1.> Download the yml file from SDS website. http://www.superdatascience.com/wp-content/uploads/2017/09/Installations.zip and extract it to get virtual_platform_linux.yml 

	2.> Download and Install Anaconda. 

	3.> Navigate to the folder where the yml file is present and run # conda env create -f virtual_platform_linux.yml 

	4.> The above command will create a virtual environment which can be accessed by Anaconda-Navigator using from the Upper-Left combo selection box from there just select Vitrual_environment. 

Start the code. 

	1.> Load the harrlikefeatures xml files from open-cv repositry https://github.com/opencv/opencv/tree/master/data/haarcascades
	2.> import cv2 (open cv) and load the haarlikefeatures cascade xml files. 
	3.> Write the rest of the code. To show the Webcam on the screen, Pass the webcam buffer to the Canvas and draw canva on the screen. 

Run the Program.
	
	start environment -  source activate virtual_platform
	start python program - python face_recognition.py
	stop environment - source deactivate

## Single Shot Detection (SSD)

	- How SSD is different
	- The multi-box concept.
	- Predicting object position. 
	- The scale problem. 

	How is SSD different - In this kind of prediction there is a way of 


The Coding behind the SSD 

	- data - forlder that contain the classes base transform that will do the required transformations so that the input images will be compatible with the neural network. 

	- funnydog is the video of a dog that we want to detect. 
	- Layers - is another folder that contains some other tools for detection and multibox part of the SSD. 
	- ObjectDetectionCommented - 
	- ObjectDetectionNoComment
	- SSD.py - the architecture of the SSD multibox detection model. We will not implement this. If we implement the whole model then we will miss what is at the heart. After watching the 
	- the pth file we will be loading to use the pretrained model. This contains the weights of the already pretrained model. 

	We will be loading this file with Torch. torch.load will open a tensor, a Tensor that will already contain the weights of this model. Then with the mapping of a dictionary we will transfer these weights to the model that we implement. 

	the pth file containts the weights of a already pre-trained model. 


Libraries that we will use for object detection using SSD. 


Step - 1 - Import all the libraries. 

Torch - The torch library contains pytorch, to build a neural network and build computer vision. PyTorch contains DynamicGraphs, we are able to compute very effeciently the gradients of compsition functions in backward propagation. We have to update the weights of these gradient of these compsition functions to update the weights of the target and the prediction. 
Dynamic graphs is a highly advanced graph structure which allows computation at a very optimized way.

Autograd - module responsible for gradient descent , we are using the Variable class which will be used to convert the tensors into the torch variable which will contain both a Tensor and a Variable and and then the Torch variable containing a Tensor and the Variable will be one element of the graph. 

CV2 - to draw some rectangles around the object. The object detection will not happen with openCV harrcascade. they will be based on SSD. 

from data import BaseTransform, VOC_CLASSES as labelmap - Data is a folder in which these classes are present. BaseTransform is the class which will do all the transformation from input images will be compatible with the neural network. When we feed the neural network with the images we need a way to transform to these classes. 

VOC_Classes is the dictionary which will do encoding of the classes. Plants = one class, dogs = another class.  

from ssd import build_ssd - This is the SSD library in python that we will use to build the SSD object detection model. build_ssd 

imageio - library that we will use to process the images of the video and applying the detect function to process the image of the video and apply the detect function. pill(library can also be used)


Step - 2 
Write the Detect Function which will do the detection using SSD. (DeepLearning)

- We are going to do a frame by frame detection. It will not do the detection on the video directly. Using imageio we will extract all the frames from the video and apply the detect functions on the frames and then reassemble 

- it will take 3 arguments. image = frame, we do not need to use the grayscale, so we do not need to add gray. 
net = neural network. 
transform = they will transform it to riht format so that it can go into the neural network.

THis function will do detect the image. It will simply return the same frame with Lable & Dog. 

- get the heights and width of the frame. [0] index = height [1] = width

Transform from a numpy array to a Torch Tensor. 
we need to make 4 transformation. 

frame_t will be the transformed frame, frame_t is a nummpy array after transform , now we will change it to a torch_tensor
Neural_network SSD was trained with Green, Blue, Red - so we are need to reverse the 

We need to add a Fake dimesion to the batch. Because the neural network cannot accpt a single value. thats why we need to add create a fake structure. 

Convert the batch of Torch tensor of inputs into a Torch Variable. - A torch variable is a highly advanced variable which contains a Tensor and a Gradient. This torch variable will become an element of a dynamic graph which will compute very effeciently the gradient of anycomposition function during backward propagation. 

after the transformation is done we will load the weights to get out pretrained model. 

Step 6 : The heart of the SSD 
Detections took all the data. 
Tensor part of the Torch variable. 
By taking the data output of the 
now we will see what a tensor containts

We have to make a for loop. Because we have to go to each batch's each class's each occurance. and then we check if the vallue is more than 0.4 then its present in the file else its not persent in the film. 

OpenCV works with Numpy array. Now we need to add a rectangle around the object that we found out. 

Since we have a pretrained model we will use that.
Step 7 : 

 we will create a object that will reflect the Neural Network itself. Thanks to the build SSD fundctn. 
 We will get the weights from an already pre-trained SSD neural network. that will open a tensor. 
 The Torch.load will load the tensor. 
 We will then attribute the loadstate dict function of the function to our already pretrained to the instance of the obect. 



