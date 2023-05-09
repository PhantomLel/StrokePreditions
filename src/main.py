import pandas as pd
import pymrmr

def mrmr(train, test):
    return pymrmr.mRMR(train, "MIQ", 50)

train_data, test_data = [], []
radiomics = pd.read_csv("data/radiomics.csv")
fold_alloc = pd.read_csv("data/Fold_alloc.csv")
baseline = pd.read_csv("data/clinical.csv")
train_test = pd.read_csv("data/train_tests.csv")


kfolds = [[] for i in range(5)]

# put each subject into a fold
for fold in fold_alloc:
    kfolds[int(fold.get("fold"))-1].append(int(fold.get("ID")))



