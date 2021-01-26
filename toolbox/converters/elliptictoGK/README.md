# Elliptic To Geoid
Transfroms elliptic coordinates with the GRS80 Geoid. 

Example use:

from toolbox.converters.elliptictoGK.elliptictoGK import Measurement

initialize class if not present yet

```measurement = Measurement()```

Define user specific variables
input coordinate file

```infile = r'C:\original_coordinates.txt'```

output coordinate file

```outfile = r'C:\projected_coordinates.txt```

geoid model

```geoid_model = r'C:\GEOID_GRS80_Oesterreich.csv'```

define the position of the lat coordinate within one line

```latrange = [16,31]```

define the position of the lon coordinate within one line

```lonrange = [33,48]```

define the position of the z coordinate within one line

```zrange = [52,59]```

number of headers in the file

```skip_header = 1```

projection of original file

```inEPSG = 'epsg:4326'```

desirect coordinate system

```outEPSG = 'epsg:32633'```

set variables in the class

```measurement.define_inpath(infile)```

```measurement.define_outpath(outfile)```

```measurement.define_geoid(geoid_model)```

```measurement.set_epsg_in(inEPSG)```

```measurement.set_epsg_out(outEPSG)```

now the range of the variables has to be ckecked by checking the output.
If the range is okay the variables can be read

```measurement.check_range(latrange,lonrange,zrange,skip_header)```

read measurements

```measurement.read_lat_lon(latrange,lonrange,zrange,skip_header)```

reproject 1D and 2D coordinates

```measurement.reproject_1D()```

```measurement.reproject_2D()```

write the output to the files

```measurement.write_output(measurement.x_out,measurement.y_out,measurement.z_out)```




