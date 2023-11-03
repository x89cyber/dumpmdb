#!/usr/bin/python3
import os
import subprocess

mdbfile = "backup.mdb"
tables = "acc_antiback,acc_door,acc_firstopen,acc_firstopen_emp,acc_holidays,acc_interlock,acc_levelset,acc_levelset_door_group,acc_linkageio,acc_map,acc_mapdoorpos,acc_morecardempgroup,acc_morecardgroup,acc_timeseg,acc_wiegandfmt,ACGroup,acholiday,ACTimeZones,action_log,AlarmLog,areaadmin,att_attreport,att_waitforprocessdata,attcalclog,attexception,AuditedExc,auth_group_permissions,auth_message,auth_permission,auth_user,auth_user_groups,auth_user_user_permissions,base_additiondata,base_appoption,base_basecode,base_datatranslation,base_operatortemplate,base_personaloption,base_strresource,base_strtranslation,base_systemoption,CHECKEXACT,CHECKINOUT,dbbackuplog,DEPARTMENTS,deptadmin,DeptUsedSchs,devcmds,devcmds_bak,django_content_type,django_session,EmOpLog,empitemdefine,EXCNOTES,FaceTemp,iclock_dstime,iclock_oplog,iclock_testdata,iclock_testdata_admin_area,iclock_testdata_admin_dept,LeaveClass,LeaveClass1,Machines,NUM_RUN,NUM_RUN_DEIL,operatecmds,personnel_area,personnel_cardtype,personnel_empchange,personnel_leavelog,ReportItem,SchClass,SECURITYDETAILS,ServerLog,SHIFT,TBKEY,TBSMSALLOT,TBSMSINFO,TEMPLATE,USER_OF_RUN,USER_SPEDAY,UserACMachines,UserACPrivilege,USERINFO,userinfo_attarea,UsersMachines,UserUpdates,worktable_groupmsg,worktable_instantmsg,worktable_msgtype,worktable_usrmsg,ZKAttendanceMonthStatistics,acc_levelset_emp,acc_morecardset,ACUnlockComb,AttParam,auth_group,AUTHDEVICE,base_option,dbapp_viewmodel,FingerVein,devlog,HOLIDAYS,personnel_issuecard,SystemLog,USER_TEMP_SCH,UserUsedSClasses,acc_monitor_log,OfflinePermitGroups,OfflinePermitUsers,OfflinePermitDoors,LossCard,TmpPermitGroups,TmpPermitUsers,TmpPermitDoors,ParamSet,acc_reader,acc_auxiliary,STD_WiegandFmt,CustomReport,ReportField,BioTemplate,FaceTempEx,FingerVeinEx,TEMPLATEEx"

tablelist = tables.split(",")
for table in tablelist:
    #get the number of records in the table
    result = subprocess.run(["mdb-count", mdbfile, table], capture_output=True)
    count = int(result.stdout.strip())
    #query records for tables that are not empty
    if (count > 0):
        print(f"[+] querying {count} records from table {table}")
        os.system("mdb-export backup.mdb " + table)
        print("")

print(f"[*] done processing {mdbfile}") 
