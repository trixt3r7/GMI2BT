import os
import cv2 as cv
import numpy as np


def face_training():
    print('=========== [ FACE TRAINING ] ===========')
    features = []
    labels = []

    print('[PROCESSING] ', end='')
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        # Print list of processed images
        # print(os.listdir(path))
        for img in os.listdir(path):
            print('.', end='')  # Dot indication of processing
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            face_rectangle = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in face_rectangle:
                faces_area = gray[y:y + h, x:x + w]
                features.append(faces_area)
                labels.append(label)
        print()
    print('[Face Training Finished!]')

    features = np.array(features, dtype='object')
    labels = np.array(labels)

    face_recognizer = cv.face.LBPHFaceRecognizer_create()

    # Train the Recognizer on the features list and the labels list
    face_recognizer.train(features, labels)

    face_recognizer.save('trainer.yml')


def face_recognition():
    print('========== [ FACE RECOGNITION ] =========')
    print('Loops through all images in /dataset/faces/validate')
    print('Images should appear in a new window, close image to see the next image in the loop.')
    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read('trainer.yml')

    abspath = os.getcwd()
    directory = r'dataset\faces\validate'
    path = os.path.join(abspath, directory)

    for img in os.listdir(path):
        img_path = os.path.join(path, img)
        img = cv.imread(img_path)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Detect the face in the image
        face_rectangle = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

        for (x, y, w, h) in face_rectangle:
            face_area = gray[y:y + h, x:x + w]

            label, confidence = face_recognizer.predict(face_area)
            # print(f'Label = {people[label]} with a confidence of {confidence}')
            img_label = f'{people[label]} {confidence:.2f}%'
            cv.putText(img, img_label, (30, 40), cv.FONT_HERSHEY_PLAIN, fontScale=1.5, color=(0, 230, 0), thickness=2)
            cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 230, 0), thickness=2)

        cv.imshow('Detected Face', img)
        cv.waitKey(0)


def logo():
    print(r" __ _  __ __    _  _____ __ _____ _  _")
    print(r"|_ |_|/  |_    | \|_  | |_ /   | / \|_) ")
    print(r"|  | |\__|__   |_/|__ | |__\__ | \_/| \ ")
    print()


def menu():
    print(f'1. Information - Data Gathering')
    print(f'2. Face training')
    print(f'3. Face recognition')
    print(f'4. Quit')


def information():
    print('\n============ [ INFORMATION ] ============')
    print('Dataset images have been downloaded with:')
    print('"Scraping-Google-Images-using-Python" from GitHub:')
    print('https://github.com/debadridtt/Scraping-Google-Images-using-Python')
    print()
    print('Next the images have been cropped and scaled (384x384px) in Photoshop.')
    print()
    print('To add other people, add images in folder named after that person in /dataset/faces/train/')
    print('Images to validate with are placed in /dataset/faces/validate/')
    input('Press Enter to continue...')


abspath = os.getcwd()
directory = r'dataset\faces\train'
DIR = os.path.join(abspath, directory)

# people = ['Bruce Lee', 'Brian Dennehy', 'Amy Winehouse', 'Heath Ledger']  # Static version
# Creates a list of objects (people) from \train\ directory
people = []
for i in os.listdir(DIR):
    people.append(i)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Menu Loop
while True:
    logo()
    menu()
    choice = input("Choose menu item: ")
    # if choice == '0':
    #     print("Nothing to see here, don't think this will be used.")
    if choice == '1':
        information()
    elif choice == '2':
        face_training()
    elif choice == '3':
        face_recognition()
    elif choice == '4':
        # Exit Program
        break
    else:
        print("Invalid menu item, please try again.")
