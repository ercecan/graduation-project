from models.constraints import MaxCreditFuturePlanConstraint, MinCreditFuturePlanConstraint, MajorFuturePlanConstraint, YearFuturePlanConstraint, PrerequisitiesFuturePlanConstraint

def get_ITU_constraints():
    return [MajorFuturePlanConstraint(), YearFuturePlanConstraint(), PrerequisitiesFuturePlanConstraint(), MaxCreditFuturePlanConstraint()]