'''
@author: Christian Wressnegger
'''

import os
import numpy as np
from sklearn.metrics import confusion_matrix, roc_auc_score

MY_DIR = os.path.dirname(os.path.abspath(__file__))
MY_DIR = os.path.join(MY_DIR, '../')

y, y_hat = np.random.randint(0, 2, 500), np.random.uniform(0, 1, 500)
thetas = np.linspace(0.1, 1, 10)

inputs = [(y, (y_hat>=t).astype(int), t) for t in thetas]
cms = [confusion_matrix(i[0], i[1]) for i in inputs]
TNs = [cm[0][0] for cm in cms]
FPs = [cm[0][1] for cm in cms]
FNs = [cm[1][0] for cm in cms]
TPs = [cm[1][1] for cm in cms]

TPRs = [tp/(tp+fn) for tp, fn in zip(TPs, FNs)]
FPRs = [fp/(fp+tn) for fp, tn in zip(FPs, TNs)]

TPR_test = [
    (y, y_hat, t, tpr) for t, tpr in zip(thetas, TPRs)
]

FPR_test = [
    (y, y_hat, t, fpr) for t, fpr in zip(thetas, FPRs)
]

AUC_test = (y, y_hat, roc_auc_score(y, y_hat))
