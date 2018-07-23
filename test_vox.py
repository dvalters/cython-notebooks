import voxelise_modis_burned_area as vox
import numpy as np

one_month_data = np.load("test_arrays.npz_FILES/one_month_data.npy")
voxelspace = np.load("test_arrays.npz_FILES/voxelspace.npy")

myvox = vox.voxelspace(voxelspace, one_month_data)
print type(myvox)
print myvox
