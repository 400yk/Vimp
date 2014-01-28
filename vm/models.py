# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class Precinct(models.Model):
    name = models.CharField(max_length = 255, primary_key = True)
    coord_lat = models.FloatField(blank = True, null = True)
    coord_lng = models.FloatField(blank = True, null = True)
    coord_alt = models.FloatField(blank = True, null = True)
    area = models.FloatField(blank = True, null = True)
    population = models.IntegerField(blank = True, null = True)
    count_yes = models.IntegerField(blank = True, null = True)
    count_no = models.IntegerField(blank = True, null = True)
    count_undecided = models.IntegerField(blank = True, null = True)
    count_yardsign = models.IntegerField(blank = True, null = True)

    def __unicode__(self):
        return self.name

class Wasco(models.Model):
    lvoteruniqueid = models.IntegerField(db_column='lVoterUniqueID', primary_key=True) # Field name made lowercase.
    saffnumber = models.CharField(db_column='sAffNumber', max_length=255, blank=True) # Field name made lowercase.
    szstatevoterid = models.CharField(db_column='szStateVoterID', max_length=255, blank=True) # Field name made lowercase.
    svotertitle = models.CharField(db_column='sVoterTitle', max_length=255, blank=True) # Field name made lowercase.
    sznamelast = models.CharField(db_column='szNameLast', max_length=255, blank=True) # Field name made lowercase.
    sznamefirst = models.CharField(db_column='szNameFirst', max_length=255, blank=True) # Field name made lowercase.
    sznamemiddle = models.CharField(db_column='szNameMiddle', max_length=255, blank=True) # Field name made lowercase.
    snamesuffix = models.CharField(db_column='sNameSuffix', max_length=255, blank=True) # Field name made lowercase.
    sgender = models.CharField(db_column='sGender', max_length=255, blank=True) # Field name made lowercase.
    szsitusaddress = models.CharField(db_column='szSitusAddress', max_length=255, blank=True) # Field name made lowercase.
    szsituscity = models.CharField(db_column='szSitusCity', max_length=255, blank=True) # Field name made lowercase.
    ssitusstate = models.CharField(db_column='sSitusState', max_length=255, blank=True) # Field name made lowercase.
    ssituszip = models.CharField(db_column='sSitusZip', max_length=255, blank=True) # Field name made lowercase.
    shousenum = models.CharField(db_column='sHouseNum', max_length=255, blank=True) # Field name made lowercase.
    sunitabbr = models.CharField(db_column='sUnitAbbr', max_length=255, blank=True) # Field name made lowercase.
    sunitnum = models.CharField(db_column='sUnitNum', max_length=255, blank=True) # Field name made lowercase.
    szstreetname = models.CharField(db_column='szStreetName', max_length=255, blank=True) # Field name made lowercase.
    sstreetsuffix = models.CharField(db_column='sStreetSuffix', max_length=255, blank=True) # Field name made lowercase.
    spredir = models.CharField(db_column='sPreDir', max_length=255, blank=True) # Field name made lowercase.
    spostdir = models.CharField(db_column='sPostDir', max_length=255, blank=True) # Field name made lowercase.
    szmailaddress1 = models.CharField(db_column='szMailAddress1', max_length=255, blank=True) # Field name made lowercase.
    szmailaddress2 = models.CharField(db_column='szMailAddress2', max_length=255, blank=True) # Field name made lowercase.
    szmailaddress3 = models.CharField(db_column='szMailAddress3', max_length=255, blank=True) # Field name made lowercase.
    szmailaddress4 = models.CharField(db_column='szMailAddress4', max_length=255, blank=True) # Field name made lowercase.
    szmailzip = models.CharField(db_column='szMailZip', max_length=255, blank=True) # Field name made lowercase.
    szphone = models.CharField(db_column='szPhone', max_length=255, blank=True) # Field name made lowercase.
    szemailaddress = models.CharField(db_column='szEmailAddress', max_length=255, blank=True) # Field name made lowercase.
    dtbirthdate = models.CharField(db_column='dtBirthDate', max_length=255, blank=True) # Field name made lowercase.
    sbirthplace = models.CharField(db_column='sBirthPlace', max_length=255, blank=True) # Field name made lowercase.
    dtregdate = models.CharField(db_column='dtRegDate', max_length=255, blank=True) # Field name made lowercase.
    dtorigregdate = models.CharField(db_column='dtOrigRegDate', max_length=255, blank=True) # Field name made lowercase.
    dtlastupdate_dt = models.CharField(db_column='dtLastUpdate_dt', max_length=255, blank=True) # Field name made lowercase.
    sstatuscode = models.CharField(db_column='sStatusCode', max_length=255, blank=True) # Field name made lowercase.
    szstatusreasondesc = models.CharField(db_column='szStatusReasonDesc', max_length=255, blank=True) # Field name made lowercase.
    susercode1 = models.CharField(db_column='sUserCode1', max_length=255, blank=True) # Field name made lowercase.
    susercode2 = models.CharField(db_column='sUserCode2', max_length=255, blank=True) # Field name made lowercase.
    iduplicateidflag = models.CharField(db_column='iDuplicateIDFlag', max_length=255, blank=True) # Field name made lowercase.
    szlanguagename = models.CharField(db_column='szLanguageName', max_length=255, blank=True) # Field name made lowercase.
    szpartyname = models.CharField(db_column='szPartyName', max_length=255, blank=True) # Field name made lowercase.
    szavstatusabbr = models.CharField(db_column='szAVStatusAbbr', max_length=255, blank=True) # Field name made lowercase.
    szavstatusdesc = models.CharField(db_column='szAVStatusDesc', max_length=255, blank=True) # Field name made lowercase.
    szprecinctname = models.CharField(db_column='szPrecinctName', max_length=255, blank=True) # Field name made lowercase.
    sprecinctid = models.CharField(db_column='sPrecinctID', max_length=255, blank=True) # Field name made lowercase.
    sprecinctportion = models.CharField(db_column='sPrecinctPortion', max_length=255, blank=True) # Field name made lowercase.
    sdistrictid_0 = models.CharField(db_column='sDistrictID_0', max_length=255, blank=True) # Field name made lowercase.
    isubdistrict_0 = models.CharField(db_column='iSubDistrict_0', max_length=255, blank=True) # Field name made lowercase.
    szdistrictname_0 = models.CharField(db_column='szDistrictName_0', max_length=255, blank=True) # Field name made lowercase.
    sdistrictid_1 = models.CharField(db_column='sDistrictID_1', max_length=255, blank=True) # Field name made lowercase.
    isubdistrict_1 = models.CharField(db_column='iSubDistrict_1', max_length=255, blank=True) # Field name made lowercase.
    szdistrictname_1 = models.CharField(db_column='szDistrictName_1', max_length=255, blank=True) # Field name made lowercase.
    sdistrictid_2 = models.CharField(db_column='sDistrictID_2', max_length=255, blank=True) # Field name made lowercase.
    isubdistrict_2 = models.CharField(db_column='iSubDistrict_2', max_length=255, blank=True) # Field name made lowercase.
    szdistrictname_2 = models.CharField(db_column='szDistrictName_2', max_length=255, blank=True) # Field name made lowercase.
    sdistrictid_3 = models.CharField(db_column='sDistrictID_3', max_length=255, blank=True) # Field name made lowercase.
    isubdistrict_3 = models.CharField(db_column='iSubDistrict_3', max_length=255, blank=True) # Field name made lowercase.
    szdistrictname_3 = models.CharField(db_column='szDistrictName_3', max_length=255, blank=True) # Field name made lowercase.
    sdistrictid_4 = models.CharField(db_column='sDistrictID_4', max_length=255, blank=True) # Field name made lowercase.
    isubdistrict_4 = models.CharField(db_column='iSubDistrict_4', max_length=255, blank=True) # Field name made lowercase.
    szdistrictname_4 = models.CharField(db_column='szDistrictName_4', max_length=255, blank=True) # Field name made lowercase.
    sdistrictid_5 = models.CharField(db_column='sDistrictID_5', max_length=255, blank=True) # Field name made lowercase.
    isubdistrict_5 = models.CharField(db_column='iSubDistrict_5', max_length=255, blank=True) # Field name made lowercase.
    szdistrictname_5 = models.CharField(db_column='szDistrictName_5', max_length=255, blank=True) # Field name made lowercase.
    selectionabbr1 = models.CharField(db_column='sElectionAbbr1', max_length=255, blank=True) # Field name made lowercase.
    szelectiondesc1 = models.CharField(db_column='szElectionDesc1', max_length=255, blank=True) # Field name made lowercase.
    dtelectiondate1 = models.CharField(db_column='dtElectionDate1', max_length=255, blank=True) # Field name made lowercase.
    selectypedesc1 = models.CharField(db_column='sElecTypeDesc1', max_length=255, blank=True) # Field name made lowercase.
    svotingprecinct1 = models.CharField(db_column='sVotingPrecinct1', max_length=255, blank=True) # Field name made lowercase.
    szvotingmethod1 = models.CharField(db_column='szVotingMethod1', max_length=255, blank=True) # Field name made lowercase.
    spartyabbr1 = models.CharField(db_column='sPartyAbbr1', max_length=255, blank=True) # Field name made lowercase.
    szpartyname1 = models.CharField(db_column='szPartyName1', max_length=255, blank=True) # Field name made lowercase.
    szcountedflag1 = models.CharField(db_column='szCountedFlag1', max_length=255, blank=True) # Field name made lowercase.
    selectionabbr2 = models.CharField(db_column='sElectionAbbr2', max_length=255, blank=True) # Field name made lowercase.
    szelectiondesc2 = models.CharField(db_column='szElectionDesc2', max_length=255, blank=True) # Field name made lowercase.
    dtelectiondate2 = models.CharField(db_column='dtElectionDate2', max_length=255, blank=True) # Field name made lowercase.
    selectypedesc2 = models.CharField(db_column='sElecTypeDesc2', max_length=255, blank=True) # Field name made lowercase.
    svotingprecinct2 = models.CharField(db_column='sVotingPrecinct2', max_length=255, blank=True) # Field name made lowercase.
    szvotingmethod2 = models.CharField(db_column='szVotingMethod2', max_length=255, blank=True) # Field name made lowercase.
    spartyabbr2 = models.CharField(db_column='sPartyAbbr2', max_length=255, blank=True) # Field name made lowercase.
    szpartyname2 = models.CharField(db_column='szPartyName2', max_length=255, blank=True) # Field name made lowercase.
    szcountedflag2 = models.CharField(db_column='szCountedFlag2', max_length=255, blank=True) # Field name made lowercase.
    selectionabbr3 = models.CharField(db_column='sElectionAbbr3', max_length=255, blank=True) # Field name made lowercase.
    szelectiondesc3 = models.CharField(db_column='szElectionDesc3', max_length=255, blank=True) # Field name made lowercase.
    dtelectiondate3 = models.CharField(db_column='dtElectionDate3', max_length=255, blank=True) # Field name made lowercase.
    selectypedesc3 = models.CharField(db_column='sElecTypeDesc3', max_length=255, blank=True) # Field name made lowercase.
    svotingprecinct3 = models.CharField(db_column='sVotingPrecinct3', max_length=255, blank=True) # Field name made lowercase.
    szvotingmethod3 = models.CharField(db_column='szVotingMethod3', max_length=255, blank=True) # Field name made lowercase.
    spartyabbr3 = models.CharField(db_column='sPartyAbbr3', max_length=255, blank=True) # Field name made lowercase.
    szpartyname3 = models.CharField(db_column='szPartyName3', max_length=255, blank=True) # Field name made lowercase.
    szcountedflag3 = models.CharField(db_column='szCountedFlag3', max_length=255, blank=True) # Field name made lowercase.
    selectionabbr4 = models.CharField(db_column='sElectionAbbr4', max_length=255, blank=True) # Field name made lowercase.
    szelectiondesc4 = models.CharField(db_column='szElectionDesc4', max_length=255, blank=True) # Field name made lowercase.
    dtelectiondate4 = models.CharField(db_column='dtElectionDate4', max_length=255, blank=True) # Field name made lowercase.
    selectypedesc4 = models.CharField(db_column='sElecTypeDesc4', max_length=255, blank=True) # Field name made lowercase.
    svotingprecinct4 = models.CharField(db_column='sVotingPrecinct4', max_length=255, blank=True) # Field name made lowercase.
    szvotingmethod4 = models.CharField(db_column='szVotingMethod4', max_length=255, blank=True) # Field name made lowercase.
    spartyabbr4 = models.CharField(db_column='sPartyAbbr4', max_length=255, blank=True) # Field name made lowercase.
    szpartyname4 = models.CharField(db_column='szPartyName4', max_length=255, blank=True) # Field name made lowercase.
    szcountedflag4 = models.CharField(db_column='szCountedFlag4', max_length=255, blank=True) # Field name made lowercase.
    selectionabbr5 = models.CharField(db_column='sElectionAbbr5', max_length=255, blank=True) # Field name made lowercase.
    szelectiondesc5 = models.CharField(db_column='szElectionDesc5', max_length=255, blank=True) # Field name made lowercase.
    dtelectiondate5 = models.CharField(db_column='dtElectionDate5', max_length=255, blank=True) # Field name made lowercase.
    selectypedesc5 = models.CharField(db_column='sElecTypeDesc5', max_length=255, blank=True) # Field name made lowercase.
    svotingprecinct5 = models.CharField(db_column='sVotingPrecinct5', max_length=255, blank=True) # Field name made lowercase.
    szvotingmethod5 = models.CharField(db_column='szVotingMethod5', max_length=255, blank=True) # Field name made lowercase.
    spartyabbr5 = models.CharField(db_column='sPartyAbbr5', max_length=255, blank=True) # Field name made lowercase.
    szpartyname5 = models.CharField(db_column='szPartyName5', max_length=255, blank=True) # Field name made lowercase.
    szcountedflag5 = models.CharField(db_column='szCountedFlag5', max_length=255, blank=True) # Field name made lowercase.

    # 1 denotes yes, 0 denotes undecided, and -1 denotes no, if null, means no data
    voter_response = models.IntegerField(null = True)

    yardsign = models.NullBooleanField(null=True)
    time_response = models.DateTimeField(default = datetime.now, blank = True)
    precinct = models.ForeignKey(Precinct, null=True)

    def __unicode__(self):
        return self.sznamefirst + " " + self.sznamelast
    class Meta:
        db_table = 'Wasco'


