### Model order selection and model validation

t (vertical) are scores
p (horizontal) are loadings

PCA:
Move the coordinate system to the center of the data
New origin computed from average of all data

The vector pointing from the new center to


SVD and the matrix multiplication and remultiplication is essentially normalization over and over to rotate a vector towards an eigenvector


#### Loss functions

 - linear |y - f|
 - quadratic |y - f|^2
 - Huber loss, piecewise function


#### bias - variance tradeoff
underfitting: high bias, low variance
overfitting: low bias, high variance

An overfitted line follows training data closely, this line varies more and will therefore have higher variance.
An underfitted line will be straighter and may therefore deviate alot from the dataset, this implies a bias.

### training / test / validation
Different conventions, wikipedia flips it, the importance is the principle

Training - variance
Test - Model order selection
Validation - MSE

#### Sample selection
Important to have enough training samples to build a stable and reliable model
Important to have enough test samples to to the model generalization capabilities

Few samples, not NOT do random sample selection, use algorithm (splitting ratio) to sample **examrelevant** motivating sample selection.

Higher order model requires more training data

Knowledge of the physical system may lead to requiring less data for training if the model can be estimated to a certain extent beforehand.

#### 
Use Stein (SURE) online
AIC offline
