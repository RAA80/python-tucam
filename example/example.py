#! /usr/bin/env python
# -*- coding: utf-8 -*-

from tucam.camapi import TUCAM
from tucam.define import (TUCAM_CAPTURE_MODES, TUCAM_IDCAPA, TUCAM_IDINFO,
                          TUCAM_IDPROP, TUCAM_ROI_ATTR, TUCAM_TRGOUT_ATTR,
                          TUCAM_TRIGGER_ATTR, TUREG_TYPE)

with TUCAM() as cam:    # либо cam.TUCAM_Dev_Open() в начале и cam.TUCAM_Dev_Close() в конце
    info = cam.TUCAM_Dev_GetInfo(info_id=TUCAM_IDINFO.TUIDI_CAMERA_MODEL)
    print("TUCAM_Dev_GetInfo = {}".format(info))
    print("    nID           = {}".format(info.nID))
    print("    nValue        = {}".format(info.nValue))
    print("    pText         = {}".format(info.pText))
    print("    nTextSize     = {}".format(info.nTextSize))

    capa_attr = cam.TUCAM_Capa_GetAttr(attr_id=TUCAM_IDCAPA.TUIDC_RESOLUTION)
    print("TUCAM_Capa_GetAttr = {}".format(capa_attr))
    print("    idCapa         = {}".format(capa_attr.idCapa))
    print("    nValMin        = {}".format(capa_attr.nValMin))
    print("    nValMax        = {}".format(capa_attr.nValMax))
    print("    nValDft        = {}".format(capa_attr.nValDft))
    print("    nValStep       = {}".format(capa_attr.nValStep))

    print("TUCAM_Capa_GetValueText (TUIDC_RESOLUTION) = {}".format(cam.TUCAM_Capa_GetValueText(attr_id=TUCAM_IDCAPA.TUIDC_RESOLUTION)))
    bitofdepth = cam.TUCAM_Capa_GetValue(attr_id=TUCAM_IDCAPA.TUIDC_BITOFDEPTH)
    print("TUCAM_Capa_GetValue (TUIDC_BITOFDEPTH) = {}".format(bitofdepth))
    print("TUCAM_Capa_SetValue (TUIDC_BITOFDEPTH) = {}".format(cam.TUCAM_Capa_SetValue(attr_id=TUCAM_IDCAPA.TUIDC_BITOFDEPTH, value=bitofdepth)))

    prop_attr = cam.TUCAM_Prop_GetAttr(attr_id=TUCAM_IDPROP.TUIDP_EXPOSURETM)
    print("TUCAM_Prop_GetAttr (TUIDP_EXPOSURETM) = {}".format(prop_attr))
    print("    idProp       = {}".format(prop_attr.idProp))
    print("    nIdxChn      = {}".format(prop_attr.nIdxChn))
    print("    dbValMin     = {}".format(prop_attr.dbValMin))
    print("    dbValMax     = {}".format(prop_attr.dbValMax))
    print("    dbValDft     = {}".format(prop_attr.dbValDft))
    print("    dbValStep    = {}".format(prop_attr.dbValStep))

    print("TUCAM_Prop_GetValueText (TUIDP_GLOBALGAIN) = {}".format(cam.TUCAM_Prop_GetValueText(attr_id=TUCAM_IDPROP.TUIDP_GLOBALGAIN)))
    print("TUCAM_Prop_SetValue (TUIDP_EXPOSURETM) = {}".format(cam.TUCAM_Prop_SetValue(attr_id=TUCAM_IDPROP.TUIDP_EXPOSURETM, value=1000*prop_attr.dbValStep)))
    print("TUCAM_Prop_GetValue (TUIDP_EXPOSURETM) = {}".format(cam.TUCAM_Prop_GetValue(attr_id=TUCAM_IDPROP.TUIDP_EXPOSURETM)))

    trigger = cam.TUCAM_Cap_GetTrigger()
    print("TUCAM_Cap_GetTrigger = {}".format(trigger))
    print("    nTgrMode         = {}".format(trigger.nTgrMode))
    print("    nExpMode         = {}".format(trigger.nExpMode))
    print("    nEdgeMode        = {}".format(trigger.nEdgeMode))
    print("    nDelayTm         = {}".format(trigger.nDelayTm))
    print("    nFrames          = {}".format(trigger.nFrames))
    print("    nBufFrames       = {}".format(trigger.nBufFrames))

    trigger_ = TUCAM_TRIGGER_ATTR()
    trigger_.nTgrMode = trigger.nTgrMode
    trigger_.nExpMode = trigger.nExpMode
    trigger_.nEdgeMode = trigger.nEdgeMode
    trigger_.nFranDelayTmmes = trigger.nDelayTm
    trigger_.nFrames = trigger.nFrames
    trigger_.nBufFrames = trigger.nBufFrames
    print("TUCAM_Cap_SetTrigger = {}".format(cam.TUCAM_Cap_SetTrigger(trigger_)))

    # print("TUCAM_Cap_DoSoftwareTrigger = {}".format(cam.TUCAM_Cap_DoSoftwareTrigger()))

    trigger = cam.TUCAM_Cap_GetTriggerOut()
    print("TUCAM_Cap_GetTriggerOut = {}".format(trigger))
    print("    nTgrOutPort         = {}".format(trigger.nTgrOutPort))
    print("    nTgrOutMode         = {}".format(trigger.nTgrOutMode))
    print("    nEdgeMode           = {}".format(trigger.nEdgeMode))
    print("    nDelayTm            = {}".format(trigger.nDelayTm))
    print("    nWidth              = {}".format(trigger.nWidth))

    trigger_ = TUCAM_TRGOUT_ATTR()
    trigger_.nTgrOutPort = trigger.nTgrOutPort
    trigger_.nTgrOutMode = trigger.nTgrOutMode
    trigger_.nEdgeMode = trigger.nEdgeMode
    trigger_.nDelayTm = trigger.nDelayTm
    trigger_.nWidth = trigger.nWidth
    print("TUCAM_Cap_SetTriggerOut = {}".format(cam.TUCAM_Cap_SetTriggerOut(trigger_)))

    register = cam.TUCAM_Reg_Read(reg_id=TUREG_TYPE.TUREG_SN)
    print("TUCAM_Reg_Read = {}".format(register))
    # print("TUCAM_Reg_Write = {}".format(cam.TUCAM_Reg_Write(reg_id=TUREG_TYPE.TUREG_SN, value=register)))

    roi = TUCAM_ROI_ATTR()
    roi.bEnable = True
    roi.nHOffset = 0
    roi.nVOffset = 0
    roi.nWidth = 2048
    roi.nHeight = 2048
    print("TUCAM_Cap_SetROI = {}".format(cam.TUCAM_Cap_SetROI(roi)))

    roi_ = cam.TUCAM_Cap_GetROI()
    print("TUCAM_Cap_GetROI = {}".format(roi_))
    print("    bEnable      = {}".format(roi_.bEnable))
    print("    nHOffset     = {}".format(roi_.nHOffset))
    print("    nVOffset     = {}".format(roi_.nVOffset))
    print("    nWidth       = {}".format(roi_.nWidth))
    print("    nHeight      = {}".format(roi_.nHeight))

    print("TUCAM_Buf_Alloc = {}".format(cam.TUCAM_Buf_Alloc()))
    print("TUCAM_Cap_Start = {}".format(cam.TUCAM_Cap_Start(mode=TUCAM_CAPTURE_MODES.TUCCM_SEQUENCE)))

    # Write single screenshot

    print("TUCAM_Buf_WaitForFrame = {}".format(cam.TUCAM_Buf_WaitForFrame(timeout=500)))
    print("TUCAM_Buf_CopyFrame = {}".format(cam.TUCAM_Buf_CopyFrame()))
    print("TUCAM_File_SaveImage = {}".format(cam.TUCAM_File_SaveImage()))

    # Write video stream

    # print("TUCAM_Rec_Start = {}".format(cam.TUCAM_Rec_Start()))
    # for _ in range(100):
    #     cam.TUCAM_Buf_WaitForFrame(timeout=500)
    #     cam.TUCAM_Buf_CopyFrame()
    #     cam.TUCAM_Rec_AppendFrame()
    # print("TUCAM_Rec_Stop = {}".format(cam.TUCAM_Rec_Stop()))

    print("TUCAM_Buf_AbortWait = {}".format(cam.TUCAM_Buf_AbortWait()))
    print("TUCAM_Cap_Stop = {}".format(cam.TUCAM_Cap_Stop()))
    print("TUCAM_Buf_Release = {}".format(cam.TUCAM_Buf_Release()))
