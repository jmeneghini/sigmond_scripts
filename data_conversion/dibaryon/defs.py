from collections import namedtuple

Ensemble = namedtuple('Ensemble', ['name', 'dir_name', 'type', 'su3', 'open', 'flow', 'Nt', 'replica', 'replica_str', 'modes', 'srcs', 't0', 'ts'])
Channel = namedtuple('Channel', ['P', 'irrep', 'flavor'])

# ensemble info
ensembles = [
    Ensemble("Scls_cls_A653", "A653", 'Scls_cls', True, False, 'flow_t1.0', 48, ('r000',), 'r000', 32, 8, 0, 24),
    Ensemble("Scls_cls_A653_t0.125", "A653", 'Scls_cls', True, False, 'flow_t0.125', 48, ('r000',), 'r000', 32, 8, 0, 24),
    Ensemble("Scls_cls_B450", "B450", 'Scls_cls', True, False, 'flow_t1.0', 64, ('r000',), 'r000', 32, 8, 0, 32),
    Ensemble("mdwf_cls_A653", "A653", 'mdwf_cls', True, False, 'flow_t1.0', 48, ('r000',), 'r000', 32, 8, 0, 24),
    Ensemble("mdwf_cls_A653_t0.4", "A653", 'mdwf_cls', True, False, 'flow_t0.4', 48, ('r000',), 'r000', 32, 8, 0, 24),
    Ensemble("mdwf_cls_B450", "B450", 'mdwf_cls', True, False, 'flow_t1.0', 64, ('r000',), 'r000', 32, 8, 0, 32),
    Ensemble("mdwf_cls_H101_r000", "H101", 'mdwf_cls', True, True, 'flow_t1.0', 96, ('r000',), 'r000', 48, 4, 0, 32),
    Ensemble("mdwf_cls_H101", "H101", 'mdwf_cls', True, True, 'flow_t1.0', 96, ('r000','r001',), 'r000-001', 48, 4, 0, 24),
    Ensemble("mdwf_hisq_a15m400trMc_a", "a15m400trMc_a", 'mdwf_hisq', True, False, 'flow_t1.0', 48, ('',), '', 60, 8, 0, 16),
    Ensemble("mdwf_hisq_a12m400trMc_a", "a12m400trMc_a", 'mdwf_hisq', True, False, 'flow_t1.0', 64, ('',), '', 54, 8, 0, 20),
    Ensemble("mdwf_hisq_a09m400trMc_a", "a09m400trMc_a", 'mdwf_hisq', True, False, 'flow_t1.0', 96, ('',), '', 54, 8, 0, 28),
    Ensemble("mdwf_hisq_a06m400trMc_a", "a06m400trMc_a", 'mdwf_hisq', True, False, 'flow_t1.0', 144, ('',), '', 46, 8, 0, 44),
    Ensemble("exp_a064_m400_mL6.4_trMc", "a064_m400_mL6.4_trMc", 'exp', True, False, '', 96, ('_1','_2',), '1-2', 68, 8, 0, 40),
    Ensemble("exp_a094_m400_mL6.0_trMc", "a094_m400_mL6.0_trMc", 'exp', True, False, '', 96, ('','_ext',), 'extp', 64, 8, 0, 24),
    Ensemble("exp_a12_m400_mL6.0_trMc", "a12_m400_mL6.0_trMc", 'exp', True, False, '', 96, ('',), '', 54, 8, 0, 20),
    Ensemble("cls_A653", "A653", 'cls', True, False, '', 48, ('r000',), 'r000', 32, 4, 0, 24),
    Ensemble("cls_B450", "B450", 'cls', True, False, '', 64, ('r000',), 'r000', 32, 8, 0, 32),
    Ensemble("cls_B451", "B451", 'cls', False, False, '', 64, ('r000',), 'r000', 32, 4, 0, 32),
    Ensemble("cls_B452", "B452", 'cls', False, False, '', 64, ('r000',), 'r000', 32, 4, 0, 32),
    Ensemble("cls_H101", "H101", 'cls', True, True, '', 96, ('r000','r001',), 'r000-001', 48, 4, 0, 24),
    Ensemble("cls_H102", "H102", 'cls', False, True, '', 96, ('r001','r002',), 'r001-002', 48, 4, 0, 24),
    Ensemble("cls_H107", "H107", 'cls', False, True, '', 96, ('r000','r001','r002','r003','r004','r005'), 'r000-005', 48, 4, 0, 24),
    Ensemble("cls_H200", "H200", 'cls', True, True, '', 96, ('r000','r001'), 'r000-001', 20, 8, 0, 32),
    Ensemble("mdwf_cls_H200", "H200", 'mdwf_cls', True, True, 'flow_t1.0', 96, ('r000','r001'), 'r000-001', 20, 8, 0, 32),
    #Ensemble("cls_J500", "J500", 'cls', True, True, '', 192, ('r004','r005'), 'r004-005', 36, 12, 0, 56),
    Ensemble("cls_J500", "J500_sm2", 'cls', True, True, '', 192, ('r004','r005','r006'), 'r004-006', 36, 12, 0, 56),
    Ensemble("cls_N200", "N200", 'cls', False, True, '', 128, ('r000','r001'), 'r000-001', 68, 8, 0, 32),
    Ensemble("cls_N202", "N202", 'cls', True, True, '', 128, ('r001',), 'r001', 68, 8, 0, 32),
    Ensemble("cls_N300", "N300", 'cls', True, True, '', 128, ('r001','r002'), 'r001-002', 32, 12, 0, 40),
    Ensemble("cls_N451", "N451", 'cls', False, False, '', 128, ('r000',), 'r000', 108, 8, 0, 32),
    Ensemble("cls_U102", "U102", 'cls', False, True, '', 128, ('r001', 'r002',), 'r001-002', 20, 5, 0, 24),
    Ensemble("cls_U103", "U103", 'cls', True, True, '', 128, ('r001','r002','r003',), 'r001-003', 20, 5, 0, 24),
    #Ensemble("cls_U103", "U103_60modes", "U103", 'cls', True, True, '', 128, ('r001','r002','r003',), 'r001-003', 60, 5, 0, 24),
    #Ensemble("cls_U103", "U103_4", "U103", 'cls', True, True, '', 128, ('r001','r002','r003',), 'r001-003', 20, 5, 0, 24),
    Ensemble("cls_E1", "E1", 'cls', True, False, '', 64, ('',), '', 30, 8, 0, 32),
    Ensemble("cls_E5", "E5_SU3", 'cls', True, False, '', 64, ('f', 'g',), 'fg', 30, 4, 0, 32),
]

backward_prop_skip = {
    'Scls_cls_A653': [],
    'Scls_cls_A653_t0.125': [],
    'Scls_cls_B450': [],
    'mdwf_cls_A653': [],
    'mdwf_cls_A653_t0.4': [],
    'mdwf_cls_B450': [],
    'mdwf_cls_H101_r000': [0],
    'mdwf_cls_H101': [0],
    'mdwf_cls_H200': [0,1,2,3],
    'a15m400trMc_a': [],
    'a12m400trMc_a': [],
    'a09m400trMc_a': [],
    'a06m400trMc_a': [],
    'a064_m400_mL6.4_trMc': [],
    'a094_m400_mL6.0_trMc': [],
    'a12_m400_mL6.0_trMc': [],
    'A653': [],
    'B450': [],
    'B451': [],
    'B452': [],
    'H101': [0],
    'H102': [0],
    'H107': [0],
    'H200': [0,1,2,3],
    'J500': [0,1,2,3],
    'N200': [0,1],
    'N202': [0,1],
    'N300': [0,1,2,3,4,5],
    'N451': [],
    'U102': [0],
    'U103': [0],
    'U103_60modes': [0],
    'U103_4': [0],
    'E1':   [],
    'E5':   [],
}

forward_prop_skip = {
    'Scls_cls_A653': [],
    'Scls_cls_A653_t0.125': [],
    'Scls_cls_B450': [],
    'mdwf_cls_A653': [],
    'mdwf_cls_A653_t0.4': [],
    'mdwf_cls_B450': [],
    'mdwf_cls_H101_r000': [3],
    'mdwf_cls_H101': [3],
    'mdwf_cls_H200': [4,5,6,7],
    'a15m400trMc_a': [],
    'a12m400trMc_a': [],
    'a09m400trMc_a': [],
    'a06m400trMc_a': [],
    'a064_m400_mL6.4_trMc': [],
    'a094_m400_mL6.0_trMc': [],
    'a12_m400_mL6.0_trMc': [],
    'A653': [],
    'B450': [],
    'B451': [],
    'B452': [],
    'H101': [3],
    'H102': [3],
    'H107': [3],
    'H200': [4,5,6,7],
    'J500': [8,9,10,11],
    'N200': [6,7],
    'N202': [6,7],
    'N300': [6,7,8,9,10,11],
    'N451': [],
    'U102': [4],
    'U103': [4],
    'U103_60modes': [4],
    'U103_4': [4],
    'E1':   [],
    'E5':   [],
}

pseudoscalar_backward_prop_skip = {
    'Scls_cls_A653': [],
    'Scls_cls_A653_t0.125': [],
    'Scls_cls_B450': [],
    'mdwf_cls_A653': [],
    'mdwf_cls_A653_t0.4': [],
    'mdwf_cls_B450': [],
    'mdwf_cls_H101_r000': [0,1],
    'mdwf_cls_H101': [0,1],
    'mdwf_cls_H200': [0,1,2,3,4,5],
    'a15m400trMc_a': [],
    'a12m400trMc_a': [],
    'a09m400trMc_a': [],
    'a06m400trMc_a': [],
    'a064_m400_mL6.4_trMc': [],
    'a094_m400_mL6.0_trMc': [],
    'a12_m400_mL6.0_trMc': [],
    'A653': [],
    'B450': [],
    'B451': [],
    'B452': [],
    'H101': [0,1],
    'H102': [0,1],
    'H107': [0,1],
    'H200': [0,1,2,3,4,5],
    'J500': [0,1,2,3,4,5],
    'N200': [0,1,2],
    'N202': [0,1,2],
    'N300': [0,1,2,3,4,5,6,7],
    'N451': [],
    'U102': [0,1],
    'U103': [0,1],
    'U103_60modes': [0,1],
    'U103_4': [0,1],
    'E1':   [],
    'E5':   [],
}

pseudoscalar_forward_prop_skip = {
    'Scls_cls_A653': [],
    'Scls_cls_A653_t0.125': [],
    'Scls_cls_B450': [],
    'mdwf_cls_A653': [],
    'mdwf_cls_A653_t0.4': [],
    'mdwf_cls_B450': [],
    'mdwf_cls_H101_r000': [2,3],
    'mdwf_cls_H101': [2,3],
    'mdwf_cls_H200': [2,3,4,5,6,7],
    'a15m400trMc_a': [],
    'a12m400trMc_a': [],
    'a09m400trMc_a': [],
    'a06m400trMc_a': [],
    'a064_m400_mL6.4_trMc': [],
    'a094_m400_mL6.0_trMc': [],
    'a12_m400_mL6.0_trMc': [],
    'A653': [],
    'B450': [],
    'B451': [],
    'B452': [],
    'H101': [2,3],
    'H102': [2,3],
    'H107': [2,3],
    'H200': [2,3,4,5,6,7],
    'J500': [6,7,8,9,10,11],
    'N200': [5,6,7],
    'N202': [5,6,7],
    'N300': [4,5,6,7,8,9,10,11],
    'N451': [],
    'U102': [3,4],
    'U103': [3,4],
    'U103_60modes': [3,4],
    'U103_4': [3,4],
    'E1':   [],
    'E5':   [],
}


pseudoscalar_modes = {
    'Scls_cls_A653': 32,
    'Scls_cls_A653_t0.125': 32,
    'Scls_cls_B450': 32,
    'mdwf_cls_A653': 32,
    'mdwf_cls_A653_t0.4': 32,
    'mdwf_cls_B450': 32,
    'mdwf_cls_H101_r000': 48,
    'mdwf_cls_H101': 48,
    'mdwf_cls_H200': 20,
    'a15m400trMc_a': 60,
    'a12m400trMc_a': 54,
    'a09m400trMc_a': 54,
    'a06m400trMc_a': 46,
    'a064_m400_mL6.4_trMc': 68,
    'a094_m400_mL6.0_trMc': 64,
    'a12_m400_mL6.0_trMc': 54,
    'A653': 32,
    'B450': 32,
    'B451': 32,
    'B452': 32,
    'H101': 144,
    'H102': 72,
    'H107': 48,
    'H200': 20,
    'J500': 36,
    'N200': 68,
    'N202': 68,
    'N300': 32,
    'N451': 108,
    'U102': 20,
    'U103': 20,
    'U103_60modes': 60,
    'U103_4': 20,
    'E1':   56,
    'E5':   60,
}

pseudoscalar_sources = {
    'Scls_cls_A653': [0, 0, 0, 0, 0, 0, 0, 0],
    'Scls_cls_A653_t0.125': [0, 0, 0, 0, 0, 0, 0, 0],
    'Scls_cls_B450': [0, 0, 0, 0, 0, 0, 0, 0],
    'mdwf_cls_A653': [0, 0, 0, 0, 0, 0, 0, 0],
    'mdwf_cls_A653_t0.4': [0, 0, 0, 0, 0, 0, 0, 0],
    'mdwf_cls_B450': [0, 0, 0, 0, 0, 0, 0, 0],
    'mdwf_cls_H101_r000': [0, 0, 0, 0],
    'mdwf_cls_H101': [0, 0, 0, 0],
    'mdwf_cls_H200': [0, 0, 0, 0, 0, 0, 0, 0],
    'a15m400trMc_a': [0, 0, 0, 0, 0, 0, 0, 0],
    'a12m400trMc_a': [0, 0, 0, 0, 0, 0, 0, 0],
    'a09m400trMc_a': [0, 0, 0, 0, 0, 0, 0, 0],
    'a06m400trMc_a': [0, 0, 0, 0, 0, 0, 0, 0],
    'a064_m400_mL6.4_trMc': [0, 0, 0, 0, 0, 0, 0, 0],
    'a094_m400_mL6.0_trMc': [0, 0, 0, 0, 0, 0, 0, 0],
    'a12_m400_mL6.0_trMc': [0, 0, 0, 0, 0, 0, 0, 0],
    'A653': [0, 0, 0, 0],
    'B450': [0, 0, 0, 0, 0, 0, 0, 0],
    'B451': [0, 0, 0, 0],
    'B452': [0, 0, 0, 0],
    'H101': [24, 40, 55, 71],
    'H102': [24, 40, 55, 71],
    'H107': [24, 40, 55, 71],
    'H200': [0, 4, 8, 12, 16, 20, 24, 28],
    'J500': [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77],
    'N200': [0, 6, 12, 18, 24, 30, 36, 42],
    'N202': [0, 6, 12, 18, 24, 30, 36, 42],
    'N300': [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44],
    'N451': [0, 0, 0, 0, 0, 0, 0, 0],
    'U102': [32, 48, 64, 79, 95],
    'U103': [32, 48, 64, 79, 95],
    'U103_60modes': [32, 48, 64, 79, 95],
    'U103_4': [32, 48, 64, 79, 95],
    'E1':   [0, 0, 0, 0, 0, 0, 0, 0],
    'E5':   [0, 0, 0, 0],
}

pseudoscalar_names = {
    'Scls_cls_A653': ['ps'],
    'Scls_cls_A653_t0.125': ['ps'],
    'Scls_cls_B450': ['ps'],
    'mdwf_cls_A653': ['ps'],
    'mdwf_cls_A653_t0.4': ['ps'],
    'mdwf_cls_B450': ['ps'],
    'mdwf_cls_H101_r000': ['ps'],
    'mdwf_cls_H101': ['ps'],
    'mdwf_cls_H200': ['ps'],
    'a15m400trMc_a': ['ps'],
    'a12m400trMc_a': ['ps'],
    'a09m400trMc_a': ['ps'],
    'a06m400trMc_a': ['ps'],
    'a064_m400_mL6.4_trMc': ['ps'],
    'a094_m400_mL6.0_trMc': ['ps'],
    'a12_m400_mL6.0_trMc': ['ps'],
    'A653': ['ps'],
    'B450': ['ps'],
    'B451': ['pion', 'kaon', 'eta_s'],
    'B452': ['pion', 'kaon', 'eta_s'],
    'H101': ['ps'],
    'H102': ['pion', 'kaon', 'eta_s'],
    'H107': ['pion', 'kaon', 'eta_s'],
    'H200': ['ps'],
    'J500': ['ps'],
    'N200': ['pion', 'kaon', 'eta_s'],
    'N202': ['ps'],
    'N300': ['ps'],
    'N451': ['pion', 'kaon', 'eta_s'],
    'U102': ['pion', 'kaon', 'eta_s'],
    'U103': ['ps'],
    'U103_60modes': ['ps'],
    'U103_4': ['ps'],
    'E1':   ['ps'],
    'E5':   ['pion'],
}

pseudoscalar_op_strs = {
    'Scls_cls_A653': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'Scls_cls_A653_t0.125': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'Scls_cls_B450': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'mdwf_cls_A653': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'mdwf_cls_A653_t0.4': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'mdwf_cls_B450': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'mdwf_cls_H101_r000': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'mdwf_cls_H101': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'mdwf_cls_H200': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'a15m400trMc_a': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'a12m400trMc_a': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'a09m400trMc_a': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'a06m400trMc_a': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'a064_m400_mL6.4_trMc': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'a094_m400_mL6.0_trMc': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'a12_m400_mL6.0_trMc': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'A653': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'B450': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'B451': {
      'pion': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
      'kaon': "Flavor=1h,1 Pref=(0,0,0) A1u kaon 0",
      'eta_s': "Flavor=0,0 Pref=(0,0,0) A1up eta_s 0",
    },
    'B452': {
      'pion': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
      'kaon': "Flavor=1h,1 Pref=(0,0,0) A1u kaon 0",
      'eta_s': "Flavor=0,0 Pref=(0,0,0) A1up eta_s 0",
    },
    'H101': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'H102': {
      'pion': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
      'kaon': "Flavor=1h,1 Pref=(0,0,0) A1u kaon 0",
      'eta_s': "Flavor=0,0 Pref=(0,0,0) A1up eta_s 0",
    },
    'H107': {
      'pion': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
      'kaon': "Flavor=1h,1 Pref=(0,0,0) A1u kaon 0",
      'eta_s': "Flavor=0,0 Pref=(0,0,0) A1up eta_s 0",
    },
    'H200': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'J500': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'N200': {
      'pion': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
      'kaon': "Flavor=1h,1 Pref=(0,0,0) A1u kaon 0",
      'eta_s': "Flavor=0,0 Pref=(0,0,0) A1up eta_s 0",
    },
    'N202': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'N300': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'N451': {
      'pion': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
      'kaon': "Flavor=1h,1 Pref=(0,0,0) A1u kaon 0",
      'eta_s': "Flavor=0,0 Pref=(0,0,0) A1up eta_s 0",
    },
    'U102': {
      'pion': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
      'kaon': "Flavor=1h,1 Pref=(0,0,0) A1u kaon 0",
      'eta_s': "Flavor=0,0 Pref=(0,0,0) A1up eta_s 0",
    },
    'U103': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'U103_60modes': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'U103_4': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'E1': {
      'ps': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
    'E5': {
      'pion': "Flavor=1,0 Pref=(0,0,0) A1um pion 0",
    },
}

tsrc_files = {
    'H200': 'tsrc_list_H200',
    'J500': 'tsrc_list_J500',
    'N200': 'tsrc_list_N200',
    'N202': 'tsrc_list_N202',
    'N300': 'tsrc_list_N300',
}

decuplet_ensembles = [
    'Scls_cls_A653',
    'Scls_cls_A653_t0.125',
    'Scls_cls_B450',
    'mdwf_cls_A653',
    'mdwf_cls_A653_t0.4',
    'mdwf_cls_B450',
    'mdwf_cls_H101_r000',
    'mdwf_cls_H101',
    'mdwf_cls_H200',
    'a15m400trMc_a',
    'a12m400trMc_a',
    'a09m400trMc_a',
    'a06m400trMc_a',
    'a064_m400_mL6.4_trMc',
    'a12_m400_mL6.0_trMc',
    'A653',
    'B450',
    'H101',
    'H102',
    'H107',
    'H200',
    'J500',
    'N200',
    'N202',
    'N300',
    'N451',
    'U103',
]

# operator info
SU3_flavors = ["1", "27", "10", "10b", "8"]
SU2_flavors = ["I0_S0", "I1_S0", "I0_S-2", "I1_S-2", "I2_S-2"]
irrep_spin_ordering = "I0_S-2"
symmetric_SU3_flavors = ["1", "27", "8"]
anti_symmetric_SU3_flavors = ["10", "10b", "8"]
symmetric_SU2_flavor = "I1_S0"
anti_symmetric_SU2_flavor = "I0_S0"
symmetric_SU3_flavor_dibaryon = "NNs"
anti_symmetric_SU3_flavor_dibaryon = "NNa"

op_files = {
    'S0': "operators_S0",
    'S-2': "operators_S-2",
}

baryon_flavor = {
    'nucleon':  '1h,0',
    'lambda':   '0,-1',
    'sigma':    '1,-1',
    'xi':       '1h,-2',
    'octet':    '8',
    'decuplet': '10',
}

spin_half_irreps = {
    0: 'G1g',
    1: 'G1',
    2: 'G',
    3: 'G',
    4: 'G1',
}

spin_three_half_irreps = {
    0: 'Hg',
}

total_prefs = {
    0: '(0,0,0)',
    1: '(0,0,1)',
    2: '(0,1,1)',
    3: '(1,1,1)',
}

def convert_irrep(irrep, psq):
  if psq == 2 and irrep == "B1":
    return "B2"
  elif psq == 2 and irrep == "B2":
    return "B1"
  elif irrep == "E2":
    return "E"

  return irrep.replace("+", "g").replace("-", "u")


def get_opstr(su3, pref, irrep, flavor, op_str):
  psq = int(pref[1])**2 + int(pref[2])**2 + int(pref[3])**2
  pref = f"Pref=({pref[1]},{pref[2]},{pref[3]})"
  irrep = convert_irrep(irrep, psq)
  if not su3:
    isospin, strangeness = flavor.split('_')
    isospin = isospin[1:]
    strangeness = strangeness[1:]
    flavor = f"{isospin},{strangeness}"

  return f"Flavor={flavor} {pref} {irrep} {op_str}"
