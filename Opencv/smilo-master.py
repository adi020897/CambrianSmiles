import cv2
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
smileCascade= cv2.CascadeClassifier('haarcascade_smile.xml')

# grab the reference to the webcam
vs = cv2.VideoCapture(0)
smilecount=0
smileval=0
# keep looping
while True:
	# grab the current frame
	ret, frame = vs.read()
  
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break
		
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.equalizeHist(gray)
		
	faces = faceCascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5, minSize=(45, 45))
	for (x,y,w,h) in faces:		
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		face_gray = gray[y:y+h, x:x+w]
		face_color = frame[y:y+h, x:x+w]
		smiles = smileCascade.detectMultiScale(face_gray, scaleFactor=1.7, minNeighbors=20)
		if(len(smiles)==0):
				smileval = smilecount
				if(smileval>0):
					print(f' + {smileval} smilecount to api')
					smilecount=0	
		else:
			for (ex,ey,ew,eh) in smiles:
				#print('face')
					cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
					smilecount=smilecount+len(smiles)
					print(f' + {smilecount} smilecount')
	
	# show the frame to our screen
	cv2.imshow("Video", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break 
# close all windows
cv2.destroyAllWindows()
