#Modified from: https://www.pyimagesearch.com/2016/01/25/real-time-panorama-and-image-stitching-with-opencv/

def detectAndDescribe(self, image):
	# convert the image to grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# check to see if we are using OpenCV 3.X
	if self.isv3:
		# detect and extract features from the image
		descriptor = cv2.xfeatures2d.SIFT_create()
		(kps, features) = descriptor.detectAndCompute(image, None)

	# otherwise, we are using OpenCV 2.4.X
	else:
		# detect keypoints in the image
		detector = cv2.FeatureDetector_create("SIFT")
		kps = detector.detect(gray)

		# extract features from the image
		extractor = cv2.DescriptorExtractor_create("SIFT")
		(kps, features) = extractor.compute(gray, kps)

	# convert the keypoints from KeyPoint objects to NumPy
	# arrays
	kps = np.float32([kp.pt for kp in kps])

	# return a tuple of keypoints and features
	return (kps, features)

def matchKeypoints(self, kpsA, kpsB, featuresA, featuresB,
		ratio, reprojThresh):
	# compute the raw matches and initialize the list of actual
	# matches
	matcher = cv2.DescriptorMatcher_create("BruteForce")
	rawMatches = matcher.knnMatch(featuresA, featuresB, 2)
	matches = []
 
	# loop over the raw matches
	for m in rawMatches:
		# ensure the distance is within a certain ratio of each
		# other (i.e. Lowe's ratio test)
		if len(m) == 2 and m[0].distance < m[1].distance * ratio:
			matches.append((m[0].trainIdx, m[0].queryIdx))
		
		# computing a homography requires at least 4 matches
		if len(matches) > 4:
			# construct the two sets of points
			ptsA = np.float32([kpsA[i] for (_, i) in matches])
			ptsB = np.float32([kpsB[i] for (i, _) in matches])
 
			# compute the homography between the two sets of points
			(H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC,
				reprojThresh)
 
			# return the matches along with the homograpy matrix
			# and status of each matched point
			return (matches, H, status)
 
		# otherwise, no homograpy could be computed
		return None
