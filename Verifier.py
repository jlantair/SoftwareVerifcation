import csv
import os.path
import bz2
import glob
from Verifier import os
import pandas as pd


class verifier:
    def __init__(self, name, cegar, predicateAbstraction, symbolicExecution, boundedModelChecking, kInduction, propertyDirectedReach, explicitValueAnalysis, numericalIntervalAnalysis, shapeAnalysis, seperationLogic, bitPreciseAnalysis, argBasedAnalysis, lazyAbstraction, interpolation, automataBasedAnalysis, concurrencySupport, rankingFunctions):
        self.name = name
        self.cegar = cegar
        self.predicateAbstraction = predicateAbstraction
        self.symbolicExecution = symbolicExecution
        self.boundedModelChecking = boundedModelChecking
        self.kInduction = kInduction
        self.propertyDirectedReach = propertyDirectedReach
        self.explicitValueAnalysis = explicitValueAnalysis
        self.numericalIntervalAnalysis = numericalIntervalAnalysis
        self.shapeAnalysis = shapeAnalysis
        self.seperationLogic = seperationLogic
        self.bitPreciseAnalysis = bitPreciseAnalysis
        self.argBasedAnalysis = argBasedAnalysis
        self.lazyAbstraction = lazyAbstraction
        self.interpolation = interpolation
        self.automataBasedAnalysis = automataBasedAnalysis
        self.concurrencySupport = concurrencySupport
        self.rankingFunctions = rankingFunctions

    def populateTestResults(self):
        print("hi")

file = pd.read_csv("Verifiers.csv", skipinitialspace=True)

verifierName = file.VerifierName
cegar = file.CEGAR
predicateAbstraction = file.PredicateAbstraction
symbolicExecution = file.SymbolicExecution
boundedModelChecking = file.BoundedModelChecking
kInduction = file.kInduction
propertyDirectedReach = file.PropertyDirectedReach
explicitValueAnalysis = file.ExplicitValueAnalysis
numericalIntervalAnalysis = file.NumericalIntervalAnalysis
shapeAnalysis = file.ShapeAnalysis
seperationLogic = file.SeperationLogic
bitPreciseAnalysis = file.BitPreciseAnalysis
argBasedAnalysis = file.ARGBasedAnalysis
lazyAbstraction = file.LazyAbstraction
interpolation = file.Interpolation
automataBasedAnalysis = file.AutomataBasedAnalysis
concurrencySupport = file.ConcurrencySupport
rankingFunctions = file.RankingFunctions

verifiers = []

for n, c, p, s, b, k, pr, e, num, sh, sep, bit, arg, l, i, a, con, r in zip(verifierName, cegar, predicateAbstraction, symbolicExecution, boundedModelChecking, kInduction, propertyDirectedReach, explicitValueAnalysis, numericalIntervalAnalysis, shapeAnalysis, seperationLogic, bitPreciseAnalysis, argBasedAnalysis, lazyAbstraction, interpolation, automataBasedAnalysis, concurrencySupport, rankingFunctions):
    verifiers.append(verifier(n, c, p, s, b, k, pr, e, num, sh, sep, bit, arg, l, i, a, con, r))
    
#Read in bz2

for b in glob.glob("TestResults\*.bz2"):
    print(b)
    #strip file name 
    #find 
   # bz_file = bz2.BZ2File(b)
    #line_list = bz_file.readlines()
    #verifier.add

#for v in verifiers:
 #   v.populateTestResults()

#Test storage in verifiers
for v in verifiers:
    print(v.name)

#Do some analytics on these verifiers 