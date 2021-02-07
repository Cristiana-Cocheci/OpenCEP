from test.BasicTests import *
from test.TreeConstructionTests import *
from test.KC_tests import *
from test.NegationTests import *
from test.PolicyTests import *
from test.MultiPattern_tests import *
from test.StorageTests import *
from test.ParallelTests import *
from test.Algorithm3Test import *
from test.UnitTests.test_storage import run_storage_tests
from stream.Stream import *


runTest.over_all_time = 0

# # basic functionality tests
# oneArgumentsearchTest()
# simplePatternSearchTest()
# googleAscendPatternSearchTest()
# amazonInstablePatternSearchTest()
# msftDrivRacePatternSearchTest()
# googleIncreasePatternSearchTest()
# amazonSpecificPatternSearchTest()
# googleAmazonLowPatternSearchTest()
# nonsensePatternSearchTest()
# hierarchyPatternSearchTest()
# duplicateEventTypeTest()
#
# # # tree plan generation algorithms
# arrivalRatesPatternSearchTest()
# nonFrequencyPatternSearchTest()
# frequencyPatternSearchTest()
# nonFrequencyPatternSearch2Test()
# frequencyPatternSearch2Test()
# nonFrequencyPatternSearch3Test()
# frequencyPatternSearch3Test()
# nonFrequencyPatternSearch4Test()
# frequencyPatternSearch4Test()
# nonFrequencyPatternSearch5Test()
# frequencyPatternSearch5Test()
# frequencyPatternSearch6Test()
# greedyPatternSearchTest()
# iiRandomPatternSearchTest()
# iiRandom2PatternSearchTest()
# iiGreedyPatternSearchTest()
# iiGreedy2PatternSearchTest()
# zStreamOrdPatternSearchTest()
# zStreamPatternSearchTest()
# dpBPatternSearchTest()
# dpLdPatternSearchTest()
# nonFrequencyTailoredPatternSearchTest()
# frequencyTailoredPatternSearchTest()
# #
# # # tree structure tests - CEP object only created not used
# structuralTest1()
# structuralTest2()
# structuralTest3()
# structuralTest4()
# structuralTest5()
# structuralTest6()
# structuralTest7()
#
# # # Kleene closure tests
# MinMax_0_TestKleeneClosure()
# MinMax_1_TestKleeneClosure()
# MinMax_2_TestKleeneClosure()
# #
# #
# # # Kleene Condition tests
# KC_AND_IndexCondition_01()
# KC_AND_IndexCondition_02()
# KC_AND_NegOffSet_01()
# KC_AllValues()
# KC_Specific_Value()
# KC_Mixed()
# KC_Condition_Failure_01()
# KC_Condition_Failure_02()
# KC_Condition_Failure_03()
# # #
# # # negation tests
# simpleNotTest()
# multipleNotInTheMiddleTest()
# oneNotAtTheBeginningTest()
# multipleNotAtTheBeginningTest()
# oneNotAtTheEndTest()
# multipleNotAtTheEndTest()
# multipleNotBeginAndEndTest()
# testWithMultipleNotAtBeginningMiddleEnd()
#
# # # # consumption policies tests
# singleType1PolicyPatternSearchTest()
# singleType2PolicyPatternSearchTest()
# contiguousPolicyPatternSearchTest()
# contiguousPolicy2PatternSearchTest()
# freezePolicyPatternSearchTest()
# freezePolicy2PatternSearchTest()
# #
# # # storage tests
# sortedStorageTest()
# run_storage_tests()
#
# # # multi-pattern tests
# # # first approach: sharing leaves
# leafIsRoot()
# distinctPatterns()
# threePatternsTest()
# samePatternDifferentTimeStamps()
# rootAndInner()
# # # #
# # # second approach: sharing equivalent subtrees
# onePatternIncludesOther()
# samePatternSharingRoot()
# severalPatternShareSubtree()
# notInTheBeginningShare()
# multipleParentsForInternalNode()


#
# # benchmarks
# if INCLUDE_BENCHMARKS:
#     sortedStorageBenchMarkTest()
#
#
# # Twitter tests
# if INCLUDE_TWITTER:
#     try:
#         from TwitterTest import run_twitter_sanity_check
#         run_twitter_sanity_check()
#     except ImportError:  # tweepy might not be installed
#         pass
#
# # Data parallel tests
# Algorithm 1 - Hirzel
# oneArgumentsearchTestAlgorithm1()
# amazonSpecificPatternSearchTestAlgoritm1()
# fbNegPatternSearchTestAlgorithm1()
# fbEqualToApple1PatternSearchTestAlgorithm1()
# fbEqualToApple2PatternSearchTestAlgorithm1()
# appleOpenToCloseTestAlgoritm1()
# applePeakToOpenTestAlgoritm1()
# KCgoogleTestAlgorithm1()
# KCequalsPatternSearchTestAlgorithm1()
multyPatternAlgorithm1()

#
# # # Algorithm 2 - Rip
# oneArgumentsearchTestAlgorithm2()
# simplePatternSearchTestAlgorithm2()
# googleAscendPatternSearchTestAlgorithm2()
# amazonInstablePatternSearchTestAlgorithm2()
# msftDrivRacePatternSearchTestAlgorithm2()
# googleIncreasePatternSearchTestAlgorithm2()
# amazonSpecificPatternSearchTestAlgorithm2()
# googleAmazonLowPatternSearchTestAlgorithm2()
# nonsensePatternSearchTestAlgorithm2()
# hierarchyPatternSearchTestAlgorithm2()
# duplicateEventTypeTestAlgorithm2()
# structuralTest1Algorithm2()
# structuralTest2Algorithm2()
# structuralTest3Algorithm2()
# structuralTest4Algorithm2()
# structuralTest5Algorithm2()
# structuralTest6Algorithm2()
# structuralTest7Algorithm2()
# MinMax_0_TestKleeneClosureAlgorithm2()
# MinMax_1_TestKleeneClosureAlgorithm2()
# MinMax_2_TestKleeneClosureAlgorithm2()
# KC_AND_IndexCondition_01_Algorithm2()
# KC_AND_IndexCondition_02_Algorithm2()
# KC_AND_NegOffSet_01_Algorithm2()
# KC_AllValuesAlgorithm2()
# KC_Specific_ValueAlgorithm2()
# KC_MixedAlgorithm2()
# leafIsRootAlgorithm2()
# distinctPatternsAlgorithm2()
# threePatternsTestAlgorithm2()
# rootAndInnerAlgorithm2()
# samePatternDifferentTimeStampsAlgorithm2()
# onePatternIncludesOtherAlgorithm2()
# samePatternSharingRootAlgorithm2()
# multipleParentsForInternalNodeAlgorithm2()
# simpleNotTestAlgorithm2()
# multipleNotInTheMiddleTestAlgorithm2()
# singleType1PolicyPatternSearchTestAlgorithm2()
# singleType2PolicyPatternSearchTestAlgorithm2()
# contiguousPolicyPatternSearchTestAlgorithm2()
# contiguousPolicy2PatternSearchTestAlgorithm2()
# freezePolicyPatternSearchTestAlgorithm2()
# freezePolicy2PatternSearchTestAlgorithm2()
# sortedStorageTestAlgorithm2()
#
#
# # ######Basic functionality tests for Algorithm3
# oneArgumentsearchTestAlgorithm3()
# simplePatternSearchTestAlgorithm3()
# googleAmazonLowPatternSearchTestAlgorithm3()
# nonsensePatternSearchTestAlgorithm3()
# duplicateEventTypeTestAlgorithm3()
# amazonSpecificPatternSearchTestAlgorithm3()
# googleAscendPatternSearchTestAlgorithm3()
# amazonInstablePatternSearchTestAlgorithm3()
# msftDrivRacePatternSearchTestAlgorithm3()
# googleIncreasePatternSearchTestAlgorithm3()
# hierarchyPatternSearchTestAlgorithm3()


# # tree plan generation algorithms for Algorithm3
# arrivalRatesPatternSearchTestAlgorithm3()
# frequencyPatternSearchTestAlgorithm3()
# nonFrequencyPatternSearchTestAlgorithm3()
# nonFrequencyPatternSearch3TestAlgorithm3()
# frequencyPatternSearch3TestAlgorithm3()
# nonFrequencyPatternSearch2TestAlgorithm3()
# frequencyPatternSearch2TestAlgorithm3()
# nonFrequencyPatternSearch4TestAlgorithm3()
# frequencyPatternSearch4TestAlgorithm3()
# greedyPatternSearchTestAlgorithm3()
# iiRandomPatternSearchTestAlgorithm3()
# iiRandom2PatternSearchTestAlgorithm3()
# iiGreedyPatternSearchTestAlgorithm3()
# iiGreedy2PatternSearchTestAlgorithm3()
# zStreamOrdPatternSearchTestAlgorithm3()
# zStreamPatternSearchTestAlgorithm3()
# dpBPatternSearchTestAlgorithm3()
# dpLdPatternSearchTestAlgorithm3()
# nonFrequencyTailoredPatternSearchTestAlgorithm3()
# frequencyTailoredPatternSearchTestAlgorithm3()
#
#
# # ### Kleene closure tests
# MinMax_0_TestKleeneClosureAlgorithm3()
# MinMax_2_TestKleeneClosureAlgorithm3()
#
#
# # # # consumption policies tests
# singleType1PolicyPatternSearchTestAlgorithm3()
# singleType2PolicyPatternSearchTestAlgorithm3()
# contiguousPolicyPatternSearchTestAlgorithm3()
# contiguousPolicy2PatternSearchTestAlgorithm3()
# freezePolicy2PatternSearchTestAlgorithm3()
#
# # storage tests
# sortedStorageTestAlgorithm3()
# #
# # # multi-pattern tests
# distinctPatternsAlgorithm3()
# samePatternDifferentTimeStampsAlgorithm3()
# rootAndInnerAlgorithm3()
# onePatternIncludesOtherAlgorithm3()
#
# print("Finished running all tests, overall time: %s" % runTest.over_all_time)
