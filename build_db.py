# This file adds foreign keys for each voter to its precinct, then
# make sure that the sum of the count in table vm_precinct equals
# the sum of the votes from the individual voters

from vm.models import *

def add_foreign_key():
    for individual in Wasco.objects.all():
        for precinct in Precinct.objects.all():
            # Found a match
            if individual.sprecinctid == precinct.name.lstrip("0"):
                individual.precinct_id = precinct
                individual.save()
                break

def sum_votes():
    for precinct in Precinct.objects.all():
        voters = precinct.wasco_set.all()
        count_yes = 0
        count_no = 0
        count_yardsign = 0
        count_undecided = 0
        for voter in voters:
            if voter.voter_response is not None:
                if voter.voter_response == 1:
                    count_yes += 1
                elif voter.voter_response == -1:
                    count_no += 1
                elif voter.voter_response == 0:
                    count_undecided += 1
            if voter.yardsign:
                if voter.yardsign == 1:
                    count_yardsign += 1

        precinct.count_yes = count_yes
        precinct.count_no = count_no
        precinct.count_undecided = count_undecided
        precinct.count_yardsign = count_yardsign
        precinct.save()

if __name__ == "__main__":
    add_foreign_key()
    sum_votes()
