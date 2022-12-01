########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, Paul Anderson, Isaac Dunn, Erick Morales, Torin Bolander
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

# you may need to put something here...
controls = {
    "Secret": 4,
    "Privileged": 3,
    "Confidential": 2,
    "Public": 1}

def securityConditionRead(assetControl, subjectControl):
    return controls[subjectControl] >= controls[assetControl]

def securityConditionWrite(assetControl, subjectControl):
    return controls[subjectControl] <= controls[assetControl]