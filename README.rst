=======
masking
=======

Python package for doing science.

* Free software: 3-clause BSD license
* Documentation: (COMING SOON!) https://st3107.github.io/masking.

Features
--------

Use it in default settings. Run the following function in a python script::

    from masking.tools import auto_mask_file

    auto_mask_file(
        "my_dark_subtracted_diffraction_image.tiff",
        "calibration_result_from_ceo2.poni",
        "auto_mask_result_to_save.msk"
    )



Use user defined settings. Run the following function in a python script::

    from masking.tools import auto_mask_file

    auto_mask_file(
        "my_dark_subtracted_diffraction_image.tiff",
        "calibration_result_from_ceo2.poni",
        "auto_mask_result_to_save.msk",
        mask_setting={"alpha": 3., "edge": 30, "lower_thresh": 1.0, "upper_thresh": 1e9}
    )

Use initial mask file provided by the user and user defined settings. Run the following function in a python script::

    from masking.tools import auto_mask_file

    auto_mask_file(
        "my_dark_subtracted_diffraction_image.tiff",
        "calibration_result_from_ceo2.poni",
        "auto_mask_result_to_save.msk",
        user_file="initial_mask_for_beam_stop.msk",
        mask_setting={"alpha": 3., "edge": 30, "lower_thresh": 1.0, "upper_thresh": 1e9}
    )

