#!/usr/bin/env python


from netCDF4 import Dataset
import datetime
import glob
import os
import numpy as np
import json

class NetCDFTools(object):
    
    def toJSON(variable="temp_mean", 
        start_date="20140101", end_date="20140131"):

        """ This function receives a time frame and produces a json version of
        the data stored at the netcdf repository.  """

        data_home = os.environ.get('DATA_HOME')
    
        start_date = datetime.datetime.strptime(start_date, "%Y%m%d").date()
    
        end_date = datetime.datetime.strptime(end_date, "%Y%m%d").date()
    
        data_files = glob.glob("%s/*.cdf" %(data_home))
        filtered_data = []
        for file_name in data_files:
            file_date = datetime.datetime.strptime(
                file_name.split('.')[2],"%Y%m%d").date()
            if file_date >= start_date and file_date <= end_date:
                file_obj = Dataset(file_name)
                date_value = {}
                variable_value = np.mean(file_obj.variables[variable][:])
                date_value["date"] = file_date.isoformat()
                date_value["value"] = np.asscalar(variable_value)
                filtered_data.append(date_value)
    
        return json.dumps(filtered_data)


def main():
    print(NetCDFTools.toJSON("temp_mean", "20151015", "20151115"))


if __name__ == '__main__':
    main()
