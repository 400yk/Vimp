# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Wasco.vote_response'
        db.add_column(u'Wasco', 'vote_response',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Wasco.yardsign'
        db.add_column(u'Wasco', 'yardsign',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Wasco.vote_response'
        db.delete_column(u'Wasco', 'vote_response')

        # Deleting field 'Wasco.yardsign'
        db.delete_column(u'Wasco', 'yardsign')


    models = {
        u'vm.wasco': {
            'Meta': {'object_name': 'Wasco', 'db_table': "u'Wasco'"},
            'dtbirthdate': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'dtBirthDate'", 'blank': 'True'}),
            'dtelectiondate1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'dtElectionDate1'", 'blank': 'True'}),
            'dtelectiondate2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'dtElectionDate2'", 'blank': 'True'}),
            'dtelectiondate3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'dtElectionDate3'", 'blank': 'True'}),
            'dtelectiondate4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'dtElectionDate4'", 'blank': 'True'}),
            'dtelectiondate5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'dtElectionDate5'", 'blank': 'True'}),
            'dtlastupdate_dt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'dtLastUpdate_dt'", 'blank': 'True'}),
            'dtorigregdate': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'dtOrigRegDate'", 'blank': 'True'}),
            'dtregdate': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'dtRegDate'", 'blank': 'True'}),
            'iduplicateidflag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'iDuplicateIDFlag'", 'blank': 'True'}),
            'isubdistrict_0': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'iSubDistrict_0'", 'blank': 'True'}),
            'isubdistrict_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'iSubDistrict_1'", 'blank': 'True'}),
            'isubdistrict_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'iSubDistrict_2'", 'blank': 'True'}),
            'isubdistrict_3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'iSubDistrict_3'", 'blank': 'True'}),
            'isubdistrict_4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'iSubDistrict_4'", 'blank': 'True'}),
            'isubdistrict_5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'iSubDistrict_5'", 'blank': 'True'}),
            'lvoteruniqueid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'lVoterUniqueID'"}),
            'saffnumber': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sAffNumber'", 'blank': 'True'}),
            'sbirthplace': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sBirthPlace'", 'blank': 'True'}),
            'sdistrictid_0': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sDistrictID_0'", 'blank': 'True'}),
            'sdistrictid_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sDistrictID_1'", 'blank': 'True'}),
            'sdistrictid_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sDistrictID_2'", 'blank': 'True'}),
            'sdistrictid_3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sDistrictID_3'", 'blank': 'True'}),
            'sdistrictid_4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sDistrictID_4'", 'blank': 'True'}),
            'sdistrictid_5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sDistrictID_5'", 'blank': 'True'}),
            'selectionabbr1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sElectionAbbr1'", 'blank': 'True'}),
            'selectionabbr2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sElectionAbbr2'", 'blank': 'True'}),
            'selectionabbr3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sElectionAbbr3'", 'blank': 'True'}),
            'selectionabbr4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sElectionAbbr4'", 'blank': 'True'}),
            'selectionabbr5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sElectionAbbr5'", 'blank': 'True'}),
            'selectypedesc1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sElecTypeDesc1'", 'blank': 'True'}),
            'selectypedesc2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sElecTypeDesc2'", 'blank': 'True'}),
            'selectypedesc3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sElecTypeDesc3'", 'blank': 'True'}),
            'selectypedesc4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sElecTypeDesc4'", 'blank': 'True'}),
            'selectypedesc5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sElecTypeDesc5'", 'blank': 'True'}),
            'sgender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sGender'", 'blank': 'True'}),
            'shousenum': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sHouseNum'", 'blank': 'True'}),
            'snamesuffix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sNameSuffix'", 'blank': 'True'}),
            'spartyabbr1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sPartyAbbr1'", 'blank': 'True'}),
            'spartyabbr2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sPartyAbbr2'", 'blank': 'True'}),
            'spartyabbr3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sPartyAbbr3'", 'blank': 'True'}),
            'spartyabbr4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sPartyAbbr4'", 'blank': 'True'}),
            'spartyabbr5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sPartyAbbr5'", 'blank': 'True'}),
            'spostdir': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sPostDir'", 'blank': 'True'}),
            'sprecinctid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sPrecinctID'", 'blank': 'True'}),
            'sprecinctportion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sPrecinctPortion'", 'blank': 'True'}),
            'spredir': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sPreDir'", 'blank': 'True'}),
            'ssitusstate': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sSitusState'", 'blank': 'True'}),
            'ssituszip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sSitusZip'", 'blank': 'True'}),
            'sstatuscode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sStatusCode'", 'blank': 'True'}),
            'sstreetsuffix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sStreetSuffix'", 'blank': 'True'}),
            'sunitabbr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sUnitAbbr'", 'blank': 'True'}),
            'sunitnum': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sUnitNum'", 'blank': 'True'}),
            'susercode1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sUserCode1'", 'blank': 'True'}),
            'susercode2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sUserCode2'", 'blank': 'True'}),
            'svotertitle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sVoterTitle'", 'blank': 'True'}),
            'svotingprecinct1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sVotingPrecinct1'", 'blank': 'True'}),
            'svotingprecinct2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sVotingPrecinct2'", 'blank': 'True'}),
            'svotingprecinct3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sVotingPrecinct3'", 'blank': 'True'}),
            'svotingprecinct4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sVotingPrecinct4'", 'blank': 'True'}),
            'svotingprecinct5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'sVotingPrecinct5'", 'blank': 'True'}),
            'szavstatusabbr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szAVStatusAbbr'", 'blank': 'True'}),
            'szavstatusdesc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szAVStatusDesc'", 'blank': 'True'}),
            'szcountedflag1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szCountedFlag1'", 'blank': 'True'}),
            'szcountedflag2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szCountedFlag2'", 'blank': 'True'}),
            'szcountedflag3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szCountedFlag3'", 'blank': 'True'}),
            'szcountedflag4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szCountedFlag4'", 'blank': 'True'}),
            'szcountedflag5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szCountedFlag5'", 'blank': 'True'}),
            'szdistrictname_0': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szDistrictName_0'", 'blank': 'True'}),
            'szdistrictname_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szDistrictName_1'", 'blank': 'True'}),
            'szdistrictname_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szDistrictName_2'", 'blank': 'True'}),
            'szdistrictname_3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szDistrictName_3'", 'blank': 'True'}),
            'szdistrictname_4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szDistrictName_4'", 'blank': 'True'}),
            'szdistrictname_5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szDistrictName_5'", 'blank': 'True'}),
            'szelectiondesc1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szElectionDesc1'", 'blank': 'True'}),
            'szelectiondesc2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szElectionDesc2'", 'blank': 'True'}),
            'szelectiondesc3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szElectionDesc3'", 'blank': 'True'}),
            'szelectiondesc4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szElectionDesc4'", 'blank': 'True'}),
            'szelectiondesc5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szElectionDesc5'", 'blank': 'True'}),
            'szemailaddress': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szEmailAddress'", 'blank': 'True'}),
            'szlanguagename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szLanguageName'", 'blank': 'True'}),
            'szmailaddress1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szMailAddress1'", 'blank': 'True'}),
            'szmailaddress2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szMailAddress2'", 'blank': 'True'}),
            'szmailaddress3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szMailAddress3'", 'blank': 'True'}),
            'szmailaddress4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szMailAddress4'", 'blank': 'True'}),
            'szmailzip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szMailZip'", 'blank': 'True'}),
            'sznamefirst': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szNameFirst'", 'blank': 'True'}),
            'sznamelast': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szNameLast'", 'blank': 'True'}),
            'sznamemiddle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szNameMiddle'", 'blank': 'True'}),
            'szpartyname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szPartyName'", 'blank': 'True'}),
            'szpartyname1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szPartyName1'", 'blank': 'True'}),
            'szpartyname2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szPartyName2'", 'blank': 'True'}),
            'szpartyname3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szPartyName3'", 'blank': 'True'}),
            'szpartyname4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szPartyName4'", 'blank': 'True'}),
            'szpartyname5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szPartyName5'", 'blank': 'True'}),
            'szphone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szPhone'", 'blank': 'True'}),
            'szprecinctname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szPrecinctName'", 'blank': 'True'}),
            'szsitusaddress': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szSitusAddress'", 'blank': 'True'}),
            'szsituscity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szSitusCity'", 'blank': 'True'}),
            'szstatevoterid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szStateVoterID'", 'blank': 'True'}),
            'szstatusreasondesc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szStatusReasonDesc'", 'blank': 'True'}),
            'szstreetname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szStreetName'", 'blank': 'True'}),
            'szvotingmethod1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szVotingMethod1'", 'blank': 'True'}),
            'szvotingmethod2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szVotingMethod2'", 'blank': 'True'}),
            'szvotingmethod3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szVotingMethod3'", 'blank': 'True'}),
            'szvotingmethod4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szVotingMethod4'", 'blank': 'True'}),
            'szvotingmethod5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'szVotingMethod5'", 'blank': 'True'}),
            'vote_response': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'yardsign': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['vm']