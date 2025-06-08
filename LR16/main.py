import face_recognition
known_image = face_recognition.load_image_file("known.jpg")
unknown_image = face_recognition.load_image_file("unknown.jpg")
unknown_image_2 = face_recognition.load_image_file("unknown2.jpg")

known_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
unknown_encoding_2 = face_recognition.face_encodings(unknown_image_2)[0]

results_1 = face_recognition.compare_faces([known_encoding], unknown_encoding)
results_2 = face_recognition.compare_faces([known_encoding], unknown_encoding_2)

print(f'фото 1: {results_1}\nфото 2: {results_2}')