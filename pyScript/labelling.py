import pandas as pd
import sys, json, numpy as np
import csv
import category_encoders as ce
import os

#Methods to label categorical data

def encodingLabel(df, column, filepath):
    for col in column:
        df[col] = df[col].astype("category")
        df[col] = df[col].cat.codes
    df.to_csv(filepath, index=False)
    return df

def oneHotEncoding(df, column, filepath):
    for col in column:
        df = pd.get_dummies(df, columns=[col], prefix=[col])
    df.to_csv(filepath, index=False)
    return df

def binaryEncoding(df, column, filepath):
    for col in column:
        encoder = ce.BinaryEncoder(cols=[col])
        df = encoder.fit_transform(df)
    df.to_csv(filepath, index=False)
    return df

def main():
    #input buffer 
    lines = sys.stdin.readlines()
    lines = json.loads(lines[0])
    
    filePath = lines["filePath"]
    column = lines["column"]
    typeOfLabelling = lines["type"]

    #dataframe input
    df = pd.read_csv(filePath)
    
    if typeOfLabelling == "findNReplace":
        print("1")
    elif typeOfLabelling == "encodingLabel":
        df = encodingLabel(df, column, filePath)
    elif typeOfLabelling == "oneHotEncoding":
        df = oneHotEncoding(df, column, filePath)
    elif typeOfLabelling == "binaryEncoding":
        df =  binaryEncoding(df, column, filePath)

if __name__ == "__main__":
    main()