import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

data_fasilitas = {
    'nama_fasilitas': ['Taman Sentral A', 'Taman Wilayah B', 'Taman Publik C'],
    'kategori': ['Rekreasi', 'Olahraga', 'Edukasi'],
    'geometry': [
        Point(102.2655, -3.7956),
        Point(102.2712, -3.7901),
        Point(102.2580, -3.8020)
    ]
}
gdf = gpd.GeoDataFrame(data_fasilitas, crs="EPSG:4326")
gdf_proj = gdf.to_crs(epsg=32748)
gdf_proj['buffer_area'] = gdf_proj.geometry.buffer(500)
gdf_buffer = gdf_proj.set_geometry('buffer_area').to_crs(epsg=4326)
gdf_buffer['luas_cakupan_m2'] = gdf_proj['buffer_area'].area
gdf_buffer.to_file("cakupan_taman_kota.geojson", driver="GeoJSON")
print("Proses otomatisasi selesai. File GeoJSON berhasil dibuat!")
fig, ax = plt.subplots(figsize=(7, 7))
gdf_buffer.plot(ax=ax, color='lightblue', edgecolor='blue', alpha=0.5, label='Radius 500m')
gdf.plot(ax=ax, color='red', marker='o', markersize=40, label='Titik Aset')
plt.title("Otomatisasi Analisis Buffer GIS (Smart Cities)")
plt.legend()
plt.show()
