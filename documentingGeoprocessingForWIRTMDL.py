import arcpy

# 1. Filename: MCD_Urban_Union_WRB2mi.shp 
# SDEDNR.EN_MCD_MULTI_CNTY_AR_VAR.shp
# Union with
# WRB_UrbanArea_2010Census.shp
MCD = "C:/path/to/SDEDNR.EN_MCD_MULTI_CNTY_AR_VAR.shp"
WRB = "C:/path/to/WRB_UrbanArea_2010Census.shp"
outUnion = "C:/path/to/MCD_Urban_Union_WRB2mi.shp"
arcpy.Union_analysis(MCD, WRB, outUnion)

# Attributes Fields Added by ADH:
# Urban_Ar_3:  1= Urban, 0=Not urban 
# CV: 1= City or Village, 0=Town
# SLAMM Model: 1 or 2 = are to include in SLAMM Model, 0=not in SLAMM Model

arcpy.AddField_management(outUnion, "Urban_AR_3", "SHORT", 2, "", "", "", "NULLABLE")
arcpy.AddField_management(outUnion, "CV", "SHORT", 2, "", "", "", "NULLABLE")

####################################################
# Do some manual attribution of Urban, city, village
####################################################

# 2. Filename: MCD_Urban_Union_WRB2mi_Dsslv.shp
# Dissolved contiguous features of MCD_Urban_Union_WRB2mi.shp 

outDissolve = "C:/path/to/MCD_Urban_Union_WRB2mi.shp"
arcpy.Dissolve_management(outUnion, outDissolve, "Urban_AR_3", "", "MULTI_PART")

# 3. Filename: ssurgoWIR.gdb (Mapunits feature class)
# SSURGO soil polygons clipped to WI River basin 2-mile buffer

boundary = "C:/path/to/WRB_Basin_2mile_Buffer.shp"
ssurgo = "C:/path/to/ssurgo.gdb/Mapunits"
outSsurgo = "C:/path/to/ssurgoWIR.gdb/Mapunits"
arcpy.Clip_analysis(ssurgo, boundary, outSsurgo)

# 4. Filename: Soils_SLAMMAreaClip.shp
# ssurgoWIR.gdb (Mapunits)
# clipped to
# MCD_Urban_Union_WRB2mi .shp

urbanSsurgo = "C:/path/to/ssurgoWIR.gdb/urbanSoils"
arcpy.Clip_analysis(outSsurgo, outUnion, urbanSoils)


