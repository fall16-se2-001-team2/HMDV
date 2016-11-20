import rasterio
from rasterio.tools.mask import mask
from countyHandler import countyHandler

print("start")
print(countyHandler.get_county("cocke").nameFull)
print(countyHandler.get_county("washington").nameFull)
print(countyHandler.get_county("van buren").nameFull)

geoms = []
geoms.append(countyHandler.get_county("sullivan").geo)
#geoms.append(countyHandler.get_county("washington").geo)
geoms.append(countyHandler.get_county("unicoi").geo)


# load the raster, mask it by the polygon and crop it
with rasterio.open("/home/jacob/python/SeiiData/gpw-v4-population-density_2015.tif") as src:
    out_image, out_transform = mask(src, geoms, crop=True)
out_meta = src.meta.copy()

# save the resulting raster  
out_meta.update({"driver": "GTiff",
    "height": out_image.shape[1],
    "width": out_image.shape[2],
"transform": out_transform})

with rasterio.open("masked.tif", "w", **out_meta) as dest:
    dest.write(out_image)


print("end")
