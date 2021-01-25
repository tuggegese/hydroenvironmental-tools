# -*- coding: utf-8 -*-
"""
Name: elliptictogeoid.py

Brief: converts elliptic coordinates to geoid coordinates
    
Author: Sebastian Gegenleithner

Example use of the class:
    
# initialize class if not present yet
measurement = Measurement()

# Define user specific variables
# input coordinate file
infile = r'C:\original_coordinates.txt'
# output coordinate file
outfile = r'C:\projected_coordinates.txt'
# geoid model
geoid_model = r'C:\GEOID_GRS80_Oesterreich.csv'

# define the position of the lat coordinate within one line
latrange = [16,31]
# define the position of the lon coordinate within one line
lonrange = [33,48]
# define the position of the z coordinate within one line
zrange = [52,59]
# number of headers in the file
skip_header = 1

# projection of original file
inEPSG = 'epsg:4326'
# desirect coordinate system
outEPSG = 'epsg:32633'

# set variables in the class
measurement.define_inpath(infile)
measurement.define_outpath(outfile)
measurement.define_geoid(geoid_model)
measurement.set_epsg_in(inEPSG)
measurement.set_epsg_out(outEPSG)

# now the range of the variables has to be ckecked by checking the output.
# If the range is okay the variables can be read
measurement.check_range(latrange,lonrange,zrange,skip_header)
# read measurements
measurement.read_lat_lon(latrange,lonrange,zrange,skip_header)

# reproject 1D and 2D coordinates
measurement.reproject_1D()
measurement.reproject_2D()

# write the output to the files
measurement.write_output(measurement.x_out,measurement.y_out,measurement.z_out)
    
"""

import pyproj
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
from matplotlib import tri

class Measurement(object):
    def __init__(self):
        # filepaths
        self.infile = r''
        self.outfile = r''
		# use geoid default
        self.geoid = r'Geoid/GEOID_GRS80_Oesterreich.csv'
        # lat/lon in 
        self.lat_in = []
        self.y_out = []
        self.lon_in = []
        self.x_out = []
        # hight in
        self.z_in = []
        self.z_out = []
        # epsg codes
        self.epsg_in = r''
        self.epsg_out = r''
    def define_inpath(self, filepath):
        self.infile = filepath
    def define_outpath(self,filepath):
        self.outfile = filepath
    def define_geoid(self,filepath):
        self.geoid = filepath
    def set_epsg_in(self,string):
        self.epsg_in = string
    def set_epsg_out(self,string):
        self.epsg_out = string
    def check_range(self,latrange,lonrange,zrange,skip_header):
        i = 0
        with open(self.infile) as f:
            for line in f:
                if i == skip_header:
                    print('Check variables')
                    print(line[latrange[0]:latrange[1]])
                    print(line[lonrange[0]:lonrange[1]])
                    print(line[zrange[0]:zrange[1]])
                i = i+1
            
    def read_lat_lon(self,latrange,lonrange,zrange, skip_header):
        i = 0
        with open(self.infile) as f:
            for line in f:
                if i>=skip_header:
                    # add lat
                    lat_string = line[latrange[0]:latrange[1]]
                    lat_degree = float(lat_string[2:4])
                    lat_minutes = float(lat_string[5:7])
                    lat_seconds = float(lat_string[8:14])
                    self.lat_in.append(lat_degree+lat_minutes/60.+lat_seconds/3600.)
                    # add lon
                    lon_string = line[lonrange[0]:lonrange[1]]
                    lon_degree = float(lon_string[2:4])
                    lon_minutes = float(lon_string[5:7])
                    lon_seconds = float(lon_string[8:14])
                    self.lon_in.append(lon_degree+lon_minutes/60.+lon_seconds/3600.)
                    # add z coordinate
                    z_coord = float(line[zrange[0]:zrange[1]])
                    self.z_in.append(z_coord) 
                i+=1
    def reproject_1D(self):
        # read geoid model
        geoid_model = np.genfromtxt(self.geoid, skip_header = 1,delimiter = ';')
        # triangulate geoid
        triang = tri.Triangulation(geoid_model[:,1],geoid_model[:,0])
        # create linear interpolator object
        interpolator = tri.LinearTriInterpolator(triang,geoid_model[:,2])

        # reproject elevations
        for i in range(0,len(self.z_in)):
            lon_i = self.lon_in[i]
            lat_i = self.lat_in[i]
            n_i = float(interpolator(lon_i,lat_i))
            self.z_out.append(self.z_in[i] - n_i)
    def reproject_2D(self):
        inProj = pyproj.Proj(init=self.epsg_in)
        outProj = pyproj.Proj(init=self.epsg_out)
        self.x_out,self.y_out = pyproj.transform(inProj,outProj,self.lon_in,self.lat_in)
    def write_output(self, x,y,z):
        f = open(self.outfile, 'w')
        
        for i in range(0,len(x)):
            f.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + '\n')
        
        f.close()
        
measurement = Measurement()