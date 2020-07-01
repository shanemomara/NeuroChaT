# -*- coding: utf-8 -*-
"""
This module implements contains the default values of input parameters.

The input parameters are used by the Configuration Class for NeuroChaT software.
The parameters are defined as {key, {key, value}} pairs where the
1st key represent the analyse for which parameters are set.
The second {key, value} pairs represent the names of the parameters
and their values.

@author: Md Nurul Islam; islammn at tcd dot ie

"""
ANALYSES = {
    "wave_property": True,
    "isi": True,
    "isi_corr": True,
    "theta_cell": True,
    "theta_skip_cell": True,
    "burst": True,
    "speed": True,
    "ang_vel": True,
    "hd_rate": True,
    "hd_shuffle": True,
    "hd_time_lapse": True,
    "hd_time_shift": True,
    "loc_rate": True,
    "loc_shuffle": True,
    "loc_time_lapse": True,
    "loc_time_shift": True,
    "spatial_corr": True,
    "grid": True,
    "border": True,
    "gradient": True,
    "multiple_regression": True,
    "inter_depend": True,
    "lfp_spectrum": True,
    "spike_phase": True,
    "phase_lock": True,
    "lfp_spike_causality": False,
}

PARAMETERS = {
    "isi": {
        "isi_bin": 2,
        "isi_length": 350,
        "isi_refractory": 2,
    },
    "isi_corr": {
        "isi_corr_bin_long": 2,
        "isi_corr_len_long": 350,
        "isi_corr_bin_short": 1,
        "isi_corr_len_short": 10,
    },
    "theta_cell": {
        "isi_corr_bin_long": 2,
        "isi_corr_len_long": 350,
        "theta_cell_freq_max": 14.0,
        "theta_cell_freq_min": 4.0,
        "theta_cell_freq_start": 6.0,
        "theta_cell_tau1_max": 5.0,
        "theta_cell_tau1_start": 0.1,
        "theta_cell_tau2_max": 0.05,
        "theta_cell_tau2_start": 0.05,
    },
    "burst": {
        "burst_thresh": 5,
        "ibi_thresh": 50,
    },
    "speed": {
        "speed_bin": 1,
        "speed_max": 40,
        "speed_min": 0,
        "speed_rate_kern_len": 3,
    },
    "ang_vel": {
        "ang_vel_bin": 10,
        "ang_vel_cutoff": 10,
        "ang_vel_kern_len": 3,
        "ang_vel_max": 200,
        "ang_vel_min": -200,
    },
    "hd_rate": {
        "hd_bin": 5,
        "loc_pixel_size": 3,
        "hd_ang_vel_cutoff": 30,
        "hd_rate_kern_len": 5,
    },
    "hd_shuffle": {
        "hd_shuffle_limit": 0,
        "hd_shuffle_bins": 100,
        "hd_shuffle_total": 500,
    },
    "hd_time_shift": {
        "hd_shift_max": 10,
        "hd_shift_min": -10,
        "hd_shift_step": 1,
    },
    "loc_rate": {
        "loc_pixel_size": 3,
        "loc_chop_bound": 5,
        "loc_rate_filter": "Box",
        "loc_rate_kern_len": 5,
        "loc_field_thresh": 0.2,
        "loc_field_smooth": False,
        "loc_field_bins": 9,
        "loc_style": "contour",
        "loc_colormap": "viridis",
        "loc_contour_levels": 5
    },
    "loc_shuffle": {
        "loc_shuffle_limit": 0,
        "loc_shuffle_nbins": 100,
        "loc_shuffle_total": 500,
        "loc_pixel_size": 3,
        "loc_chop_bound": 5,
        "loc_rate_filter": "Box",
        "loc_rate_kern_len": 5,
    },
    "loc_time_lapse": {
        "loc_pixel_size": 3,
        "loc_chop_bound": 5,
        "loc_rate_filter": "Box",
        "loc_rate_kern_len": 5,
    },
    "loc_time_shift": {
        "loc_shift_max": 10,
        "loc_shift_min": -10,
        "loc_shift_step": 1,
        "loc_pixel_size": 3,
        "loc_chop_bound": 5,
        "loc_rate_filter": "Box",
        "loc_rate_kern_len": 5,
    },
    "spatial_corr": {
        "loc_pixel_size": 3,
        "loc_chop_bound": 5,
        "rot_corr_bin": 3,
        "spatial_corr_filter": "Box",
        "spatial_corr_kern_len": 5,
        "spatial_corr_min_obs": 20,
        "spatial_corr_style": "contour",
        "spatial_corr_colormap": "coolwarm",
        "spatial_corr_contour_levels": 10,
    },
    "grid": {
        "grid_ang_bin": 3,
        "grid_ang_tol": 2,
        "loc_pixel_size": 3,
        "loc_chop_bound": 5,
        "rot_corr_bin": 3,
        "spatial_corr_filter": "Box",
        "spatial_corr_kern_len": 5,
        "spatial_corr_min_obs": 20,
    },
    "border": {
        "border_ang_bin": 3,
        "border_firing_thresh": 0.1,
        "border_stair_steps": 5,
        "burst_thresh": 5,
        "loc_pixel_size": 3,
        "loc_chop_bound": 5,
        "loc_rate_filter": "Box",
        "loc_rate_kern_len": 5,
    },
    "gradient": {
        "grad_asymp_lim": 0.25,
        "grad_displace_lim": 0.25,
        "grad_growth_rate_lim": 0.5,
        "border_ang_bin": 3,
        "border_firing_thresh": 0.1,
        "border_stair_steps": 5,
        "burst_thresh": 5,
        "loc_pixel_size": 3,
        "loc_chop_bound": 5,
        "loc_rate_filter": "Box",
        "loc_rate_kern_len": 5,
    },
    "multiple_regression": {
        "mra_episode": 120,
        "mra_interval": 0.1,
        "mra_nrep": 1000,
    },
    "lfp_spectrum": {
        "lfp_prefilt_highcut": 40,
        "lfp_prefilt_lowcut": 1.5,
        "lfp_prefilt_order": 10,
        "lfp_pwelch_freq_max": 40,
        "lfp_pwelch_nfft": 1024,
        "lfp_pwelch_overlap": 1.0,
        "lfp_pwelch_seg_size": 2.0,
        "lfp_stft_freq_max": 40,
        "lfp_stft_nfft": 1024,
        "lfp_stft_overlap": 1.0,
        "lfp_stft_seg_size": 2.0,
        "lfp_spectrum_colormap": "magma",
        "lfp_lowband_lowcut": 1.5,
        "lfp_lowband_highcut": 4,
        "lfp_highband_lowcut": 5,
        "lfp_highband_highcut": 11,
        "lfp_band_win_len": 1.6,
    },
    "spike_phase": {
        "phase_amp_thresh": 0.15,
        "phase_bin": 5,
        "phase_freq_max": 12.0,
        "phase_freq_min": 6.0,
        "phase_loc_freq_max": 40,
        "phase_loc_nfft": 1024,
        "phase_power_thresh": 0.1,
        "phase_raster_bin": 2,
        "lfp_prefilt_highcut": 40,
        "lfp_prefilt_lowcut": 1.5,
        "lfp_prefilt_order": 10,
    },
    "phase_lock": {
        "phase_loc_freq_max": 40,
        "phase_loc_nfft": 1024,
        "phase_loc_win_low": -0.4,
        "phase_loc_win_up": 0.4,
        "phase_power_thresh": 0.1,
        "phase_raster_bin": 2,
    },
}
