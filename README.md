# wds2015
Project developed during the First Workshop on Data Science.



# API Usage
The main service method `toJSON()` receives 3 parameters, a data frame specified as:

* Date: "YYYYMMDD.hhmmss"
* Variable: One of the following variables


## Available Variables

int32 base_time() 
    string: 2014-07-18 00:00:00 0:00 
    long_name: Base time in Epoch 
    units: seconds since 1970-1-1 0:00:00 0:00 
 
 
 
 
float64 time_offset(time) 
    long_name: Time offset from base_time 
    units: seconds since 2014-07-18 00:00:00 0:00 
 
 
 
 
float64 time(time) 
    long_name: Time offset from midnight 
    units: seconds since 2014-07-18 00:00:00 0:00 
    standard_name: time 
 
 
 
 
float32 atmos_pressure(time) 
    long_name: Atmospheric pressure 
    units: kPa 
    valid_min: 85.0 
    valid_max: 103.0 
    valid_delta: 1.0 
    missing_value: -9999.0 
 
 
 
 
int32 qc_atmos_pressure(time) 
    long_name: Quality check results on field: Atmospheric pressure 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
float32 temp_mean(time) 
    long_name: Temperature mean 
    units: degC 
    valid_min: 0.0 
    valid_max: 50.0 
    valid_delta: 20.0 
    missing_value: -9999.0 
 
 
 
 
int32 qc_temp_mean(time) 
    long_name: Quality check results on field: Temperature mean 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
float32 temp_std(time) 
    long_name: Temperature standard deviation 
    units: degC 
 
 
 
 
float32 rh_mean(time) 
    long_name: Relative humidity mean 
    units: % 
    valid_min: 0.0 
    valid_max: 104.0 
    valid_delta: 30.0 
    missing_value: -9999.0 
 
 
 
 
int32 qc_rh_mean(time) 
    long_name: Quality check results on field: Relative humidity mean 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
float32 rh_std(time) 
    long_name: Relative humidity standard deviation 
    units: % 
 
 
 
 
float32 vapor_pressure_mean(time) 
    long_name: Vapor pressure mean, calculated 
    units: kPa 
    valid_min: 0.0 
    valid_max: 10.0 
    valid_delta: 1.0 
    missing_value: -9999.0 
 
 
 
 
int32 qc_vapor_pressure_mean(time) 
    long_name: Quality check results on field: Vapor pressure mean, calculated 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
float32 vapor_pressure_std(time) 
    long_name: Vapor pressure standard deviation 
    units: kPa 
 
 
 
 
float32 wspd_arith_mean(time) 
    long_name: Wind speed arithmetic mean 
    units: m/s 
    valid_min: 0.0 
    valid_max: 60.0 
    valid_delta: 20.0 
    missing_value: -9999.0 
 
 
 
 
int32 qc_wspd_arith_mean(time) 
    long_name: Quality check results on field: Wind speed arithmetic mean 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
float32 wspd_vec_mean(time) 
    long_name: Wind speed vector mean 
    units: m/s 
    valid_min: 0.0 
    valid_max: 60.0 
    valid_delta: 20.0 
    missing_value: -9999.0 
 
 
 
 
int32 qc_wspd_vec_mean(time) 
    long_name: Quality check results on field: Wind speed vector mean 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
float32 wdir_vec_mean(time) 
    long_name: Wind direction vector mean 
    units: degree 
    valid_min: 0.0 
    valid_max: 360.0 
    missing_value: -9999.0 
 
 
 
 
int32 qc_wdir_vec_mean(time) 
    long_name: Quality check results on field: Wind direction vector mean 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
float32 wdir_vec_std(time) 
    long_name: Wind direction vector mean standard deviation 
    units: degree 
    missing_value: -9999.0 
 
 
 
 
float32 org_precip_rate_mean(time) 
    long_name: ORG precipitation rate mean 
    units: mm/hr 
    valid_min: 0.0 
    valid_max: 500.0 
    missing_value: -9999.0 
 
 
 
 
int32 qc_org_precip_rate_mean(time) 
    long_name: Quality check results on field: ORG precipitation rate mean 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
float32 org_precip_rate_max(time) 
    long_name: ORG precipitation rate maximum 
    units: mm/hr 
    valid_min: 0.0 
    valid_max: 500.0 
    missing_value: -9999.0 
 
 
 
 
int32 qc_org_precip_rate_max(time) 
    long_name: Quality check results on field: ORG precipitation rate maximum 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
    flag_method: bit 
 
 
 
 
float32 org_precip_rate_min(time) 
    long_name: ORG precipitation rate minimum 
    units: mm/hr 
    valid_min: 0.0 
    valid_max: 500.0 
    missing_value: -9999.0 
 
 
 
 
int32 qc_org_precip_rate_min(time) 
    long_name: Quality check results on field: ORG precipitation rate minimum 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
    flag_method: bit 
 
 
 
 
float32 org_precip_rate_std(time) 
    long_name: ORG precipitation rate standard deviation 
    units: mm/hr 
    missing_value: -9999.0 
 
 
 
 
int32 pwd_err_code(time) 
    long_name: PWD alarm 
    units: unitless 
    missing_value: -9999 
 
 
 
 
int32 pwd_mean_vis_1min(time) 
    long_name: PWD 1 minute mean visibility 
    units: m 
    valid_min: 0 
    valid_max: 20000 
    missing_value: -9999 
 
 
 
 
int32 qc_pwd_mean_vis_1min(time) 
    long_name: Quality check results on field: PWD 1 minute mean visibility 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
int32 pwd_mean_vis_10min(time) 
    long_name: PWD 10 minute mean visibility 
    units: m 
    valid_min: 0 
    valid_max: 20000 
    missing_value: -9999 
 
 
 
 
int32 qc_pwd_mean_vis_10min(time) 
    long_name: Quality check results on field: PWD 10 minute mean visibility 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
int32 pwd_pw_code_inst(time) 
    long_name: PWD instantaneous present weather code 
    units: unitless 
    valid_min: 0 
    valid_max: 99 
    missing_value: -9999 
 
 
 
 
int32 qc_pwd_pw_code_inst(time) 
    long_name: Quality check results on field: PWD instantaneous present weather code 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
int32 pwd_pw_code_15min(time) 
    long_name: PWD 15 minute present weather code 
    units: unitless 
    valid_min: 0 
    valid_max: 99 
    missing_value: -9999 
 
 
 
 
int32 qc_pwd_pw_code_15min(time) 
    long_name: Quality check results on field: PWD 15 minute present weather code 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
int32 pwd_pw_code_1hr(time) 
    long_name: PWD 1 hour present weather code 
    units: unitless 
    valid_min: 0 
    valid_max: 99 
    missing_value: -9999 
 
 
 
 
int32 qc_pwd_pw_code_1hr(time) 
    long_name: Quality check results on field: PWD 1 hour present weather code 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
float32 pwd_precip_rate_mean_1min(time) 
    long_name: PWD 1 minute mean precipitation rate 
    units: mm/hr 
    valid_min: 0.0 
    valid_max: 999.99 
    valid_delta: 100.0 
    missing_value: -9999.0 
 
 
 
 
int32 qc_pwd_precip_rate_mean_1min(time) 
    long_name: Quality check results on field: PWD 1 minute mean precipitation rate 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
float32 pwd_cumul_rain(time) 
    long_name: PWD cumulative liquid precipitation 
    units: mm 
    valid_min: 0.0 
    valid_max: 99.99 
    valid_delta: 50.0 
    missing_value: -9999.0 
 
 
 
 
int32 qc_pwd_cumul_rain(time) 
    long_name: Quality check results on field: PWD cumulative liquid precipitation 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
float32 logger_volt(time) 
    long_name: Logger voltage 
    units: V 
    missing_value: -9999.0 
    valid_min: 10.0 
    valid_max: 15.0 
    valid_delta: 5.0 
 
 
 
 
int32 qc_logger_volt(time) 
    long_name: Quality check results on field: Logger voltage 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
float32 logger_temp(time) 
    long_name: Logger temperature 
    units: degC 
    missing_value: -9999.0 
    valid_min: 0.0 
    valid_max: 50.0 
    valid_delta: 10.0 
 
 
 
 
int32 qc_logger_temp(time) 
    long_name: Quality check results on field: Logger temperature 
    units: unitless 
    description: See global attributes for individual bit descriptions. 
 
 
 
 
float32 lat() 
    long_name: North latitude 
    units: degree_N 
    valid_min: -90.0 
    valid_max: 90.0 
    standard_name: latitude 
 
 
 
 
float32 lon() 
    long_name: East longitude 
    units: degree_E 
    valid_min: -180.0 
    valid_max: 180.0 
    standard_name: longitude 
 
 
 
 
float32 alt() 
    long_name: Altitude above mean sea level 
    units: m 
    standard_name: altitude 
 





