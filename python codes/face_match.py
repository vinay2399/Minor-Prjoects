import face_recognition
import cv2

video_capture= cv2.VideoCapture(0)
image=face_recognition.load_image_file('vicky.JPEG')
my_encoding=face_recognition.face_encodings(image)[0]
known_face_names=['vinay']
known_face_encoding=[my_encoding]
while(1):
    ret,frame=video_capture.read()
    #cv2.imshow('face_recognition',frame)
    #cv2.waitKey(0)
    rgb_frame=frame[:,:,::-1]
    #cv2.imshow('frame2',rgb_frame)
    #cv2.waitKey(0)
    face_location=face_recognition.face_locations(rgb_frame)
    face_encodings=face_recognition.face_encodings(rgb_frame,face_location)
    for (top,right,bottom,left),face_encoding in zip(face_location,face_encodings):
        matches=face_recognition.compare_faces(my_encoding,face_encodings)
        name='unknown'
        if (True in matches):
            first_match_index=matches.index(True)
            name=known_face_names[first_match_index]
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,name,(left+6,bottom),font,1.0,(0,0,255),1)
    cv2.imshow('frame_matching',frame)
    k=cv2.waitKey(30) &0xff
    if k==27:
        break
cv2.destroyAllWindows()
video_capture.release()
