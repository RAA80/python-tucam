#! /usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import numpy
import os
from ctypes import (CFUNCTYPE, POINTER, byref, c_char_p, c_double, c_int,
                    c_ubyte, c_uint, c_ushort, c_void_p, cast, cdll, pointer,
                    create_string_buffer)
from .define import (HDTUCAM, HDTUIMG, TUCAM_CALC_ROI_ATTR, TUCAM_CAPA_ATTR,
                     TUCAM_DRAW, TUCAM_DRAW_INIT, TUCAM_FILE_SAVE, TUCAM_FRAME,
                     TUCAM_FW_UPDATE, TUCAM_INIT, TUCAM_OPEN, TUCAM_PPROP_ATTR,
                     TUCAM_PROP_ATTR, TUCAM_RAWIMG_HEADER, TUCAM_REC_SAVE,
                     TUCAM_REG_RW, TUCAM_ROI_ATTR, TUCAM_TRGOUT_ATTR,
                     TUCAM_TRIGGER_ATTR, TUCAM_VALUE_INFO, TUCAM_VALUE_TEXT,
                     TUCAM_VPROP_ATTR, TUCAMRET, TUFRM_FORMATS, TUIMG_FORMATS,
                     TUIMG_OPEN)


def _load_lib(name):
    return cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "libs", name))


_lib = _load_lib("TUCam.dll")


class TUCAM_API(c_void_p):
    ''' Основной интерфейс для работы с устройствами '''

    _functions_ = {         # arg1 - return value, arg2+ - func arguments
        'TUCAM_Api_Init': CFUNCTYPE(c_uint, POINTER(TUCAM_INIT)),
        'TUCAM_Api_Uninit': CFUNCTYPE(c_uint),
        'TUCAM_Dev_Open': CFUNCTYPE(c_uint, POINTER(TUCAM_OPEN)),
        'TUCAM_Dev_Close': CFUNCTYPE(c_uint, HDTUCAM),
        'TUCAM_Dev_GetInfo': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_VALUE_INFO)),
        'TUCAM_Dev_GetInfoEx': CFUNCTYPE(c_uint, c_uint, POINTER(TUCAM_VALUE_INFO)),
        'TUCAM_Capa_GetAttr': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_CAPA_ATTR)),
        'TUCAM_Capa_GetValue': CFUNCTYPE(c_uint, HDTUCAM, c_int, POINTER(c_int)),
        'TUCAM_Capa_SetValue': CFUNCTYPE(c_uint, HDTUCAM, c_int, c_int),
        'TUCAM_Capa_GetValueText': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_VALUE_TEXT)),
        'TUCAM_Prop_GetAttr': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_PROP_ATTR)),
        'TUCAM_Prop_GetValue': CFUNCTYPE(c_uint, HDTUCAM, c_int, POINTER(c_double), c_int),
        'TUCAM_Prop_SetValue': CFUNCTYPE(c_uint, HDTUCAM, c_int, c_double, c_int),
        'TUCAM_Prop_GetValueText': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_VALUE_TEXT), c_int),
        'TUCAM_Buf_Alloc': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_FRAME)),
        'TUCAM_Buf_Release': CFUNCTYPE(c_uint, HDTUCAM),
        'TUCAM_Buf_AbortWait': CFUNCTYPE(c_uint, HDTUCAM),
        'TUCAM_Buf_WaitForFrame': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_FRAME), c_int),
        'TUCAM_Buf_CopyFrame': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_FRAME)),
        # 'TUCAM_Buf_DataCallBack': CFUNCTYPE(c_uint, HDTUCAM, BUFFER_CALLBACK, c_void_p),
        'TUCAM_Buf_GetData': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_RAWIMG_HEADER)),
        'TUCAM_Cap_SetROI': CFUNCTYPE(c_uint, HDTUCAM, TUCAM_ROI_ATTR),
        'TUCAM_Cap_GetROI': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_ROI_ATTR)),
        'TUCAM_Cap_SetTrigger': CFUNCTYPE(c_uint, HDTUCAM, TUCAM_TRIGGER_ATTR),
        'TUCAM_Cap_GetTrigger': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_TRIGGER_ATTR)),
        'TUCAM_Cap_DoSoftwareTrigger': CFUNCTYPE(c_uint, HDTUCAM),
        'TUCAM_Cap_SetTriggerOut': CFUNCTYPE(c_uint, HDTUCAM, TUCAM_TRGOUT_ATTR),
        'TUCAM_Cap_GetTriggerOut': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_TRGOUT_ATTR)),
        'TUCAM_Cap_Start': CFUNCTYPE(c_uint, HDTUCAM, c_uint),
        'TUCAM_Cap_Stop': CFUNCTYPE(c_uint, HDTUCAM),
        'TUCAM_File_SaveImage': CFUNCTYPE(c_uint, HDTUCAM, TUCAM_FILE_SAVE),
        'TUCAM_File_LoadProfiles': CFUNCTYPE(c_uint, HDTUCAM, c_char_p),
        'TUCAM_File_SaveProfiles': CFUNCTYPE(c_uint, HDTUCAM, c_char_p),
        'TUCAM_Rec_Start': CFUNCTYPE(c_uint, HDTUCAM, TUCAM_REC_SAVE),
        'TUCAM_Rec_AppendFrame': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_FRAME)),
        'TUCAM_Rec_Stop': CFUNCTYPE(c_uint, HDTUCAM),
        'TUIMG_File_Open': CFUNCTYPE(c_uint, POINTER(TUIMG_OPEN), POINTER(POINTER(TUCAM_FRAME))),
        'TUIMG_File_Close': CFUNCTYPE(c_uint, HDTUIMG),
        'TUCAM_Reg_Read': CFUNCTYPE(c_uint, HDTUCAM, TUCAM_REG_RW),
        'TUCAM_Reg_Write': CFUNCTYPE(c_uint, HDTUCAM, TUCAM_REG_RW),
        'TUCAM_Draw_Init': CFUNCTYPE(c_uint, HDTUCAM, TUCAM_DRAW_INIT),
        'TUCAM_Draw_Frame': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_DRAW)),
        'TUCAM_Draw_Uninit': CFUNCTYPE(c_uint, HDTUCAM),
        'TUCAM_Calc_SetROI': CFUNCTYPE(c_uint, HDTUCAM, TUCAM_CALC_ROI_ATTR),
        'TUCAM_Calc_GetROI': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_CALC_ROI_ATTR)),
        'TUCAM_Proc_Start': CFUNCTYPE(c_uint, HDTUCAM, c_int),
        'TUCAM_Proc_Stop': CFUNCTYPE(c_uint, HDTUCAM, TUCAM_FILE_SAVE),
        'TUCAM_Proc_AbortWait': CFUNCTYPE(c_uint, HDTUCAM),
        'TUCAM_Proc_UpdateFrame': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_FRAME)),
        'TUCAM_Proc_WaitForFrame': CFUNCTYPE(c_uint, HDTUCAM, POINTER(POINTER(TUCAM_FRAME))),
        'TUCAM_Proc_Prop_GetAttr': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_PPROP_ATTR)),
        'TUCAM_Proc_Prop_GetValue': CFUNCTYPE(c_uint, HDTUCAM, c_int, POINTER(c_double)),
        'TUCAM_Proc_Prop_SetValue': CFUNCTYPE(c_uint, HDTUCAM, c_int, c_double),
        'TUCAM_Proc_Prop_GetValueText': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_VALUE_TEXT)),
        'TUCAM_Vendor_Config': CFUNCTYPE(c_uint, HDTUCAM, c_uint),
        'TUCAM_Vendor_ConfigEx': CFUNCTYPE(c_uint, c_uint, c_uint),
        'TUCAM_Vendor_Update': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_FW_UPDATE)),
        'TUCAM_Vendor_Prop_GetAttr': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_VPROP_ATTR)),
        'TUCAM_Vendor_Prop_GetValue': CFUNCTYPE(c_uint, HDTUCAM, c_int, POINTER(c_double), c_int),
        'TUCAM_Vendor_Prop_SetValue': CFUNCTYPE(c_uint, HDTUCAM, c_int, c_double, c_int),
        'TUCAM_Vendor_Prop_GetValueText': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_VALUE_TEXT), c_int),
        'TUCAM_Vendor_ResetIndexFrame': CFUNCTYPE(c_uint, HDTUCAM),
        'TUCAM_Vendor_WaitForIndexFrame': CFUNCTYPE(c_uint, HDTUCAM, POINTER(TUCAM_FRAME)),
        'TUCAM_Buf_Attach': CFUNCTYPE(c_uint, HDTUCAM, POINTER(c_ubyte), c_uint),
        'TUCAM_Buf_Detach': CFUNCTYPE(c_uint, HDTUCAM),
        'TUCAM_Get_GrayValue': CFUNCTYPE(c_uint, HDTUCAM, c_int, c_int, POINTER(c_ushort)),
        'TUCAM_Index_GetColorTemperature': CFUNCTYPE(c_uint, HDTUCAM, c_int, c_int, c_int, POINTER(c_uint)),
        'TUCAM_Rec_SetAppendMode': CFUNCTYPE(c_uint, HDTUCAM, c_uint),
        'TUCAM_Proc_CopyFrame': CFUNCTYPE(c_uint, HDTUCAM, POINTER(POINTER(TUCAM_FRAME))),
        # 'TUCAM_Vendor_AFPlatform': CFUNCTYPE(c_uint, HDTUCAM, POINTER(NVILen)),
    }

    def __call__(self, *args):
        prototype = args[0]
        arguments = args[1:]

        ret = prototype((self.name, _lib))(*arguments)
        if ret != 1:
            raise Exception("Errorcode {:x} ({})".format(ret, TUCAMRET(ret).name))

        return True

    def __getattr__(self, name):
        self.name = name
        if name in self._functions_:
            return functools.partial(self.__call__, self._functions_[name])


class TUCAM(object):
    ''' Python wrapper for TUCAM library '''

    def __init__(self):
        self._hdtucam = None
        self._frame = None
        self._api = TUCAM_API()

        self.TUCAM_Api_Init()

    def __del__(self):
        self.TUCAM_Api_Uninit()

    def __enter__(self):
        if self.TUCAM_Dev_Open():
            return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._hdtucam is not None:
            self.TUCAM_Dev_Close()

    def TUCAM_Api_Init(self):
        ''' Initialization of TUCAM-API library includes binding of driver and
            initialization of some internal resources, which is used before
            calling the other interfaces. The whole program only needs to call once
        '''

        init_param = TUCAM_INIT()

        if self._api.TUCAM_Api_Init(byref(init_param)):
            return init_param

    def TUCAM_Api_Uninit(self):
        ''' Uninstallation of TUCAM-API library includes the release of driver
            binding and some internal resources. It will be called once when the
            entire program is ended
        '''

        return self._api.TUCAM_Api_Uninit()

    def TUCAM_Dev_Open(self):
        ''' Open the camera, the camera is in work mode after the call, which
            can respond to the calls of other interfaces. The camera should be
            ensured prior to that, that is, it should be after the initialization
            of calling TUCAM_Api_Init
        '''

        cam_open = TUCAM_OPEN()

        if self._api.TUCAM_Dev_Open(byref(cam_open)):
            self._hdtucam = cam_open.hIdxTUCam
            return cam_open

    def TUCAM_Dev_Close(self):
        ''' Close the camera and the camera is in standby mode after called, and
            does not respond to calls from other interfaces
        '''

        return self._api.TUCAM_Dev_Close(self._hdtucam)

    def TUCAM_Dev_GetInfo(self, info_id):
        ''' Obtain the related information of camera, such as a USB port type,
            camera product number, API version number, firmware version number,
            camera type, etc. The camera should be ensured prior to that, and
            make sure the camera is opened, that is, it should be done after
            calling TUCAM_Api_Init initialization and TUCAM_Api_Open
        '''

        info = TUCAM_VALUE_INFO()
        info.nID = info_id.value

        if self._api.TUCAM_Dev_GetInfo(self._hdtucam, byref(info)):
            return info

    def TUCAM_Capa_GetAttr(self, attr_id):
        ''' Obtain the attribute value of performance parameters. The attributes
            obtained include the minimum value, maximum value, the default value
            and step of the parameter. The specific supported performance type
            can be referred to TUCAM_IDCAPA
        '''

        capa_attr = TUCAM_CAPA_ATTR()
        capa_attr.idCapa = attr_id.value

        if self._api.TUCAM_Capa_GetAttr(self._hdtucam, byref(capa_attr)):
            return capa_attr

    def TUCAM_Cap_SetROI(self, roi):
        ''' It is used to set the interested areas of image, with the upper left
            corner as the origin of coordinates. The set horizontal offset,
            vertical offset, width and height must be in multiples of 4.
            (width by height must be in multiples of 32 in 11bit mode)
        '''

        return self._api.TUCAM_Cap_SetROI(self._hdtucam, roi)

    def TUCAM_Cap_GetROI(self):
        ''' It is used to get the interested areas of image, with the upper left
            corner as the origin of coordinates. The get horizontal offset,
            vertical offset, width and height must be in multiples of 4.
            (width by height must be in multiples of 32 in 11bit mode)
            Capture does not start from this moment. Acquisition starts after
            TUCAM_Cap_Start interface is called
        '''

        roi = TUCAM_ROI_ATTR()

        if self._api.TUCAM_Cap_GetROI(self._hdtucam, byref(roi)):
            return roi

    def TUCAM_Capa_GetValue(self, attr_id):
        ''' Obtain the current attribute value of performance parameters.
            The specific supported performance type can be referred to
            TUCAM_IDCAPA
        '''

        value = c_int()

        if self._api.TUCAM_Capa_GetValue(self._hdtucam, c_int(attr_id.value), byref(value)):
            return value.value

    def TUCAM_Capa_SetValue(self, attr_id, value):
        ''' Set the current attribute value of performance parameters. The
            specific supported performance type can be referred to TUCAM_IDCAPA
        '''

        return self._api.TUCAM_Capa_SetValue(self._hdtucam, c_int(attr_id.value), c_int(value))

    def TUCAM_Capa_GetValueText(self, attr_id):
        ''' Obtain the text information of current attribute value of
            performance parameters. The specific supported performance type
            can be referred to TUCAM_IDCAPA
        '''

        buff = create_string_buffer(64)
        buff_ptr = cast(buff, c_char_p)

        value_text = TUCAM_VALUE_TEXT()
        value_text.nID = attr_id.value
        value_text.pText = buff_ptr
        value_text.nTextSize = 64

        if self._api.TUCAM_Capa_GetValueText(self._hdtucam, byref(value_text)):
            return value_text.pText

    def TUCAM_Prop_GetAttr(self, attr_id):
        ''' Obtain the attribute value of attribute parameters. The attributes
            obtained include the minimum value, maximum value, the default
            value and step of the parameter. The specific supported
            performance type can be referred to TUCAM_IDPROP
        '''

        prop_attr = TUCAM_PROP_ATTR()
        prop_attr.idProp = attr_id.value

        if self._api.TUCAM_Prop_GetAttr(self._hdtucam, byref(prop_attr)):
            return prop_attr

    def TUCAM_Prop_GetValue(self, attr_id, channel=0):
        ''' Obtain the current attribute value of attribute parameters. The
            specific supported performance type can be referred to TUCAM_IDPROP
        '''

        value = c_double()

        if self._api.TUCAM_Prop_GetValue(self._hdtucam, c_int(attr_id.value), byref(value), c_int(channel)):
            return value.value

    def TUCAM_Prop_SetValue(self, attr_id, value, channel=0):
        ''' Set the current attribute value of attribute parameters. The
            specific supported performance type can be referred to TUCAM_IDPROP
        '''

        return self._api.TUCAM_Prop_SetValue(self._hdtucam, c_int(attr_id.value), c_double(value), c_int(channel))

    def TUCAM_Prop_GetValueText(self, attr_id, channel=0):
        ''' Obtain the text information of current attribute value of attribute
            parameters. The specific supported performance type can be referred
            to TUCAM_IDPROP
        '''

        buff = create_string_buffer(64)
        buff_ptr = cast(buff, c_char_p)

        value_text = TUCAM_VALUE_TEXT()
        value_text.nID = attr_id.value
        value_text.pText = buff_ptr
        value_text.nTextSize = 64

        if self._api.TUCAM_Prop_GetValueText(self._hdtucam, byref(value_text), c_int(channel)):
            return value_text.pText

    def TUCAM_Buf_Alloc(self):
        ''' Allocate memory for data capture. When the application calls this
            interface, SDK will allocate the necessary internal buffer to
            buffer image acquisition. Capture does not start from this moment.
            When the acquisition is started, the application must call
            TUCAM_Cap_Start interface. If the buffer is no longer necessary,
            the application should call TUCAM_Buf_Release interface to release
            the internal buffer
        '''

        self._frame = TUCAM_FRAME()
        self._frame.ucFormatGet = TUFRM_FORMATS.TUFRM_FMT_RGB888.value
        self._frame.uiRsdSize = 1     # Frames captured once

        return self._api.TUCAM_Buf_Alloc(self._hdtucam, byref(self._frame))

    def TUCAM_Buf_Release(self):
        ''' Free up memory space for data capture. If the interface is called
            during capture, the interface will return to the state that the
            camera is busy
        '''

        return self._api.TUCAM_Buf_Release(self._hdtucam)

    def TUCAM_Buf_WaitForFrame(self, timeout):
        ''' It is used for the completion of data capture. By calling
            TUCAM_Buf_Alloc the space allocated, the captured frame data is
            obtained. It must be used after calling TUCAM_Cap_Start to start
            capturing; otherwise it will return the state of not ready
        '''

        return self._api.TUCAM_Buf_WaitForFrame(self._hdtucam, byref(self._frame), c_int(timeout))

    def TUCAM_Buf_CopyFrame(self):
        ''' It is used for the image format data copied after the completion of
            waiting data capture different from TUCAM_Buf_Alloc. It must be
            called after TUCAM_Buf_WaitForFrame is returned; otherwise the
            correct image data cannot be obtained
        '''

        return self._api.TUCAM_Buf_CopyFrame(self._hdtucam, byref(self._frame))

    def TUCAM_Buf_AbortWait(self):
        ''' It is used for the waiting when stopping the data capture. After
            calling TUCAM_Buf_WaitForFrame for data capture waiting, use this
            interface to abort waiting
        '''

        return self._api.TUCAM_Buf_AbortWait(self._hdtucam)

    def TUCAM_Cap_Start(self, mode):
        ''' Start data capture. Prior to capture, the interested areas and
            trigger mode should be configured
        '''

        return self._api.TUCAM_Cap_Start(self._hdtucam, c_uint(mode.value))

    def TUCAM_Cap_Stop(self):
        ''' Stop data capture '''

        return self._api.TUCAM_Cap_Stop(self._hdtucam)

    def TUCAM_File_SaveImage(self):
        ''' Save frame data '''

        file_save = TUCAM_FILE_SAVE()
        file_save.nSaveFmt = TUIMG_FORMATS.TUFMT_PNG.value
        file_save.pstrSavePath = b"./screenshot"
        file_save.pFrame = pointer(self._frame)

        return self._api.TUCAM_File_SaveImage(self._hdtucam, file_save)

    def TUCAM_Rec_Start(self):
        ''' Open the video file, and save the video frame data, the data are
            not written at this time. The frame rate set should be greater
            than 1fps, and those less than 1fps will be regarded as 1fps to
            create videofiles
        '''

        file_save = TUCAM_REC_SAVE()
        file_save.nCodec = 0        # ??? Need fix
        file_save.pstrSavePath = b"./video.avi"
        file_save.fFps = 24.0

        return self._api.TUCAM_Rec_Start(self._hdtucam, file_save)

    def TUCAM_Rec_Stop(self):
        ''' Close video file, and calling of TUCAM_Rec_AppendFrame at this
            time will not be able to write data
        '''

        return self._api.TUCAM_Rec_Stop(self._hdtucam)

    def TUCAM_Rec_AppendFrame(self):
        ''' Write the image data into the file, and call the interface at
            TUCAM_Buf_WaitForFrame
        '''

        return self._api.TUCAM_Rec_AppendFrame(self._hdtucam, byref(self._frame))

    def TUCAM_Cap_GetTrigger(self):
        ''' It is used to obtain the trigger attributes '''

        trigger = TUCAM_TRIGGER_ATTR()

        if self._api.TUCAM_Cap_GetTrigger(self._hdtucam, byref(trigger)):
            return trigger

    def TUCAM_Cap_SetTrigger(self, trigger):
        ''' It is used for setting the trigger attribute. Capture does not
            start from this moment. Acquisition starts after TUCAM_Cap_Start
            interface is called
        '''

        return self._api.TUCAM_Cap_SetTrigger(self._hdtucam, trigger)

    def TUCAM_Cap_DoSoftwareTrigger(self):
        ''' Execute software trigger commands '''

        return self._api.TUCAM_Cap_DoSoftwareTrigger(self._hdtucam)

    def TUCAM_Cap_GetTriggerOut(self):
        ''' It is used to obtain the trigger attributes '''

        trigger = TUCAM_TRGOUT_ATTR()

        if self._api.TUCAM_Cap_GetTriggerOut(self._hdtucam, byref(trigger)):
            return trigger

    def TUCAM_Cap_SetTriggerOut(self, trigger):
        ''' It is used for setting the outputtrigger attribute '''

        return self._api.TUCAM_Cap_SetTriggerOut(self._hdtucam, trigger)

    def TUCAM_Reg_Read(self, reg_id):
        ''' Contents read from the register. Refer to TUREG_TYPE for types of
            reading
        '''

        buff = create_string_buffer(64)
        buff_ptr = cast(buff, c_char_p)

        register = TUCAM_REG_RW()
        register.nRegType = reg_id.value
        register.pBuf = buff_ptr
        register.nBufSize = 64

        if self._api.TUCAM_Reg_Read(self._hdtucam, register):
            return register.pBuf

    def TUCAM_Reg_Write(self, reg_id, value):
        ''' Contents written into the register. Refer to TUREG_TYPE for types
            of writing
        '''

        buff = create_string_buffer(value)
        buff_ptr = cast(buff, c_char_p)

        register = TUCAM_REG_RW()
        register.nRegType = reg_id.value
        register.pBuf = buff_ptr
        register.nBufSize = 64

        return self._api.TUCAM_Reg_Write(self._hdtucam, register)

    def convert_image_data(self):
        ''' Преобразует изображение в numpy-массив '''

        data = numpy.asarray(self._frame.pBuffer[self._frame.usHeader: self._frame.usHeader + self._frame.uiImgSize], dtype=numpy.uint8)
        return numpy.reshape(data, (self._frame.usWidth, self._frame.usHeight, self._frame.ucChannels))


__all__ = [ "TUCAM" ]
