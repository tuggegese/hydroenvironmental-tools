# Elliptic To Geoid
Transforms elliptic coordinates with the GRS80 Geoid. 

Example use:

```from toolbox.converters.elliptictoGK.elliptictoGK import Measurement```

```measurement = Measurement()```

```infile = r'C:\input_example.txt'```

```outfile = r'C:\projected_coordinates.txt```

```geoid_model = r'C:\GEOID_GRS80_Oesterreich.csv'```

```latrange = [16,31]```

```lonrange = [33,48]```

```zrange = [52,59]```

```skip_header = 1```

```inEPSG = 'epsg:4326'```

```outEPSG = 'epsg:32633'```

```measurement.define_inpath(infile)```

```measurement.define_outpath(outfile)```

```measurement.define_geoid(geoid_model)```

```measurement.set_epsg_in(inEPSG)```

```measurement.set_epsg_out(outEPSG)```

```measurement.check_range(latrange,lonrange,zrange,skip_header)```

```measurement.read_lat_lon(latrange,lonrange,zrange,skip_header)```

```measurement.reproject_1D()```

```measurement.reproject_2D()```

```measurement.write_output(measurement.x_out,measurement.y_out,measurement.z_out)```




