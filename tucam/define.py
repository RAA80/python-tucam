#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ctypes import (POINTER, Structure, c_bool, c_byte, c_char, c_char_p,
                    c_double, c_float, c_int, c_ubyte, c_uint, c_ushort,
                    c_void_p)
from enum import Enum


class TUCAMRET(Enum):
    ''' typedef enum TUCAM status '''

    TUCAMRET_SUCCESS           = 0x00000001     # no error, general success code, app should check the value is positive
    TUCAMRET_FAILURE           = 0x80000000     # error
    TUCAMRET_NO_MEMORY         = 0x80000101     # not enough memory
    TUCAMRET_NO_RESOURCE       = 0x80000102     # not enough resource except memory
    TUCAMRET_NO_MODULE         = 0x80000103     # no sub module
    TUCAMRET_NO_DRIVER         = 0x80000104     # no driver
    TUCAMRET_NO_CAMERA         = 0x80000105     # no camera
    TUCAMRET_NO_GRABBER        = 0x80000106     # no grabber
    TUCAMRET_NO_PROPERTY       = 0x80000107     # there is no alternative or influence id, or no more property id
    TUCAMRET_FAILOPEN_CAMERA   = 0x80000110     # fail open the camera
    TUCAMRET_FAILOPEN_BULKIN   = 0x80000111     # fail open the bulk in endpoint
    TUCAMRET_FAILOPEN_BULKOUT  = 0x80000112     # fail open the bulk out endpoint
    TUCAMRET_FAILOPEN_CONTROL  = 0x80000113     # fail open the control endpoint
    TUCAMRET_FAILCLOSE_CAMERA  = 0x80000114     # fail close the camera
    TUCAMRET_FAILOPEN_FILE     = 0x80000115     # fail open the file
    TUCAMRET_FAILOPEN_CODEC    = 0x80000116     # fail open the video codec
    TUCAMRET_FAILOPEN_CONTEXT  = 0x80000117     # fail open the video context
    TUCAMRET_INIT              = 0x80000201     # API requires has not initialized state.
    TUCAMRET_BUSY              = 0x80000202     # API cannot process in busy state.
    TUCAMRET_NOT_INIT          = 0x80000203     # API requires has initialized state.
    TUCAMRET_EXCLUDED          = 0x80000204     # some resource is exclusive and already used.
    TUCAMRET_NOT_BUSY          = 0x80000205     # API requires busy state.
    TUCAMRET_NOT_READY         = 0x80000206     # API requires ready state.
    TUCAMRET_ABORT             = 0x80000207     # abort process
    TUCAMRET_TIMEOUT           = 0x80000208     # timeout
    TUCAMRET_LOSTFRAME         = 0x80000209     # frame data is lost
    TUCAMRET_MISSFRAME         = 0x8000020A     # frame is lost but reason is low lever driver's bug
    TUCAMRET_USB_STATUS_ERROR  = 0x8000020B     # the USB status error
    TUCAMRET_INVALID_CAMERA    = 0x80000301     # invalid camera
    TUCAMRET_INVALID_HANDLE    = 0x80000302     # invalid camera handle
    TUCAMRET_INVALID_OPTION    = 0x80000303     # invalid the option value of structure
    TUCAMRET_INVALID_IDPROP    = 0x80000304     # invalid property id
    TUCAMRET_INVALID_IDCAPA    = 0x80000305     # invalid capability id
    TUCAMRET_INVALID_IDPARAM   = 0x80000306     # invalid parameter id
    TUCAMRET_INVALID_PARAM     = 0x80000307     # invalid parameter
    TUCAMRET_INVALID_FRAMEIDX  = 0x80000308     # invalid frame index
    TUCAMRET_INVALID_VALUE     = 0x80000309     # invalid property value
    TUCAMRET_INVALID_EQUAL     = 0x8000030A     # invalid property value equal
    TUCAMRET_INVALID_CHANNEL   = 0x8000030B     # the property id specifies channel but channel is invalid
    TUCAMRET_INVALID_SUBARRAY  = 0x8000030C     # the combination of subarray values are invalid. e.g. TUCAM_IDPROP_SUBARRAYHPOS + TUCAM_IDPROP_SUBARRAYHSIZE is greater than the number of horizontal pixel of sensor.
    TUCAMRET_INVALID_VIEW      = 0x8000030D     # invalid view window handle
    TUCAMRET_INVALID_PATH      = 0x8000030E     # invalid file path
    TUCAMRET_INVALID_IDVPROP   = 0x8000030F     # invalid vendor property id
    TUCAMRET_NO_VALUETEXT      = 0x80000310     # the property does not have value text
    TUCAMRET_OUT_OF_RANGE      = 0x80000311     # value is out of range
    TUCAMRET_NOT_SUPPORT       = 0x80000312     # camera does not support the function or property with current settings
    TUCAMRET_NOT_WRITABLE      = 0x80000313     # the property is not writable
    TUCAMRET_NOT_READABLE      = 0x80000314     # the property is not readable
    TUCAMRET_WRONG_HANDSHAKE   = 0x80000410     # this error happens TUCAM get error code from camera unexpectedly
    TUCAMRET_NEWAPI_REQUIRED   = 0x80000411     # old API does not support the value because only new API supports the value
    TUCAMRET_ACCESSDENY        = 0x80000412     # the property cannot access during this TUCAM status
    TUCAMRET_NO_CORRECTIONDATA = 0x80000501     # not take the dark and shading correction data yet.
    TUCAMRET_INVALID_PRFSETS   = 0x80000601     # the profiles set name is invalid
    TUCAMRET_INVALID_IDPPROP   = 0x80000602     # invalid process property id
    TUCAMRET_DECODE_FAILURE    = 0x80000701     # the image decoding raw data to rgb data failure
    TUCAMRET_COPYDATA_FAILURE  = 0x80000702     # the image data copying failure
    TUCAMRET_ENCODE_FAILURE    = 0x80000703     # the image encoding data  to video failure
    TUCAMRET_WRITE_FAILURE     = 0x80000704     # the write the video frame failure
    TUCAMRET_FAIL_READ_CAMERA  = 0x83001001     # fail read from camera
    TUCAMRET_FAIL_WRITE_CAMERA = 0x83001002     # fail write to camera
    TUCAMRET_OPTICS_UNPLUGGED  = 0x83001003     # optics part is unplugged so please check it.
    TUCAMRET_RECEIVE_FINISH    = 0x00000002     # no error, vendor receive frame message
    TUCAMRET_EXTERNAL_TRIGGER  = 0x00000003     # no error, receive the external trigger signal


class TUCAM_IDINFO(Enum):
    ''' typedef enum information id '''

    TUIDI_BUS                = 0x01         # the bus type USB2.0/USB3.0
    TUIDI_VENDOR             = 0x02         # the vendor id
    TUIDI_PRODUCT            = 0x03         # the product id
    TUIDI_VERSION_API        = 0x04         # the API version
    TUIDI_VERSION_FRMW       = 0x05         # the firmware version
    TUIDI_VERSION_FPGA       = 0x06         # the FPGA version
    TUIDI_VERSION_DRIVER     = 0x07         # the driver version
    TUIDI_TRANSFER_RATE      = 0x08         # the transfer rate
    TUIDI_CAMERA_MODEL       = 0x09         # the camera model (string)
    TUIDI_CURRENT_WIDTH      = 0x0A         # the camera image data current width(must use TUCAM_Dev_GetInfoEx and after calling TUCAM_Buf_Alloc)
    TUIDI_CURRENT_HEIGHT     = 0x0B         # the camera image data current height(must use TUCAM_Dev_GetInfoEx and after calling TUCAM_Buf_Alloc)
    TUIDI_CAMERA_CHANNELS    = 0x0C         # the camera image data channels
    TUIDI_BCDDEVICE          = 0x0D         # the USB bcdDevice
    TUIDI_TEMPALARMFLAG      = 0x0E         # the Temperature Alarm Flag
    TUIDI_UTCTIME            = 0x0F         # the get utc time
    TUIDI_LONGITUDE_LATITUDE = 0x10         # the get longitude latitude
    TUIDI_WORKING_TIME       = 0x11         # the get working time
    TUIDI_FAN_SPEED          = 0x12         # the get fan speed
    TUIDI_FPGA_TEMPERATURE   = 0x13         # the get fpga temperature
    TUIDI_PCBA_TEMPERATURE   = 0x14         # the get pcba temperature
    TUIDI_ENV_TEMPERATURE    = 0x15         # the get environment temperature
    TUIDI_DEVICE_ADDRESS     = 0x16         # the USB device address
    TUIDI_USB_PORT_ID        = 0x17         # the USB port id
    TUIDI_ENDINFO            = 0x18         # the string id end


class TUCAM_IDCAPA(Enum):
    ''' typedef enum capability id '''

    TUIDC_RESOLUTION           = 0x00       # id capability resolution
    TUIDC_PIXELCLOCK           = 0x01       # id capability pixel clock
    TUIDC_BITOFDEPTH           = 0x02       # id capability bit of depth
    TUIDC_ATEXPOSURE           = 0x03       # id capability automatic exposure time
    TUIDC_HORIZONTAL           = 0x04       # id capability horizontal
    TUIDC_VERTICAL             = 0x05       # id capability vertical
    TUIDC_ATWBALANCE           = 0x06       # id capability automatic white balance
    TUIDC_FAN_GEAR             = 0x07       # id capability fan gear
    TUIDC_ATLEVELS             = 0x08       # id capability automatic levels
    TUIDC_SHIFT                = 0x09       # (The reserved) id capability shift(15~8, 14~7, 13~6, 12~5, 11~4, 10~3, 9~2, 8~1, 7~0) [16bit]
    TUIDC_HISTC                = 0x0A       # id capability histogram statistic
    TUIDC_CHANNELS             = 0x0B       # id capability current channels(Only color camera support:0-RGB,1-Red,2-Green,3-Blue. Used in the property levels, see enum TUCHN_SELECT)
    TUIDC_ENHANCE              = 0x0C       # id capability enhance
    TUIDC_DFTCORRECTION        = 0x0D       # id capability defect correction (0-not correction, 1-calculate, 3-correction)
    TUIDC_ENABLEDENOISE        = 0x0E       # id capability enable denoise (TUIDP_NOISELEVEL effective)
    TUIDC_FLTCORRECTION        = 0x0F       # id capability flat field correction (0-not correction, 1-grab frame, 2-calculate, 3-correction)
    TUIDC_RESTARTLONGTM        = 0x10       # id capability restart long exposure time (only CCD camera support)
    TUIDC_DATAFORMAT           = 0x11       # id capability the data format(only YUV format data support 0-YUV 1-RAW)
    TUIDC_DRCORRECTION         = 0x12       # (The reserved)id capability dynamic range of correction
    TUIDC_VERCORRECTION        = 0x13       # id capability vertical correction(correction the image data show vertical, in windows os the default value is 1)
    TUIDC_MONOCHROME           = 0x14       # id capability monochromatic
    TUIDC_BLACKBALANCE         = 0x15       # id capability black balance
    TUIDC_IMGMODESELECT        = 0x16       # id capability image mode select(CMS mode)
    TUIDC_CAM_MULTIPLE         = 0x17       # id capability multiple cameras (how many cameras use at the same time, only SCMOS camera support)
    TUIDC_ENABLEPOWEEFREQUENCY = 0x18       # id capability enable power frequency (50HZ or 60HZ)
    TUIDC_ROTATE_R90           = 0x19       # id capability rotate 90 degree to right
    TUIDC_ROTATE_L90           = 0x1A       # id capability rotate 90 degree to left
    TUIDC_NEGATIVE             = 0x1B       # id capability negative film enable
    TUIDC_HDR                  = 0x1C       # id capability HDR enable
    TUIDC_ENABLEIMGPRO         = 0x1D       # id capability image process enable
    TUIDC_ENABLELED            = 0x1E       # id capability USB led enable
    TUIDC_ENABLETIMESTAMP      = 0x1F       # id capability time stamp enable
    TUIDC_ENABLEBLACKLEVEL     = 0x20       # id capability black level offset enable
    TUIDC_ATFOCUS              = 0x21       # id capability auto focus enable(0-manual 1-automatic focus 2-Once)
    TUIDC_ATFOCUS_STATUS       = 0x22       # id capability auto focus status(0-stop 1-focusing 2-completed 3-defocus)
    TUIDC_PGAGAIN              = 0x23       # id capability sensor pga gain
    TUIDC_ATEXPOSURE_MODE      = 0x24       # id capability automatic exposure time mode
    TUIDC_BINNING_SUM          = 0x25       # id capability the summation binning
    TUIDC_BINNING_AVG          = 0x26       # id capability the average binning
    TUIDC_FOCUS_C_MOUNT        = 0x27       # id capability the focus c-mount mode(0-normal 1-c-mount mode)
    TUIDC_ENABLEPI             = 0x28       # id capability PI enable
    TUIDC_ATEXPOSURE_STATUS    = 0x29       # id capability auto exposure status (0-doing 1-completed)
    TUIDC_ATWBALANCE_STATUS    = 0x2A       # id capability auto white balance status (0-doing 1-completed)
    TUIDC_TESTIMGMODE          = 0x2B       # id capability test image mode select
    TUIDC_SENSORRESET          = 0x2C       # id capability sensor reset
    TUIDC_PGAHIGH              = 0x2D       # id capability pga high gain
    TUIDC_PGALOW               = 0x2E       # id capability pga low gain
    TUIDC_PIXCLK1_EN           = 0x2F       # id capability pix1 clock enable
    TUIDC_PIXCLK2_EN           = 0x30       # id capability pix2 clock enable
    TUIDC_ATLEVELGEAR          = 0x31       # id capability auto level gear
    TUIDC_ENABLEDSNU           = 0x32       # id capability enable dsnu
    TUIDC_ENABLEOVERLAP        = 0x33       # id capability enable exposure time overlap mode
    TUIDC_CAMSTATE             = 0x34       # id capability camera state
    TUIDC_ENABLETRIOUT         = 0x35       # id capability enable trigger out enable
    TUIDC_ROLLINGSCANMODE      = 0x36       # id capability rolling scan mode
    TUIDC_ROLLINGSCANLTD       = 0x37       # id capability rolling scan line time delay
    TUIDC_ROLLINGSCANSLIT      = 0x38       # id capability rolling scan slit height
    TUIDC_ROLLINGSCANDIR       = 0x39       # id capability rolling scan direction
    TUIDC_ROLLINGSCANRESET     = 0x3A       # id capability rolling scan direction reset
    TUIDC_ENABLETEC            = 0x3B       # id capability TEC enable
    TUIDC_ENABLEBLC            = 0x3C       # id capability backlight compensation enable
    TUIDC_ENABLETHROUGHFOG     = 0x3D       # id capability electronic through fog enable
    TUIDC_ENABLEGAMMA          = 0x3E       # id capability gamma enable
    TUIDC_CAMPARASAVE          = 0x3F       # id capability camera parameter save
    TUIDC_CAMPARALOAD          = 0x40       # id capability camera parameter load
    TUIDC_ENDCAPABILITY        = 0x41       # id capability end


class TUCAM_IDPROP(Enum):
    ''' typedef enum property id '''

    TUIDP_GLOBALGAIN       = 0x00       # id property global gain
    TUIDP_EXPOSURETM       = 0x01       # id property exposure time
    TUIDP_BRIGHTNESS       = 0x02       # id property brightness (Effective automatic exposure condition)
    TUIDP_BLACKLEVEL       = 0x03       # id property black level
    TUIDP_TEMPERATURE      = 0x04       # id property temperature control
    TUIDP_SHARPNESS        = 0x05       # id property sharpness
    TUIDP_NOISELEVEL       = 0x06       # id property the noise level
    TUIDP_HDR_KVALUE       = 0x07       # id property the HDR K value
    TUIDP_GAMMA            = 0x08       # id property gamma
    TUIDP_CONTRAST         = 0x09       # id property contrast
    TUIDP_LFTLEVELS        = 0x0A       # id property left levels
    TUIDP_RGTLEVELS        = 0x0B       # id property right levels
    TUIDP_CHNLGAIN         = 0x0C       # id property channel gain
    TUIDP_SATURATION       = 0x0D       # id property saturation
    TUIDP_CLRTEMPERATURE   = 0x0E       # id property color temperature
    TUIDP_CLRMATRIX        = 0x0F       # id property color matrix setting
    TUIDP_DPCLEVEL         = 0x10       # id property defect points correction level
    TUIDP_BLACKLEVELHG     = 0x11       # id property black level high gain
    TUIDP_BLACKLEVELLG     = 0x12       # id property black level low gain
    TUIDP_POWEEFREQUENCY   = 0x13       # id property power frequency (50HZ or 60HZ)
    TUIDP_HUE              = 0x14       # id property hue
    TUIDP_LIGHT            = 0x15       # id property light
    TUIDP_ENHANCE_STRENGTH = 0x16       # id property enhance strength
    TUIDP_NOISELEVEL_3D    = 0x17       # id property the 3D noise level
    TUIDP_FOCUS_POSITION   = 0x18       # id property focus position
    TUIDP_FRAME_RATE       = 0x19       # id property frame rate
    TUIDP_START_TIME       = 0x1A       # id property start time
    TUIDP_FRAME_NUMBER     = 0x1B       # id property frame number
    TUIDP_INTERVAL_TIME    = 0x1C       # id property interval time
    TUIDP_GPS_APPLY        = 0x1D       # id property gps apply
    TUIDP_AMB_TEMPERATURE  = 0x1E       # id property ambient temperature
    TUIDP_AMB_HUMIDITY     = 0x1F       # id property ambient humidity
    TUIDP_AUTO_CTRLTEMP    = 0x20       # id property auto control temperature
    TUIDP_AVERAGEGRAY      = 0x21       # id property average gray setting
    TUIDP_AVERAGEGRAYTHD   = 0x22       # id property average gray threshold setting
    TUIDP_ENHANCETHD       = 0x23       # id property enhance threshold setting
    TUIDP_ENHANCEPARA      = 0x24       # id property enhance parameter setting
    TUIDP_EXPOSUREMAX      = 0x25       # id property max exposure time setting
    TUIDP_EXPOSUREMIN      = 0x26       # id property min exposure time setting
    TUIDP_GAINMAX          = 0x27       # id property max gain setting
    TUIDP_GAINMIN          = 0x28       # id property min gain setting
    TUIDP_THROUGHFOGPARA   = 0x29       # id property through fog parameter setting
    TUIDP_ENDPROPERTY      = 0x2A       # id property end


class TUCAM_IDVPROP(Enum):
    ''' typedef enum vendor property id '''

    TUIDV_ADDR_FLASH         = 0x00     # id vendor flash address
    TUIDV_ODDEVENH           = 0x01     # id vendor odd even high value
    TUIDV_ODDEVENL           = 0x02     # id vendor odd even low value
    TUIDV_HDRHGBOFFSET       = 0x03     # id vendor the hdr high gain b offset
    TUIDV_HDRLGBOFFSET       = 0x04     # id vendor the hdr low gain b offset
    TUIDV_CMSHGBOFFSET       = 0x05     # id vendor the cms high gain b offset
    TUIDV_CMSLGBOFFSET       = 0x06     # id vendor the cms low gain b offset
    TUIDV_FPNENABLE          = 0x07     # id vendor the fpn enable
    TUIDV_WORKING_TIME       = 0x08     # id vendor the working time
    TUIDV_CALC_DSNU          = 0x09     # id vendor the calc dsnu
    TUIDV_CALC_PRNU          = 0x0A     # id vendor the calc prnu
    TUIDV_CALC_DPC           = 0x0B     # id vendor the calc dpc
    TUIDV_CALC_STOP          = 0x0C     # id vendor the calc stop
    TUIDV_CALC_STATE         = 0x0D     # id vendor the calc state [0-GenFree, 1-GenBusy, 2-CalBusy, 3-WRBusy, 4-GenDone, 5-GenStop]
    TUIDV_HDR_LVALUE         = 0x0E     # id property the HDR Low value
    TUIDV_HDR_HVALUE         = 0x0F     # id property the HDR High value
    TUIDV_FW_CHECK           = 0x10     # id property the FW Check value
    TUIDV_HIGHSPEEDHGBOFFSET = 0x11     # id vendor the high speed high gain b offset
    TUIDV_HIGHSPEEDLGBOFFSET = 0x12     # id vendor the high speed low gain b offset
    TUIDV_TEMPERATURE_OFFSET = 0x13     # id vendor the temperature offset
    TUIDV_ENDVPROPERTY       = 0x14     # id vendor end


class TUCAM_IDPPROP(Enum):
    TUIDPP_EDF_QUALITY      = 0x00      # id process EDF quality
    TUIDPP_STITCH_SPEED     = 0x01      # id process stitch speed
    TUIDPP_STITCH_BGC_RED   = 0x02      # id process stitch background color red
    TUIDPP_STITCH_BGC_GREEN = 0x03      # id process stitch background color green
    TUIDPP_STITCH_BGC_BLUE  = 0x04      # id process stitch background color blue
    TUIDPP_STITCH_VALID     = 0x05      # id process stitch whether the result is valid (Only get value)
    TUIDPP_STITCH_AREA_X    = 0x06      # id process stitch result and the current point X coordinates value (Only get value)
    TUIDPP_STITCH_AREA_Y    = 0x07      # id process stitch result and the current point Y coordinates value (Only get value)
    TUIDPP_STITCH_NEXT_X    = 0x08      # id process stitch result and the next point X coordinates value (Only get value)
    TUIDPP_STITCH_NEXT_Y    = 0x09      # id process stitch result and the next point Y coordinates value (Only get value)
    TUIDPP_ENDPPROPERTY     = 0x0A      # id process end


class TUCAM_IDCROI(Enum):
    ''' typedef enum calculate roi id '''

    TUIDCR_WBALANCE   = 0x00    # id calculate roi white balance
    TUIDCR_BBALANCE   = 0x01    # id calculate roi black balance
    TUIDCR_BLOFFSET   = 0x02    # id calculate roi black level offset
    TUIDCR_FOCUS      = 0x03    # id calculate roi focus
    TUIDCR_EXPOSURETM = 0x04    # id calculate roi exposure time
    TUIDCR_END        = 0x05    # id calculate roi end


class TUCAM_CAPTURE_MODES(Enum):
    ''' typedef enum the capture mode '''

    TUCCM_SEQUENCE            = 0x00    # capture start sequence mode
    TUCCM_TRIGGER_STANDARD    = 0x01    # capture start trigger standard mode
    TUCCM_TRIGGER_SYNCHRONOUS = 0x02    # capture start trigger synchronous mode
    TUCCM_TRIGGER_GLOBAL      = 0x03    # capture start trigger global
    TUCCM_TRIGGER_SOFTWARE    = 0x04    # capture start trigger software
    TUCCM_TRIGGER_GPS         = 0x05    # capture start trigger gps


class TUIMG_FORMATS(Enum):
    ''' typedef enum the image formats '''

    TUFMT_RAW = 0x01            # The format RAW
    TUFMT_TIF = 0x02            # The format TIFF
    TUFMT_PNG = 0x04            # The format PNG
    TUFMT_JPG = 0x08            # The format JPEG
    TUFMT_BMP = 0x10            # The format BMP


class TUREG_TYPE(Enum):
    ''' typedef enum the register types '''

    TUREG_SN                = 0x01      # The type register SN
    TUREG_DATA              = 0x02      # The type register data
    TUREG_BAD_ROW           = 0x03      # The type register bad row     (Vendor use)
    TUREG_BAD_COL           = 0x04      # The type register bad column  (Vendor use)
    TUREG_BGC               = 0x05      # The type register background  (Vendor use)
    TUREG_HDR               = 0x06      # The type register HDR exp para(Vendor use)
    TUREG_HBG               = 0x07      # The type register HDR exp para(Vendor use)
    TUREG_CMS               = 0x08      # The type register CMS exp para(Vendor use)
    TUREG_CBG               = 0x09      # The type register CMS exp para(Vendor use)
    TUREG_CODE              = 0x0A      # The type register code        (Vendor use)
    TUREG_DPC               = 0x0B      # The type register DPC         (Vendor use)
    TUREG_TEMPERATUREOFFSET = 0x0C      # The type register Temperature (Vendor use)
    TUREG_HIGHSPEEDBGYLIST  = 0x0D      # The type register  (Vendor use)


class TUCAM_TRIGGER_EXP(Enum):
    ''' typedef enum the trigger exposure time mode '''

    TUCTE_EXPTM = 0x00          # use exposure time
    TUCTE_WIDTH = 0x01          # use width level


class TUCAM_TRIGGER_EDGE(Enum):
    ''' typedef enum the trigger edge mode '''

    TUCTD_RISING  = 0x01        # rising edge
    TUCTD_FAILING = 0x00        # failing edge


class TUCAM_TRIGGER_READOUTDIRRESET(Enum):
    ''' typedef enum the trigger readout direction reset mode '''

    TUCTD_YES = 0x00            # yes reset
    TUCTD_NO  = 0x01            # no reset


class TUCAM_TRIGGER_READOUTDIR(Enum):
    ''' typedef enum the trigger readout direction mode '''

    TUCTD_DOWN      = 0x00      # down
    TUCTD_UP        = 0x01      # up
    TUCTD_DOWNUPCYC = 0x02      # down up cycle


class TUCAM_OUTPUTTRG_PORT(Enum):
    ''' typedef enum the output trigger port mode '''

    TUPORT_ONE   = 0x00         # use port1
    TUPORT_TWO   = 0x01         # use port2
    TUPORT_THREE = 0x02         # use port3


class TUCAM_OUTPUTTRG_KIND(Enum):
    ''' typedef enum the output trigger kind mode '''

    TUOPT_GND       = 0x00      # use low
    TUOPT_VCC       = 0x01      # use high
    TUOPT_IN        = 0x02      # use trigger input
    TUOPT_EXPSTART  = 0x03      # use exposure start
    TUOPT_EXPGLOBAL = 0x04      # use global exposure
    TUOPT_READEND   = 0x05      # use read end


class TUCAM_OUTPUTTRG_EDGE(Enum):
    ''' typedef enum the output trigger edge mode '''

    TUOPT_RISING  = 0x00        # rising edge
    TUOPT_FAILING = 0x01        # failing edge


class TUFRM_FORMATS(Enum):
    ''' typedef enum the frame formats '''

    TUFRM_FMT_RAW    = 0x10     # The raw data
    TUFRM_FMT_USUAl  = 0x11     # The usually data
    TUFRM_FMT_RGB888 = 0x12     # The RGB888 data for drawing


class TUGAIN_MODE(Enum):
    ''' typedef enum the SCMOS gain mode '''

    TUGAIN_HDR  = 0x00          # The HDR mode
    TUGAIN_HIGH = 0x01          # The High gain mode
    TUGAIN_LOW  = 0x02          # The Low gain mode


class TUVEN_CFG_MODE(Enum):
    ''' typedef enum the vendor config mode '''

    TUVCM_BGC         = 0x00    # The background correction
    TUVCM_CODE        = 0x01    # The code
    TUVCM_REBG        = 0x02    # The refresh background
    TUVCM_SN_CHECKING = 0x03    # The SN checking


class TUVEN_CFGEX_MODE(Enum):
    ''' typedef enum the vendor configex mode '''

    TUVCMEX_FWTOOL = 0x00       # The called by fwtool
    TUVCMEX_END    = 0x01       # The end


class TUDRAW_MODE(Enum):
    ''' typedef enum drawing mode(only support on windows os) '''

    TUDRAW_DFT = 0x00           # The default mode
    TUDRAW_DIB = 0x01           # The DIB mode
    TUDRAW_DX9 = 0x02           # The DirectX 9.0


class TUCHN_SELECT(Enum):
    ''' The enum of channels '''

    TUCHN_SHARE = 0x00          # The channel shared (Gray or RGB)
    TUCHN_RED   = 0x01          # The channel 1 (Red channel)
    TUCHN_GREEN = 0x02          # The channel 2 (Green channel)
    TUCHN_BLUE  = 0x03          # The channel 3 (Blue channel)


class TUFW_TYPE(Enum):
    ''' typedef enum the firmware types '''

    TUFW_IIC  = 0x01            # The type firmware IIC
    TUFW_FPGA = 0x02            # The type firmware FPGA


class TUREC_MODE(Enum):
    ''' typedef enum the record append mode '''

    TUREC_TIMESTAMP = 0x01      # The record mode time-stamp
    TUREC_SEQUENCE  = 0x02      # The record mode sequence


class TUPROC_TYPE(Enum):
    ''' typedef enum the image process type '''

    TUPROC_EDF    = 0x00        # The process EDF
    TUPROC_STITCH = 0x01        # The process stitch


class TUSTITCH_MODE(Enum):
    ''' typedef enum the image process stitch mode '''

    TUSM_FINE      = 0x00       # The fine mode
    TUSM_EXCELLENT = 0x01       # The excellent mode


class TUFOCUS_STATUS(Enum):
    ''' typedef enum the focus status '''

    TUFS_STOP      = 0x00       # The focus status is stop
    TUFS_FOCUSING  = 0x01       # The focus status is focusing
    TUFS_COMPLETED = 0x02       # The focus status is completed
    TUFS_DEFOCUS   = 0x03       # The focus status is defocus


########################


class HDTUCAM(Structure):
    _fields_ = [
        ('void', c_void_p)
    ]


class HDTUIMG(Structure):
    _fields_ = [
        ('void', c_void_p)
    ]


class TUCAM_INIT(Structure):
    ''' the camera initialize struct '''

    _fields_ = [
        ('uiCamCount', c_uint),                 # [out]
        ('pstrConfigPath', c_char_p)            # [in] save the path of the camera parameters
    ]


class TUCAM_OPEN(Structure):
    ''' the camera open struct '''

    _fields_ = [
        ('uiIdxOpen', c_uint),                  # [in]
        ('hIdxTUCam', HDTUCAM)                  # [out] the handle of the opened camera device
    ]


class TUIMG_OPEN(Structure):
    ''' the image open struct '''

    _fields_ = [
        ('pszfileName', c_char_p),              # [in] the full path of the image file
        ('hIdxTUImg', HDTUIMG)                  # [out] the handle of the opened image file
    ]


class TUCAM_VALUE_INFO(Structure):
    ''' the camera value info struct '''

    _fields_ = [
        ('nID', c_int),                         # [in] TUCAM_IDINFO
        ('nValue', c_int),                      # [in] value of information
        ('pText', c_char_p),                    # [in/out] text of the value
        ('nTextSize', c_int)                    # [in] text buf size
    ]


class TUCAM_VALUE_TEXT(Structure):
    ''' the camera value text struct '''

    _fields_ = [
        ('nID', c_int),                         # [in] TUCAM_IDPROP / TUCAM_IDCAPA
        ('dbValue', c_double),                  # [in] value of property
        ('pText', c_char_p),                    # [in/out] text of the value
        ('nTextSize', c_int)                    # [in] text buf size
    ]


class TUCAM_CAPA_ATTR(Structure):
    ''' the camera capability attribute '''

    _fields_ = [
        ('idCapa', c_int),                      # [in] TUCAM_IDCAPA
        ('nValMin', c_int),                     # [out] minimum value
        ('nValMax', c_int),                     # [out] maximum value
        ('nValDft', c_int),                     # [out] default value
        ('nValStep', c_int)                     # [out] minimum stepping between a value and the next
    ]


class TUCAM_PROP_ATTR(Structure):
    ''' the camera property attribute '''

    _fields_ = [
        ('idProp', c_int),                      # [in] TUCAM_IDPROP
        ('nIdxChn', c_int),                     # [in/out] the index of channel
        ('dbValMin', c_double),                 # [out] minimum value
        ('dbValMax', c_double),                 # [out] maximum value
        ('dbValDft', c_double),                 # [out] default value
        ('dbValStep', c_double)                 # [out] minimum stepping between a value and the next
    ]


class TUCAM_VPROP_ATTR(Structure):
    ''' the camera vendor property attribute '''

    _fields_ = [
        ('idVProp', c_int),                     # [in] TUCAM_IDVPROP
        ('nIdxChn', c_int),                     # [in/out] the index of channel
        ('dbValMin', c_double),                 # [out] minimum value
        ('dbValMax', c_double),                 # [out] maximum value
        ('dbValDft', c_double),                 # [out] default value
        ('dbValStep', c_double)                 # [out] minimum stepping between a value and the next
    ]


class TUCAM_PPROP_ATTR(Structure):
    ''' the camera process property attribute '''

    _fields_ = [
        ('idPProp', c_int),                     # [in] TUCAM_IDVPROP
        ('procType', c_int),                    # [in] TUPROC_TYPE
        ('dbValMin', c_double),                 # [out] minimum value
        ('dbValMax', c_double),                 # [out] maximum value
        ('dbValDft', c_double),                 # [out] default value
        ('dbValStep', c_double)                 # [out] minimum stepping between a value and the next
    ]


class TUCAM_ROI_ATTR(Structure):
    ''' the camera roi attribute '''

    _fields_ = [
        ('bEnable', c_bool),                    # [in/out] The ROI enable
        ('nHOffset', c_int),                    # [in/out] The horizontal offset
        ('nVOffset', c_int),                    # [in/out] The vertical offset
        ('nWidth', c_int),                      # [in/out] The ROI width
        ('nHeight', c_int)                      # [in/out] The ROI height
    ]


class TUCAM_CALC_ROI_ATTR(Structure):
    ''' the camera roi calculate attribute '''

    _fields_ = [
        ('bEnable', c_bool),                    # [in/out] The ROI enable
        ('idCalc', c_int),                      # [in] TUCAM_IDCROI
        ('nHOffset', c_int),                    # [in/out] The horizontal offset
        ('nVOffset', c_int),                    # [in/out] The vertical offset
        ('nWidth', c_int),                      # [in/out] The ROI width
        ('nHeight', c_int)                      # [in/out] The ROI height
    ]


class TUCAM_TRIGGER_ATTR(Structure):
    ''' the camera trigger attribute '''

    _fields_ = [
        ('nTgrMode', c_int),                    # [in/out] The mode of trigger
        ('nExpMode', c_int),                    # [in/out] The mode of exposure [0, 1] 0:Exposure time   1:Width level
        ('nEdgeMode', c_int),                   # [in/out] The mode of edge     [0, 1] 0:Falling edge    1:Rising edge
        ('nDelayTm', c_int),                    # [in/out] The time delay
        ('nFrames', c_int),                     # [in/out] How many frames per trigger
        ('nBufFrames', c_int)                   # [in/out] How many frames in buffer
    ]


class TUCAM_TRGOUT_ATTR(Structure):
    ''' the camera trigger out attribute '''

    _fields_ = [
        ('nTgrOutPort', c_int),                 # [in/out] The port of trigger out
        ('nTgrOutMode', c_int),                 # [in/out] The mode of trigger out
        ('nEdgeMode', c_int),                   # [in/out] The mode of edge     [0, 1] 1:Falling edge    0:Rising edge
        ('nDelayTm', c_int),                    # [in/out] The time delay
        ('nWidth', c_int)                       # [in/out] The width of pulse
    ]


class TUCAM_FRAME(Structure):
    ''' the camera frame struct '''

    _fields_ = [
        ('szSignature', c_char * 8),            # [out]Copyright+Version: TU+1.0 ['T', 'U', '1', '\0']
        ('usHeader', c_ushort),                 # [out] The frame header size
        ('usOffset', c_ushort),                 # [out] The frame data offset
        ('usWidth', c_ushort),                  # [out] The frame width
        ('usHeight', c_ushort),                 # [out] The frame height
        ('uiWidthStep', c_uint),                # [out] The frame width step
        ('ucDepth', c_ubyte),                   # [out] The frame data depth
        ('ucFormat', c_ubyte),                  # [out] The frame data format
        ('ucChannels', c_ubyte),                # [out] The frame data channels
        ('ucElemBytes', c_ubyte),               # [out] The frame data bytes per element
        ('ucFormatGet', c_ubyte),               # [in] Which frame data format do you want    see TUFRM_FORMATS
        ('uiIndex', c_uint),                    # [in/out] The frame index number
        ('uiImgSize', c_uint),                  # [out] The frame size
        ('uiRsdSize', c_uint),                  # [in] The frame reserved size    (how many frames do you want)
        ('uiHstSize', c_uint),                  # [out] The frame histogram size
        ('pBuffer', POINTER(c_ubyte))           # [in/out] The frame buffer
    ]


class TUCAM_FILE_SAVE(Structure):
    ''' the file save struct '''

    _fields_ = [
        ('nSaveFmt', c_int),                    # [in] the format of save file     see TUIMG_FORMATS
        ('pstrSavePath', c_char_p),             # [in] the path of save file
        ('pFrame', POINTER(TUCAM_FRAME))        # [in] the struct of camera frame
    ]


class TUCAM_REC_SAVE(Structure):
    ''' the record save struct '''

    _fields_ = [
        ('nCodec', c_int),                      # [in] the coder-decoder type
        ('pstrSavePath', c_char_p),             # [in] the path of save record file
        ('fFps', c_float)                       # [in] the current FPS
    ]


class TUCAM_REG_RW(Structure):
    ''' the register read/write struct '''

    _fields_ = [
        ('nRegType', c_int),                    # [in] the format of register     see TUREG_TYPE
        ('pBuf', c_char_p),                     # [in/out] pointer to the buffer value
        ('nBufSize', c_int)                     # [in] the buffer size
    ]


class TUCAM_DRAW_INIT(Structure):
    ''' typedef struct draw initialize '''

    _fields_ = [
        ('nMode', c_int),                       # [in] (The reserved)Whether use hardware acceleration (If the GPU support) default:TUDRAW_DFT
        ('ucChannels', c_ubyte),                # [in] The data channels
        ('nWidth', c_int),                      # [in] The drawing data width
        ('nHeight', c_int)                      # [in] The drawing data height
    ]


class TUCAM_DRAW(Structure):
    ''' typedef struct drawing '''

    _fields_ = [
        ('nSrcX', c_int),                       # [in/out] The x-coordinate, in pixels, of the upper left corner of the source rectangle
        ('nSrcY', c_int),                       # [in/out] The y-coordinate, in pixels, of the upper left corner of the source rectangle
        ('nSrcWidth', c_int),                   # [in/out] Width, in pixels, of the source rectangle
        ('nSrcHeight', c_int),                  # [in/out] Height, in pixels, of the source rectangle
        ('nDstX', c_int),                       # [in/out] The x-coordinate, in MM_TEXT client coordinates, of the upper left corner of the destination rectangle
        ('nDstY', c_int),                       # [in/out] The y-coordinate, in MM_TEXT client coordinates, of the upper left corner of the destination rectangle
        ('nDstWidth', c_int),                   # [in/out] Width,  in MM_TEXT client coordinates, of the destination rectangle
        ('nDstHeight', c_int),                  # [in/out] Height, in MM_TEXT client coordinates, of the destination rectangle
        ('pFrame', POINTER(TUCAM_FRAME))        # [in] the struct of camera frame
    ]


class TUCAM_FW_UPDATE(Structure):
    ''' the firmware update '''

    _fields_ = [
        ('nFwType', c_int),                     # [in] the format of firmware     see TUFW_TYPE
        ('pstrFwFile', c_char_p)                # [in] the path of firmware file
    ]


class TUCAM_POINT(Structure):
    ''' typedef struct point '''

    _fields_ = [
        ('nPtX', c_int),
        ('nPtY', c_int)
    ]


class TUCAM_IMG_HEADER(Structure):
    ''' define the struct of image header '''

    _fields_ = [
        ('szSignature', c_char * 8),            # [out]Copyright+Version: TU+1.0 ['T', 'U', '1', '\0']
        ('usHeader', c_ushort),                 # [in/out] The image header size
        ('usOffset', c_ushort),                 # [in/out] The image data offset
        ('usWidth', c_ushort),                  # [in/out] The image width
        ('usHeight', c_ushort),                 # [in/out] The image height
        ('uiWidthStep', c_uint),                # [in/out] The image width step
        ('ucDepth', c_ubyte),                   # [in/out] The image data depth (see from CV)
        ('ucFormat', c_ubyte),                  # [in/out] The image data format TUIMG_FORMAT
        ('ucChannels', c_ubyte),                # [in/out] The image data channels
        ('ucElemBytes', c_ubyte),               # [in/out] The image data bytes per element
        ('ucFormatGet', c_ubyte),               # [in] Which frame data format do you want
        ('uiIndex', c_uint),                    # [out] The image index number
        ('uiImgSize', c_uint),                  # [in/out] The image size
        ('uiRsdSize', c_uint),                  # [in/out] The image reserved size
        ('uiHstSize', c_uint),                  # [in/out] The image histogram size
        ('pImgData', POINTER(c_ubyte)),         # [in/out] Pointer to the image data
        ('pImgHist', POINTER(c_uint)),          # [in/out] Pointer to the image histogram data
        ('usLLevels', c_ushort),                # [out] The image left levels value
        ('usRLevels', c_ushort),                # [out] The image right levels value
        ('ucRsd1', c_byte * 64),                # The reserved
        ('dblExposure', c_double),              # [in/out] The exposure time
        ('ucRsd2', c_byte * 170),               # The reserved
        ('dblTimeStamp', c_double),             # [in/out] The time stamp
        ('dblTimeLast', c_double),              # [in/out] The time stamp last
        ('ucRsd3', c_byte * 32),                # The reserved
        ('ucGPSTimeStampYear', c_ubyte),        # [out] The GPS time stamp year
        ('ucGPSTimeStampMonth', c_ubyte),       # [out] The GPS time stamp month
        ('ucGPSTimeStampDay', c_ubyte),         # [out] The GPS time stamp day
        ('ucGPSTimeStampHour', c_ubyte),        # [out] The GPS time stamp hour
        ('ucGPSTimeStampMin', c_ubyte),         # [out] The GPS time stamp min
        ('ucGPSTimeStampSec', c_ubyte),         # [out] The GPS time stamp sec
        ('nGPSTimeStampNs', c_int),             # [out] The GPS time stamp ns
        ('ucRsd4', c_byte * 639)                # The reserved
    ]


class TUCAM_RAWIMG_HEADER(Structure):
    ''' Define the struct of raw image header '''

    _fields_ = [
        ('usWidth', c_ushort),                  # [in/out] The image width
        ('usHeight', c_ushort),                 # [in/out] The image height
        ('ucDepth', c_ubyte),                   # [in/out] The image data depth (see from CV)
        ('ucChannels', c_ubyte),                # [in/out] The image data channels
        ('ucElemBytes', c_ubyte),               # [in/out] The image data bytes per element
        ('uiIndex', c_uint),                    # [out] The image index number
        ('uiImgSize', c_uint),                  # [in/out] The image size
        ('dblExposure', c_double),              # [in/out] The exposure time
        ('pImgData', POINTER(c_ubyte)),         # [in/out] Pointer to the image data
        ('dblTimeStamp', c_double),             # [in/out] The time stamp
        ('dblTimeLast', c_double)               # [in/out] The time stamp last
    ]


########################


class NVILen(object):
    pass


class BUFFER_CALLBACK(object):
    pass
