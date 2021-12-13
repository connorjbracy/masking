from pkg_resources import resource_filename

from pyFAI.azimuthalIntegrator import AzimuthalIntegrator
import matplotlib.pyplot as plt
import fabio
import masking.tools as tools
import numpy as np

plt.ioff()

TIFF_FILE = resource_filename("masking", "data/image.tiff")
PONI_FILE = resource_filename("masking", "data/geo.poni")


def test_auto_mask():
    ai = AzimuthalIntegrator(dist=1., detector="Perkin", wavelength=0.1)
    img = np.zeros((3, 3))
    image, dct = tools.auto_mask(img, ai)
    assert isinstance(image, np.ndarray)
    assert isinstance(dct, dict)


def test_auto_mask_files(tmp_path):
    mask_file = tmp_path.joinpath("./mask.msk")
    tools.auto_mask_file(
        TIFF_FILE,
        PONI_FILE,
        str(mask_file),
        mask_setting={"alpha": 3.}
    )
    mask = fabio.open(str(mask_file)).data
    image = fabio.open(str(TIFF_FILE)).data
    masked_image = np.ma.masked_array(image, 1 - mask)
    del mask, image
    plt.imshow(masked_image)
    plt.colorbar()
    plt.show(block=False)
