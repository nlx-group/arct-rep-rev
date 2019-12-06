from sklearn import svm

def get_data(source):
	vectors = []
	labels = []
	with open(source, "r") as fb:
		for line in fb:

			vector = []
			for value in line.split(",")[:-1]:
				vector.append(float(value))

			vectors.append(vector)
			labels.append(float(line.split(",")[-1]))

	return (vectors, labels)

train_vectors, train_labels = get_data("arct_original_train_w0-w1r.vectors")
development_vectors, development_labels = get_data("arct_original_development_w0-w1r.vectors")
test_vectors, test_labels = get_data("arct_original_test_w0-w1r.vectors")

clf = svm.SVC(gamma=0.3, C=3.8, kernel="poly", degree=2, cache_size=10000, verbose=False)
print(clf.fit(train_vectors, train_labels))  
print("train", clf.score(train_vectors, train_labels))
print("development", clf.score(development_vectors, development_labels))
print("test", clf.score(test_vectors, test_labels))