import ctypes
import os
import _ctypes
import sys

UCT_LoginCfm = ctypes.CFUNCTYPE(None, ctypes.c_char, ctypes.c_char_p, ctypes.c_ulong
, ctypes.c_uint, ctypes.c_ushort
, ctypes.c_uint, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte) )

UCT_SCallMoCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p
, ctypes.c_uint, ctypes.c_int
, ctypes.c_int )

UCT_SCallMtInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p
, ctypes.c_int, ctypes.c_char_p
, ctypes.c_char_p, ctypes.c_uint, ctypes.c_int)


UCT_SCallRelInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_ushort, ctypes.c_int)

UCT_LocalRingReq = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_ubyte)

UCT_LocalRingStop = ctypes.CFUNCTYPE(ctypes.c_int)


UCT_GCallMoCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char, ctypes.c_uint, ctypes.c_int)

UCT_GCallMtInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p , ctypes.c_uint, ctypes.c_int)

UCT_GCallPressCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char, ctypes.c_int )

UCT_GCallPressRelCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char, ctypes.c_int )

UCT_GCallPressChagInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char,ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int )

UCT_GCallRelInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char,ctypes.c_char_p, ctypes.c_int )

UCT_UctGDataInd = ctypes.CFUNCTYPE(ctypes.c_int)

UCT_QueryGDataInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char)

UCT_QueryUDataInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char)

UCT_GetUctGrpDataFormIdx = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p)

UCT_GetUctGrpBaseInfoFormIdx = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p , ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte))

UCT_ImDataInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p ,ctypes.c_char_p,  ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int)

UCT_ImDataColorInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p ,ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,  ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int)

UCT_MissingCallPromptInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p ,ctypes.c_char_p, ctypes.c_int, ctypes.c_int
, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,  ctypes.c_char_p, ctypes.c_char_p,ctypes.c_char_p,ctypes.c_char_p)

UCT_SpecificQueryResponse = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int
, ctypes.c_char_p ,ctypes.c_char_p, ctypes.c_int, ctypes.c_int
, ctypes.c_int, ctypes.c_int,  ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte)
,  ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int,  ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int)

UCT_RecordQueryResponse = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,  ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte)
, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int
,  ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte),  ctypes.POINTER(ctypes.c_ubyte)
, ctypes.c_int,  ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int)

UCT_ScallMtVideoMonitorInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int)

UCT_SCallPhoneVideoTransferInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int,ctypes.c_char_p, ctypes.c_int)

UCT_MsgVideoTransferInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)

UCT_PhoneVideoQueData = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)
, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

UCT_PhoneVideoCfgData = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int
, ctypes.c_int, ctypes.c_int)

UCT_PhoneVideoClose = ctypes.CFUNCTYPE(ctypes.c_int)

UCT_PhoneGetNetStatus = ctypes.CFUNCTYPE(ctypes.c_int)

UCT_Printf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

pFunc_ut_PtzControl = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p,ctypes.c_int)

UCT_SCallMtInterceptionInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p,ctypes.c_int)

UCT_PhoneVideoQueGpsData = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int),ctypes.POINTER(ctypes.c_int),ctypes.POINTER(ctypes.c_int))

UCT_PhoneVideoCfgGpsData = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char, ctypes.c_char, ctypes.c_int,ctypes.c_int,ctypes.c_int)

UCT_PhoneVideoQueSaveData = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int))

UCT_PhoneVideoCfgSaveData = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char, ctypes.c_int)

UCT_PhoneManageLogFile = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

UCT_PhoneOutFtpLogFile = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_ushort, ctypes.c_uint, ctypes.c_ushort, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)

UCT_PhoneComment = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p,ctypes.c_char_p, ctypes.POINTER(ctypes.c_int))

UCT_LoginScanState = ctypes.CFUNCTYPE(None, ctypes.c_char, ctypes.c_int)

UCT_ModifyPwdCfm = ctypes.CFUNCTYPE(None, ctypes.c_char)

UCT_SCallNotify = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int)


class User(ctypes.Structure):
    _fields_ = [
        ("ucUserDn", ctypes.c_ubyte * 32),
        ("ucUserName_Desc", ctypes.c_ubyte * 90),
        ("ucUserIconName", ctypes.c_ubyte * 32),
        ("ucUserType", ctypes.c_ubyte),
        ("ucUserState", ctypes.c_ubyte),
    ]

class TmpGrpUserDataInd(ctypes.Structure):
    _fields_ = [
        ("ucRet", ctypes.c_ubyte),
        ("ucGrpDn", ctypes.c_ubyte * 32),
        ("ucGrpName", ctypes.c_ubyte * 128),
        ("ucIconName", ctypes.c_ubyte * 32),
        ("ucGrpStat", ctypes.c_ubyte),
        ("usGrpUserNum", ctypes.c_ushort),
        ("grpUsers", User*100),
    ]

UCT_TmpGrpQueAckInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(TmpGrpUserDataInd))

UCT_SVideoMoCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_int)

UCT_SVideoMtInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int)

UCT_SVideoMtIndEx = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p)

UCT_SVideoRelInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_ushort, ctypes.c_int)

UCT_VideoStatInfo = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,ctypes.c_int, ctypes.c_int,ctypes.c_int)


UCT_GVideoMoCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_int)

UCT_GVideoRelInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_ushort, ctypes.c_int)

UCT_GroupInfoNotify = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_int)

UCT_OmOpenAccuntCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p)

UCT_OmModifyPwdCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p)

UCT_OmModifyAvatarCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p)

UCT_OmModifyUserCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p)

UCT_CreateGroupCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p,ctypes.c_char_p)

UCT_DeleteGroupCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p,ctypes.c_char_p)

UCT_QuitGroupCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p,ctypes.c_char_p)

UCT_ModifyGroupCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p,ctypes.c_char_p)

UCT_InviteGroupCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p,ctypes.c_char_p)

UCT_KickOutGroupCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p,ctypes.c_char_p)

UCT_JoinGroupCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p,ctypes.c_char_p)

UCT_SetDataTransportInfo = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int,ctypes.c_int
,ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p,ctypes.c_char_p, ctypes.c_char_p)

UCT_P2P_Eastone = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p
, ctypes.c_int,ctypes.c_int, ctypes.c_int,ctypes.c_int, ctypes.c_int
, ctypes.c_char_p)

UCT_P2P_EastoneCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p
, ctypes.c_int,ctypes.c_int, ctypes.c_int)

UCT_P2MP_Eastone = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p,ctypes.c_char_p
, ctypes.c_int,ctypes.c_int, ctypes.c_int,ctypes.c_int, ctypes.c_int
, ctypes.c_char_p)

UCT_P2MP_EastoneCfm = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p
, ctypes.c_int,ctypes.c_int, ctypes.c_int)

UCT_MSG_EastoneResult = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,  ctypes.c_char_p)

UCT_SpeakerInd = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,  ctypes.c_int)

UCT_CallSuspend = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,  ctypes.c_int)

UCT_CallActive = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

UCT_MqNotify = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p)

UCT_Notify = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)

UCT_OperateResult = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)


class UCT_CALLBACKV1_s(ctypes.Structure):
    _fields_ = [
        ("fLoginCfm", UCT_LoginCfm),
        ("fSCallMoCfm", UCT_SCallMoCfm),
        ("fSCallMtInd", UCT_SCallMtInd),
        ("fSCallRelInd", UCT_SCallRelInd),

        ("fLocalRingReq", UCT_LocalRingReq),
        ("fLocalRingStop", UCT_LocalRingStop),

        ("fGCallMoCfm", UCT_GCallMoCfm),
        ("fGCallMtInd", UCT_GCallMtInd),
        ("fGCallPressCfm", UCT_GCallPressCfm),
        ("fGCallPressRelCfm", UCT_GCallPressRelCfm),
        ("fGCallPressChagInd", UCT_GCallPressChagInd),
        ("fGCallRelInd", UCT_GCallRelInd),

        ("fUctGDataInd", UCT_UctGDataInd),
        ("fQueryGdataInd", UCT_QueryGDataInd),
        ("fQueryUdataInd", UCT_QueryUDataInd),

        ("fGetUctGrpDataFormIdx", UCT_GetUctGrpDataFormIdx),
        ("fGetUctGrpBaseInfoFormIdx", UCT_GetUctGrpBaseInfoFormIdx),

        ("fImDataInd", UCT_ImDataInd),
        ("fImDataColorInd", UCT_ImDataColorInd),
        ("fMissCallPromptInd", UCT_MissingCallPromptInd),

        ("fSpecificQueryResponse", UCT_SpecificQueryResponse),

        ("fRecordQueryResponse", UCT_RecordQueryResponse),

        ("fScallMtVideoMonitorInd", UCT_ScallMtVideoMonitorInd),
        ("fScallMtVideoTransferInd", UCT_SCallPhoneVideoTransferInd),
        ("fMsgVideoTransferInd", UCT_MsgVideoTransferInd),

        ("fPhoneVideoQueData", UCT_PhoneVideoQueData),
        ("fPhoneVideoCfgData", UCT_PhoneVideoCfgData),
        ("fPhoneVideoClose", UCT_PhoneVideoClose),

        ("fPhoneGetNetStatus", UCT_PhoneGetNetStatus),
        ("fPrintf", UCT_Printf),

        ("f_ut_PtzControlReq", pFunc_ut_PtzControl),
        ("fSCallMtInterceptionInd", UCT_SCallMtInterceptionInd),

        ("fPhoneVideoQueGpsData", UCT_PhoneVideoQueGpsData),
        ("fPhoneVideoCfgGpsData", UCT_PhoneVideoCfgGpsData),

        ("fPhoneVideoQueSaveData", UCT_PhoneVideoQueSaveData),
        ("fPhoneVideoCfgSaveData", UCT_PhoneVideoCfgSaveData),

        ("fPhoneManageLogFile", UCT_PhoneManageLogFile),
        ("fPhoneOutFtpLogFile", UCT_PhoneOutFtpLogFile),

        ("fPhoneComment", UCT_PhoneComment),

        ("fPhoneLoginScanState", UCT_LoginScanState),

        ("fPwdCfm", UCT_ModifyPwdCfm),

        ("fCallNotify", UCT_SCallNotify),

        ("fTmpGrpQueAckInd", UCT_TmpGrpQueAckInd),

        ("fSVideoMoCfm", UCT_SVideoMoCfm),

        ("fSVideoMtInd", UCT_SVideoMtInd),

        ("fSVideoMtIndEx", UCT_SVideoMtIndEx),
        ("fSVideoRelInd", UCT_SVideoRelInd),
        ("fVideoStatInfo", UCT_VideoStatInfo),

        ("fGVideoMoCfm", UCT_GVideoMoCfm),
        ("fGVideoRelInd", UCT_GVideoRelInd),
        ("fGroupInfoNotify", UCT_GroupInfoNotify),

        ("fOpenAccuntCfm", UCT_OmOpenAccuntCfm),
        ("fModifyPwdCfm", UCT_OmModifyPwdCfm),
        ("fModifyAvatarCfm", UCT_OmModifyAvatarCfm),
        ("fModifyUserCfm", UCT_OmModifyUserCfm),

        ("fCreateGroupCfm", UCT_CreateGroupCfm),
        ("fDeleteGroupCfm", UCT_DeleteGroupCfm),
        ("fQuitGroupCfm", UCT_QuitGroupCfm),

        ("fModifyGroupCfm", UCT_ModifyGroupCfm),
        ("fInviteGroupCfm", UCT_InviteGroupCfm),
        ("fKickOutGroupCfm", UCT_KickOutGroupCfm),
        ("fJoinGroupCfm", UCT_JoinGroupCfm),

        ("fSetDataTransportInfo", UCT_SetDataTransportInfo),

        ("fP2P_Eastone", UCT_P2P_Eastone),
        ("fP2P_EastoneCfm", UCT_P2P_EastoneCfm),

        ("fP2MP_Eastone", UCT_P2MP_Eastone),

        ("fP2MP_EastoneCfm", UCT_P2MP_EastoneCfm),

        ("fUCT_MSG_EastoneResult", UCT_MSG_EastoneResult),

        ("fSpeakerInd", UCT_SpeakerInd),

        ("fCallSuspend", UCT_CallSuspend),

        ("fCallActive", UCT_CallActive),

        ("fMqNotify", UCT_MqNotify),

        ("fNotify", UCT_Notify),

        ("fOperateResult", UCT_OperateResult),

        ("__tmp", ctypes.c_void_p * 128),

    ]

CUR_PATH = os.path.dirname(__file__)
dllPath = os.path.join(CUR_PATH, "SDK\\uct.dll")
print(dllPath)

pDll = ctypes.WinDLL(dllPath)
print(pDll)

def _callback(para):
    obj = para.__getitem__(0)
    print(obj)

callback = UCT_CALLBACKV1_s()
callback.fLoginCfm = UCT_LoginCfm(_callback)
ret = pDll.UCT_Start(ctypes.byref(callback))

print(ret)

pDll.UCT_Set_Device_Type(1,1)

ret = pDll.UCT_LoginReq('6300001',3, '6300001', '58.248.254.110')

os.system("pause")

pDll.UCT_End()