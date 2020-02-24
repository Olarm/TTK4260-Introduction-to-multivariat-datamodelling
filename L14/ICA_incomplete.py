import cv2
import matplotlib.pyplot as plt
import numpy as np

im1='4.jpg'
im2='5.jpg'
im2='ghasemi.jpg'
im1='damiano.jpg'
im2='frank.jpg'

# Function to show two images
def showTwoIm(im1, im2):
    plt.figure(figsize=(18, 8))
    plt.subplot(1,2,1)
    plt.imshow(im1,cmap='gray')
    plt.axis('off')
    plt.subplot(1,2,2)
    plt.imshow(im2,cmap='gray')
    plt.axis('off')
    plt.show()

# Original images
S1 = cv2.imread(im1,0)
S2 = cv2.imread(im2,0)

# Mixing images
w = np.array([[0.6, 0.4], [0.4, 0.6]])

X1 = w[0,0]*S1 + w[0,1]*S2
X2 = w[1,0]*S1 + w[1,1]*S2

#showTwoIm(X1, X2)

# Flatten the 2D X1 and X2 matrix into vectors and plot against each other

f1 = X1.flatten()
f2 = X2.flatten()

plt.scatter(f1, f2, s=0.5, alpha=0.5)
plt.show()

# make it a vector and center data around mean
M, N = X1.shape
x1 = X1.reshape(M*N, 1) 
x2 = X2.reshape(M*N, 1)

x1v = x1 - np.mean(x1) 
x2v = x2 - np.mean(x2)

#theta0 = FILL
numer = -2 * x1.T * x2
#denom = np.sum(x2**2 - x1**2)
#theta0 = 1/2 * np.arctan2(numer, denom)