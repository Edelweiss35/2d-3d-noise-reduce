import cv2


def video_write_remove_noise(videofile):

	#cap = cv2.VideoCapture(0)  webcam
	cap = cv2.VideoCapture(videofile)
	if(not cap.isOpened()):
		print("file is not exists")
		return "error"
	fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
	out = cv2.VideoWriter('result.avi',fourcc,10,(int(cap.get(3)),int(cap.get(4))),True)

	frame_count = 0
	while True:
		ret, frame = cap.read()
		if frame is None:
			break

		if ret==True:

			denoise_frame = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
			out.write(denoise_frame)
			#cv2.imshow("name", denoise_frame)
		else:
			break
		print(frame_count)
		frame_count +=1

	cap.release()
	out.release()
if __name__ == "__main__":

	video_write_remove_noise("test.mp4")



